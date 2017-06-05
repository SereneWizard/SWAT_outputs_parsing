# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import collections
import numpy as np
import pandas as pd


rchFile = 'output.hru'


cols2Extract = [('LULC', (1, 4)),
                ('HRU', (5,9)), 
                ('year', (30, 34)), 
                ('surfaceQ', (215, 224)), 
                ('lateralQ', (235, 244)), 
                ('NSURQ', (575, 584)), 
                ('NLATQ', (585, 594)), 
                ('Yield_tonperha', (695, 704)), 
                ('TileQ', (777, 786)), 
                ('TileNO3', (787, 796))]
cols2Extract = collections.OrderedDict(cols2Extract)

col_positions = list(cols2Extract.values())
col_names = list(cols2Extract.keys())
nyears = 20
df_weird = pd.read_fwf(rchFile, colspecs=col_positions, names=col_names, 
                       skiprows=8)
df= pd.read_fwf(rchFile, colspecs=col_positions, skiprows=8)
df.columns = col_names
filtered_df = df.loc[df['year'] <= nyears]
filtered_df.to_csv('output_hru.csv', sep=',', index=False)

