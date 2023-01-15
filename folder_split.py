'''
Test-train-validation split

This script will divide sorted images into test/train/validation folders

The target folder must contain subfolders containing images sorted by class

The designated directory will contain copies of the images in labeled folders
'''

import splitfolders

print('Splitting folders')

splitfolders.ratio('~/data/Sorted Photos', output='~/data/data_07', seed=6489, ratio=(.8, .1, .1)) 

print('Splitting complete')