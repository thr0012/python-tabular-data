#!/usr/bin/env python3

import argparse
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
 
 
def load_data(csv_path):

    return pd.read_csv(csv_path)

def run_linear_regression(x, y):
    result = stats.linregress(x, y)
    return result.slope, result.intercept, result.rvalue, result.pvalue, result.stderr
 
