#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import numpy as np
import pandas as pd
import itertools
import matplotlib.pyplot as plt

PATH = '/Users/rintarokomori/Desktop/assignment/'


def num_cell_method1():
    # one way to convert voxel -> num_cell (code below shows the concatenation of just the two major regions)

    df = pd.read_csv('s2_compare.csv', index_col=0, header=0)

    acronymList = list(df['Acronym'])
    nameList = list(df['Name'])
    regionList = list(df['Major_Region'])
    voxelList_iso = np.array(df['Voxel_kom_2017']) / 7891055 * 8000000
    voxelList_hippo = np.array(df['Voxel_kom_2017']) / 2729405 * 5000000

    df1 = pd.DataFrame(np.column_stack([acronymList[6:379], nameList[6:379], regionList[6:379], voxelList_iso[6:379]]),
                       columns=['Acronym', 'Name', 'Region', 'Voxel'])
    df2 = pd.DataFrame(
        np.column_stack([acronymList[455:555], nameList[455:555], regionList[455:555], voxelList_hippo[455:555]]),
        columns=['Acronym', 'Name', 'Region', 'Voxel'])

    # frames = [df1, df2]
    # result = pd.concat(frames)
    result = df1.append(df2)
    print (result)

def organize_s2compare():
    # 1. delete unnnecessary columns from s2_compare.csv
    # 2. delete unnecessary rows if major_region is not in majorreg_list
    # 3. define cerebral nuclei to be Striatum and Pallidum combined

    df = pd.read_csv('{}s2_compare.csv'.format(PATH), index_col=0, header=0)

    delete_list = ['ID', 'Voxel_so_2016', 'Voxel_oh_bef2014']
    df = df.drop(delete_list, 1)

    majorreg_list = ['Cerebellum', 'Isocortex', 'Hippocampal formation', 'Olfactory areas', 'Cortical subplate',
                   'Striatum', 'Pallidum', 'Thalamus', 'Hypothalamus', 'Midbrain', 'Medulla', 'Pons']

    delete_list = [key for key, reg in enumerate(df['Major_Region']) if reg not in majorreg_list]
    df = df.drop(delete_list, 0)

    for key, row in df.iterrows():
        if row[2] == 'Striatum' or row[2] == 'Pallidum':
            df.at[key, 'Major_Region'] = 'Cerebral nuclei'

    df.to_csv('{}voxel_region.csv'.format(PATH), header=True, index=True)

def reglist_unique():
    # the region acronym in row and column of conn_matrix do not match.
    # from conn matrix, create two columns (From and To) with unique region names → (292 rows * 2 columns)

    conn_matrix = pd.read_csv('Table2BriCAL/new/conn_matrix.csv', index_col=0, header=0)
    # temp = list(conn_matrix.index)+list(conn_matrix.columns)
    # print(len(temp))

    new_acronym_list = np.unique(list(conn_matrix.index) + list(conn_matrix.columns))
    print(len(new_acronym_list))

    temp2 = list(itertools.product(new_acronym_list, new_acronym_list))
    col1 = [x for x, y in temp2]
    col2 = [y for x, y in temp2]

    df1 = pd.DataFrame(np.column_stack([col1, col2]), columns=['From', 'To'])
    # df1.to_csv('{}final_{}.csv'.format(PATH, time.strftime('%y%m%d')))
    df1.to_csv('{}finale.csv'.format(PATH))

def voxel_vs_connstr():
    # 1. print out volume(voxel) of region in [From],[To], and also the value that multiplies the two
    # 2. prints out a voxel**2 vs. connectivity graph

    df1 = pd.read_csv('{}voxel_region.csv'.format(PATH), index_col=0, header=0)
    df2 = pd.read_csv('{}finale.csv'.format(PATH), index_col=0, header=0)

    temp1 = []
    for acronym in df2['From']:
        for x, y in zip(df1['Acronym'], df1['Voxel_kom_2017']):
            if acronym == x:
                temp1.append(y)
    df2['V(s)'] = temp1

    temp2 = []
    for acronym in df2['To']:
        for x, y in zip(df1['Acronym'], df1['Voxel_kom_2017']):
            if acronym == x:
                temp2.append(y)
    df2['V(t)'] = temp2

    df2['V(s)*V(t)'] = df2['V(s)'] * df2['V(t)']
    #print(df2.shape)

    df2.to_csv('{}finale.csv'.format(PATH), header=True, index=True)

    # connectivity = []
    # volume = []
    #
    # for key, row in df2.iterrows():
    #     if row[6] != 0:
    #         connectivity.append(row[6])
    #         volume.append(row[4])
    # x = volume
    # y = connectivity
    #
    # plt.scatter(x, y, color='red', marker='o')
    # plt.xlabel('V(s)*V(t)')
    # plt.ylabel('Connectivity Strength')
    # plt.show()

def num_cell_method2():
    # convert voxel -> num_cell of each region

    df1 = pd.read_csv('{}voxel_region.csv'.format(PATH), index_col=0, header=0)
    df2 = pd.read_csv('{}finale.csv'.format(PATH), index_col=0, header=0)

    num_cell_dict = {'Cerebellum': 40000000, 'Isocortex': 8000000, 'Hippocampal formation': 5000000,
                     'Olfactory areas': 1000000, 'Cortical subplate': 1000000,
                     'Cerebral nuclei': 10000000, 'Thalamus': 8000000, 'Hypothalamus': 1000000,
                     'Midbrain': 2000000, 'Medulla': 2000000, 'Pons': 2000000}
    total_voxel_dict = {'Cerebellum': 3445073, 'Isocortex': 7891055, 'Hippocampal formation': 2729405,
                        'Olfactory areas': 2988743, 'Cortical subplate': 569974,
                        'Cerebral nuclei': 2877420 + 599514, 'Thalamus': 1297712, 'Hypothalamus': 972554,
                        'Midbrain': 2351722, 'Medulla': 1981978, 'Pons': 1069305}

    temp = []
    for index, tmp in df2.iterrows():
        # print(tmp[['From', 'V(s)']])
        df_tmp = df1[(df1.Acronym == tmp['From'])]
        a = df_tmp.Major_Region
        # if a in num_cell_dict:
        # print(a.values[0])
        major_region = a.values[0]
        v = tmp['V(s)'] * num_cell_dict[major_region] / total_voxel_dict[major_region]
        temp.append(v)
    # print(temp)
    df2['num_cell(from)'] = temp
    df2.to_csv('{}finale.csv'.format(PATH))

def connectivitystr():
    # fill in connectivity_strength_row with the matching (From)->(To) pair

    df = pd.read_csv('{}finale.csv'.format(PATH), index_col=0, header=0)
    df2 = pd.read_csv('{}Table2BriCAL/new/conn_matrix.csv'.format(PATH), index_col=0, header=0)
    temp = []
    for x, y in zip(df['From'],df['To']):
        try:
            temp.append(abs(df2.at[x,y]))
        except:
            temp.append(0.0)
    df['Connectivity_Strength'] = temp
    df.to_csv('{}finale.csv'.format(PATH))


def totalcs():
    #total conn_str from [From reg]

    df = pd.read_csv('{}finale.csv'.format(PATH),index_col=0,header=0)

    acronym_list = np.unique([x for x in df['From']])
    total_cs = {}
    for acr in acronym_list:
        temp = df[df['From'] == '{}'.format(acr)]
        total_cs['{}'.format(acr)] = sum(temp['Connectivity_Strength'])

    totalcsList = [total_cs['{}'.format(acr)] for acr in df['From']]
    df['total_cs_from'] = totalcsList

    df.to_csv('{}finale.csv'.format(PATH), index=True)

def n_out():
    # output port-size

    df = pd.read_csv('{}finale.csv'.format(PATH), index_col=0, header=0)
    # df['n_out'] = 0.0
    df['n_out'] = df['num_cell(from)'] * df['Connectivity_Strength'] / df['total_cs_from']

    df= df.fillna(0.0)

    df.to_csv('{}finale.csv'.format(PATH))

def matrix():
    # create a matrix with value of port-size

    df = pd.read_csv('{}finale.csv'.format(PATH),index_col=0,header=0)

    temp = np.unique(df['From'])

    df2 = pd.DataFrame(columns=temp, index= temp)

    for x, y, z in zip(df['From'], df['To'], df['n_out']):
       # print(x, y , z)
        df2.at[x,y] = z

    df2.to_csv('{}finale_matrix.csv'.format(PATH), index=True)

if __name__ == '__main__':
    organize_s2compare()
    reglist_unique()
    voxel_vs_connstr()
    num_cell_method2()
    connectivitystr()
    totalcs()
    n_out()
    matrix()
