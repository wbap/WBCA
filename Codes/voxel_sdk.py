# -*- coding: utf-8 -*-

from  __future__  import print_function
import time
import os
import nrrd
from allensdk.config.manifest import Manifest
from allensdk.api.queries.ontologies_api import OntologiesApi
from allensdk.core.structure_tree import StructureTree
from allensdk.core.reference_space import ReferenceSpace
from allensdk.api.queries.mouse_connectivity_api import MouseConnectivityApi
import warnings
warnings.filterwarnings('ignore')
import numpy as np

def Ref():

    oapi = OntologiesApi()
    structure_graph = oapi.get_structures_with_sets([1])
    structure_graph = StructureTree.clean_structures(structure_graph)
    tree = StructureTree(structure_graph)

#     "need to download annotation the first time"
#     annotation_dir = 'annotation'
#     Manifest.safe_mkdir(annotation_dir)
#     annotation_path = os.path.join(annotation_dir, 'annotation.nrrd')
    annotation_path = 'annotation_2017_25.nrrd'

#     mcapi = MouseConnectivityApi()
#     mcapi.download_annotation_volume('annotation/ccf_2016', 25, annotation_path)

    annotation, meta = nrrd.read(annotation_path)
    
    rsp = ReferenceSpace(tree, annotation, [25, 25, 25])

    import pandas as pd
    df = pd.read_csv('ontology_170731.csv')
    
    idList = df['id']
    acronymList = df['acronym']
    nameList = df['name']

    voxel_count = [rsp.total_voxel_map[int(stid)] for stid in df['id']]
    
    df = pd.DataFrame(np.column_stack([idList, acronymList, nameList, voxel_count]), 
                      columns=['ID','Acronym','Name','Total Voxel'])
    df.to_csv('s2_{}.csv'.format(time.strftime('%y%m%d')))


Ref()