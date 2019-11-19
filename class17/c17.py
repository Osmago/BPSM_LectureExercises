#!/bin/usr/python3

import pandas as pd	
import matplotlib.pyplot as plt

df = pd.read_csv('eukaryotes.tsv', sep="\t", na_values='-')

df
