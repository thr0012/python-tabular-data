#!/usr/bin/env python3

import argparse
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
 
 
def load_data(csv_path):
    """ Load the csv data """
    return pd.read_csv(csv_path)

def run_linear_regression(x, y):
    """Run a simple linear regression"""
    result = stats.linregress(x, y)
    return result.slope, result.intercept, result.rvalue, result.pvalue, result.stderr

def plot_species_regression(ax, species_df, species_name, color): 
    """plot the regressions"""
    x = species_df["petal_length_cm"]
    y = species_df["sepal_length_cm"]

    result = stats.linregress(x,y)
    return result.slope, result.intercept, result.rvalue, result.pvalue, result.stderr

def plot_species_regression (ax, species_df, species_name, color):
    """Scatter plot with the regression line"""
    x = species_df["petal_length_cm"]
    y = species_df["sepal_length_cm"]
 
    slope, intercept, r_value, p_value, _ = run_linear_regression(x, y)
 
    ax.scatter(x, y, color=color, alpha=0.6, label="Data")
    ax.plot(
        x.sort_values(),
        slope * x.sort_values() + intercept,
        color="black",
        linewidth=1.5,
        label=f"y = {slope:.2f}x + {intercept:.2f}\n$R^2$ = {r_value**2:.3f}, p = {p_value:.2e}",
    )
 
    ax.set_title(species_name.replace("_", " "), style="italic", fontsize=11)
    ax.set_xlabel("Petal length (cm)")
    ax.set_ylabel("Sepal length (cm)")
    ax.legend(fontsize=8)
