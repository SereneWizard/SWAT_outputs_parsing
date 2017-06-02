# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import collections
import numpy as np
import pandas as pd


rchFile = 'output.rch'


cols2Extract = [('SUB', (6, 10)), 
                ('year', (20, 25)), 
                ('flow', (38, 50)), 
                ('nitrate', (542, 553)), 
                ('phosphorus', (554, 565))]
cols2Extract = collections.OrderedDict(cols2Extract)

col_positions = list(cols2Extract.values())
col_names = list(cols2Extract.keys())
nyears = 20
df_weird = pd.read_fwf(rchFile, colspecs=col_positions, names=col_names, 
                       skiprows=8)
df= pd.read_fwf(rchFile, colspecs=col_positions, skiprows=8)
df.columns = col_names
filtered_df = df.loc[df['year'] <= nyears]
filtered_df.to_csv('output_rch.csv', sep=',', index=False)

