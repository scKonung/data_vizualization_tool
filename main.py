import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Read a csv file from source
print("Please write a source to a csv file:")
print("(0) - Cancel")
while(True):
    input_source = input()
    if (input_source.__eq__("0")):
        break
    try:
        data = pd.read_csv(input_source)
        break
    except:
        print("ERROR: Could find file by this source:" + input_source)
        print("Please try again write a source to a csv file or cancel(0)")