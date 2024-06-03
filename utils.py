import pandas as pd
import numpy as np
import ast 
import re

# Function to clean the mobadla column
def clean_mobadla(series):
    try:
        cleaned_series = series.str.extract(r'(\d+\.?\d*)').astype(float)
        return cleaned_series
    except AttributeError:
        return np.nan
    except ValueError:
        return np.nan
    
    
def calculate_rate_sqft(mobadla, kshetrafal):
    try:
        rate_sqft = mobadla / (kshetrafal * 10.764)
        return rate_sqft
    except ZeroDivisionError:
        return np.nan
    except TypeError:
        return np.nan
    except ValueError:
        return np.nan
    