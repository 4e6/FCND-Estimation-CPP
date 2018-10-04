# Read sensor data to figure out the stdev

import csv
import numpy as np

lines = []
with open('config/log/Graph2.txt') as f:
    reader = csv.reader(f, delimiter=',')
    lines = list(reader)

values = np.array([float(line[1]) for line in lines[1:]])
stdev = np.std(values)
print('stdev =', stdev)
