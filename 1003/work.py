import numpy as np
import pandas as pd
import csv
import skimage.measure

def import_random_matrix(filename):
    return pd.read_csv(filename,header=None).values

def reduce_matrix_max(matrix,stride):
    temp_matrix = skimage.measure.block_reduce(matrix,stride,np.max)
    return skimage.measure.block_reduce(temp_matrix,stride,np.max)

def reduce_matrix_mean(matrix,stride):
    temp_matrix = skimage.measure.block_reduce(matrix,stride,np.mean)
    return skimage.measure.block_reduce(matrix,stride,np.mean)

input_filename = 'random_matrix.csv'
random_matrix = import_random_matrix(input_filename)

stride = 3
reduce_matrix_max = reduce_matrix_max(random_matrix,stride)
pd.DataFrame(reduce_matrix_max).to_csv('reduce_matrix_maxpooling.csv',header=None,index=None)
print(f'MaxPooling Matrix Shape: {reduce_matrix_max.shape}')
reduce_matrix_mean = reduce_matrix_mean(random_matrix,stride)
pd.DataFrame(reduce_matrix_mean).to_csv('reduce_matrix_avepooling.csv',header=None,index=None)
print(f'AvePooling Matrix Shape: {reduce_matrix_mean.shape}')