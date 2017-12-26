#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
table2brical.py
=====
This module contains the class `Table2BriCAL` which converts table files
describing connectome into a BriCA language JSON file.
Changes made are as follows:
"__init__": Added some initial lists and dictionary for making port sizes
            Added acronyms of thalamus # added by hayami
"loadHierarchy": Added codes to import source and target lists and ports
"build": Changed var to abs(var)
         Added and imported port sizes
         Added thresholds of thalamus # added by hayami
"removeModules": Created to remove modules do not have any ports including super modules # added by hayami
"createPort": Imports port sizes into "Shape"
"createConnection": Added connectivity strengths as conn in a parameter and ff/fb
                    as ff_fb to distinguish by a negative or a positive number in Comment section
"main": Added thresholds of thalamus # added by hayami
"""

import sys
import os
import json

class Table2BriCAL:
    """
    converts table files describing connectome into a BriCA language JSON file.
    """

    def __init__(self):
        self.json={}
        self.connection={}
        self.regions={}
        self.superModules={}
        self.subModules={}
        self.modules={}
        self.ports=[]
        self.connections=[]
        self.headItems=None

        self.temp_source=[]
        self.temp_target=[]
        self.temp_port={}
        self.thalamus = ['VAL','VM','VPL','VPLpc','VPM','VPMpc','SPFm','SPFp','SPA',
                         'PP','MG','LGd','LP','PO','POL','SGN','AV','AM','AD',
                         'IAM','IAD','LD','IMD','MD','SMT','PR','PVT','PT','RE','RH','CM','PCN'
                         'CL','PF','RT','IGL','LGv','SubG','MH','LH']

    def loadConnection(self, path):
        heading = True
        for line in open(path, 'r'):
            items = line[:-1].split('\t')
            if heading:
                self.headItems = items[1:]
                heading = False
            else:
                self.connection[items[0]]=items[1:]

    def loadRegions(self, path):
        for line in open(path, 'r'):
            items = line[:-1].split('\t')
            if len(items) < 4:
                break
            module={}
            module["Name"]=items[1]
            module["Comment"]=items[3]
            self.modules[items[0]]=module

    def loadHierarchy(self, path):
        with open(path, 'r') as f:
            for key, line in enumerate(f):
                strs = line.strip('\n').split('\t')
                if key == 0:
                    self.temp_target = strs[3:]
                else:
                    self.temp_source.append(strs[2])
                    self.temp_port[strs[2]] = strs[3:]
                    if strs[0] in self.modules and strs[1] in self.modules:
                        self.superModules[strs[0]] = strs[1]
                        if strs[1] in self.subModules:
                            subModules = self.subModules[strs[1]]
                        else:
                            subModules = []
                        subModules.append(strs[0])
                        self.subModules[strs[1]] = subModules


    def build(self, threshold):
        for id in self.connection:
            originName = self.modules[id]["Name"]
            items = self.connection[id]
            p_sizes = self.temp_port[id]
            for i in range(0, len(items)):
                try:
                    if items[i].strip() == '':
                        items[i] = '0'
                    var = float(items[i])
                    p_size = float(p_sizes[i])
                except:
                    print("Cannot convert item " + str(i) + ":'" + items[i] + "' for id:" + id + ".")

                targetID = self.headItems[i]
                targetName = self.modules[targetID]["Name"]
                originModule = self.modules[id]
                targetModule = self.modules[targetID]
                if originName in self.thalamus or targetName in self.thalamus:
                    if var >= threshold[1]:
                        self.createPort("Output", originModule, originName, targetName, p_size)
                        self.createPort("Input", targetModule, originName, targetName, p_size)
                        self.createConnection(id, targetID, var)

                    elif var <= - threshold[2]:
                        self.createPort("Output", originModule, originName, targetName, p_size)
                        self.createPort("Input", targetModule, originName, targetName, p_size)
                        self.createConnection(id, targetID, var)

                else:
                    if abs(var) >= threshold[0]:
                        self.createPort("Output", originModule, originName, targetName, p_size)
                        self.createPort("Input", targetModule, originName, targetName, p_size)
                        self.createConnection(id, targetID, var)
        self.addHierarchyToModules()
        self.removeModules()

    def removeModules(self):
        for id in self.connection:
            if self.superModules.has_key(id): # if subregion
                if not self.modules[id].has_key("Ports"): # have any port
                    self.modules[self.modules[id]["SuperModule"]]['SubModules'].remove(id)
                    del(self.modules[id])
                    for port in self.ports:
                        if port["Module"] == id:
                            self.ports.remove(port)
                    for connection in self.connections:
                        if connection["FromModule"] == id or connection["ToModule"] == id:
                            self.connections.remove(connection)
        for subModule in self.subModules:
            del(self.modules[subModule])

        for module in self.modules:
            del(self.modules[module]["SuperModule"])


    def createPort(self, type, module, origin, target, size):
        portName = self.alterModuleName(origin) + "-" + self.alterModuleName(target) + "-" + type
        if "Ports" in module:
            ports = module["Ports"]
        else:
            ports = []
        ports.append(portName)
        module["Ports"] = ports
        port = {}
        port["Name"] = portName
        port["Module"] = module["Name"]
        port["Type"] = type
        port["Shape"] = [int(round(size))]
        if type == "Input":
            port["Comment"] = "An input port of " + target + " for connection from " + origin
        else:
            port["Comment"] = "An output port of " + origin + " for connection to " + target
        self.ports.append(port)

    def createConnection(self, originID, targetID, conn):
        originName = self.modules[originID]["Name"]
        targetName = self.modules[targetID]["Name"]
        connection = {}
        connectionName = originName + "-" + targetName
        connection["Name"] = connectionName
        connection["FromModule"] = originName
        connection["ToModule"] = targetName
        outputPortName = self.alterModuleName(originName) + "-" + self.alterModuleName(targetName) + "-Output"
        inputPortName = self.alterModuleName(originName) + "-" + self.alterModuleName(targetName) + "-Input"
        connection["FromPort"] = outputPortName # self.getPath(originID) + "/" + outputPortName
        connection["ToPort"] = inputPortName    # self.getPath(targetID) + "/" + inputPortName
        if conn < 0:
            ff_fb = "FB"
        elif conn > 0:
            ff_fb = "FF"
        else:
            ff_fb = "None"
        connection["Comment"] = "A connection from " + originName + " to " + targetName + ", Connectivity Strength: "\
                                + str(abs(conn)) + ", FF-FB: " + ff_fb
        self.connections.append(connection)

    @staticmethod
    def alterModuleName(name):
        return name.replace('.', '#')

    def addHierarchyToModules(self):
        for moduleID in self.modules:
            module = self.modules[moduleID]
            if moduleID in self.superModules:
                module["SuperModule"] = self.superModules[moduleID]
            if moduleID in self.subModules:
                module["SubModules"] = self.subModules[moduleID]

    def getPath(self, id):
        pathList = [id]
        while id in self.superModules:
            pathList.append(self.superModules[id])
            id = self.superModules[id]
        path = ""
        for id in reversed(pathList):
            if path == "":
                path = self.modules[id]["Name"]
            else:
                path = path + "/" + self.modules[id]["Name"]
        return path

    def writeJSON(self, path, base):
        fp = open(path, 'w')
        header = {}
        header["Type"]="A"
        basename = os.path.basename(path)
        if "." in basename:
            header["Name"]=basename[0:basename.rfind(".")]
        else:
            header["Name"] = basename
        header["Base"] = base
        self.json["Header"]=header
        modules = []
        for module in self.modules:
            modules.append(self.modules[module])
        self.json["Modules"]=modules
        self.json["Ports"] = self.ports
        self.json["Connections"] = self.connections
        json.dump(self.json, fp, indent=1)
        fp.close()

if __name__ == '__main__':
    if len(sys.argv)!=9:
        print('Usage: table2brical.py connection.txt regions.txt hierarchy.txt output.json prefix threshold_isocortex threshold_thalamus_ff threshold_thalamus_fb')
        quit()
    params = sys.argv
    threshold = [float(params[6]),float(params[7]),float(params[8])]
    t2b = Table2BriCAL()
    t2b.loadConnection(params[1])
    t2b.loadRegions(params[2])
    t2b.loadHierarchy(params[3])
    t2b.build(threshold)
    t2b.writeJSON(params[4], params[5])
