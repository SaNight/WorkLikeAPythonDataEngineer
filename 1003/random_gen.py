import numpy as np
import pandas as pd
import csv
import argparse

parser = argparse.ArgumentParser(description='Create a custom num matrix(81*81)')
parser.add_argument('num', type=int)
args=parser.parse_args()

output_filename = 'random_matrix.csv'
random_output = np.random.uniform(-args.num,args.num,(81,81))
pd.DataFrame(random_output).to_csv(output_filename,header=None,index=None)
