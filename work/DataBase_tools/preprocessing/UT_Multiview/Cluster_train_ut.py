import numpy as np
import os
# Usage:
# => Build a new folder named ClusterLabel
# => Move this code into the new Folder
# => Using python Cluster.py to run it.
# => Remove this code from the new Folder.
path = "Z:\\UTMULTIVIEW\\data\\labeldata\\synth"

filelists = [18,  6, 45,  7, 17, 24, 43, 36, 35, 46, 12,  9, 29, 42, 40, 34, 20, 37, 13, 44,  5, 30, 47, 25, 19,  8,  1, 14, 31, 26, 39, 23, 33, 16, 22,  0,  4, 11, 28, 27,  2, 38, 41, 32, 21,  3, 15, 10]
filelength = [16, 16, 16]

begin = 0
for i in range(3):
  curlists = filelists[begin: begin+filelength[i]]
  begin = begin + filelength[i]
  print(curlists)
  contents = []

  for j in range(len(curlists)):

    if curlists[j] < 10: 
        filename = os.path.join(path, f"s0{curlists[j]}.label")
    else:
        filename = os.path.join(path, f"s{curlists[j]}.label")

    with open(filename) as infile:
      lines = infile.readlines()
      header = lines.pop(0)
      contents += lines
  with open(f"Cluster{i}.label", 'w') as outfile:
    outfile.write(header)
    for content in contents:
      outfile.write(content)


    
      


