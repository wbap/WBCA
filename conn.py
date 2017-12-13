#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

"""

from __future__ import print_function
import csv
import pandas as pd
import numpy as np


def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)


def loadMatrix():
    csv_file = 'raw_data/s4_ipsi_nnls_171203.csv'
    df = pd.read_csv(csv_file, index_col=0, header=0)

    fffb_file = 'raw_data/fffb_dawd.csv'
    fffb_df = pd.read_csv(fffb_file, header=0)

    for key, row in fffb_df.iterrows():
        if row[0] == 'FB':
            df.at[row[1], row[2]] = -df.at[row[1], row[2]]

    acronym_list = np.sort(np.unique(list(df.index) + list(df.columns)))

    df.to_csv('new/conn_matrix.csv', header=True, index=True)

    return acronym_list


def hierarchy(acronym_list):
    csv_file = 'raw_data/s2_171020.csv'
    df = pd.read_csv(csv_file, index_col=0, header=0)

    parent_list = ['Cerebellum', 'Isocortex', 'Hippocampal formation', 'Olfactory areas', 'Cortical subplate',
                   'Striatum', 'Pallidum', 'Thalamus','Hypothalamus', 'Midbrain', 'Medulla', 'Pons']

    hierarchy_list = []
    temp_list = []

    for ac, reg in zip(df['Acronym'], df['Major Region']):
        if ac in acronym_list and reg in parent_list:
            if reg == 'Striatum' or reg == 'Pallidum':
                temp_list.append('Cerebral nuclei')
            else:
                temp_list.append(reg)
            hierarchy_list.append(ac)

    csv_file1 = 'raw_data/finale_matrix.csv'
    df1 = pd.read_csv(csv_file1, header=0)

    df1.insert(loc=0, column='Region', value=temp_list)
    df1.insert(loc=0, column='Acronym', value=hierarchy_list)
    df1.to_csv('new/port_size_matrix.csv', index=0)

    with open('new/hierarchy.txt', 'w') as output_file:
        with open('new/port_size_matrix.csv', 'r') as input_file:
            [output_file.write('\t'.join(row) + '\n') for row in csv.reader(input_file)]
        # output_file.close()

    df1.to_csv('new/port_size_matrix.csv', header=True, index=True)

    return hierarchy_list


def extractMatrix(hierarchy_list):
    csv_file = 'new/conn_matrix.csv'
    df = pd.read_csv(csv_file, index_col=0, header=0)

    col_delete_list = [name for name in df.columns if name not in hierarchy_list]
    df = df.drop(col_delete_list, 1)
    idx_delete_list = [name for name in df.index if name not in hierarchy_list]
    df = df.drop(idx_delete_list, 0)

    add_list = [name for name in df.columns if name not in df.index]
    df2 = pd.DataFrame(0.0, index=add_list, columns=df.columns)
    df3= pd.concat([df, df2])
    df3.sort_index(axis=0, inplace=True)

    acronym_list = np.sort(np.unique(list(df.index) + list(df.columns)))

    df3.to_csv('new/conn_matrix.csv', header=True, index=True)

    return acronym_list


def connectivity():
    csv_file = 'new/conn_matrix.csv'
    df = pd.read_csv(csv_file, index_col=0, header=0)

    df.to_csv('new/conn_matrix.csv', header=True, index=True)

    with open('new/connection.txt', 'w') as my_output_file:
        with open(csv_file, 'r') as my_input_file:
            [my_output_file.write('\t'.join(row) + '\n') for row in csv.reader(my_input_file)]
        # my_output_file.close()


def blockDiagram():
    csv_file = 'new/conn_matrix.csv'
    df = pd.read_csv(csv_file, index_col=0, header=0)

    with open('new/blockDiagram.txt', 'w') as f:
        for idx in df.index:
            for col in df.columns:
                if df.at[idx, col] > 0:
                    f.write('{} --> {}\n'.format(idx, col))
                elif df.at[idx, col] < 0:
                    f.write('{} ==> {}\n'.format(idx, col))
                else:
                    continue


def region(acronym_list):
    csv_file = 'raw_data/ontology_170731.csv'
    df = pd.read_csv(csv_file, index_col=0, header=0)

    parent_list = ['Cerebellum', 'Isocortex', 'Hippocampal formation', 'Olfactory areas', 'Cortical subplate',
                   'Cerebral nuclei', 'Thalamus', 'Hypothalamus', 'Midbrain', 'Medulla', 'Pons']

    region_list = []
    with open('new/regions.txt', 'w') as f:
        for ac, name in zip(df['acronym'], df['safe_name']):
            if ac in acronym_list:
                f.write('{}\t{}\t{}\t{}\n'.format(ac, ac, name, name))
                region_list.append((ac, name))
        for par in parent_list:
            f.write('{}\t{}\t{}\t{}\n'.format(par, par, par, par))

    return region_list


if __name__ == '__main__':
    acronymList = loadMatrix()
    hierarchyList = hierarchy(acronymList)
    acronymList = extractMatrix(hierarchyList)
    connectivity()
    blockDiagram()
    regionList = region(acronymList)