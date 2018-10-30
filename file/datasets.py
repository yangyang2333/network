import pandas as pd
import numpy as np

def getData(path):
  dataset=pd.read_csv(path)
  matrix = []
  for i in range(len(dataset)):
      matrix.append(dataset[str(i)])
  m = np.array(matrix)
  return m




