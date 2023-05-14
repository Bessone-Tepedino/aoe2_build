# Base packages

import pandas as pd
pd.set_option("display.max_columns", 100)
pd.set_option("display.max_rows", 100)

import numpy as np
# allows annotation of arguments with multiple types
from typing import Union
import pickle

import datetime

# SQL

import re
import itertools
from collections import defaultdict

# Additional packages
# from plotnine import *
# from linearmodels import IV2SLS
# from sparseiv.sparse_iv_regress import SparseIVRegress as sr

# allows you to write sql clauses to filter dataframes
# import pandasql as psql
# psql.sqldf(query, locals())

def move_column(df: pd.DataFrame, cols_to_move: Union[list, str], ref_col: str, relative_position = 'after'):
    """
    Move a column to a new position in the dataframe
    :param df: dataframe
    :param cols_to_move: list or string of columns to move
    :param ref_col: column to move relative to
    :param relative_position: 'before' or 'after' the reference column. The default is 'after'

    :return: dataframe with moved columns
    """

    if isinstance(cols_to_move, str):
        cols_to_move = [cols_to_move]

    index = df.columns.get_loc(ref_col)
    if relative_position == 'after':
        for col in cols_to_move:
            index +=1
            df.insert(index, col, df.pop(col))
            # need to restart the index since the ref columns may have changed position after the popping
            index = df.columns.get_loc(ref_col)

    elif relative_position == 'before':
        for col in cols_to_move:
            df.insert(index, col, df.pop(col))
            # need to restart the index since the ref columns may have changed position after the popping
            index = df.columns.get_loc(ref_col)

    else:
        raise ValueError('relative_position must be either "before" or "after"')
    
    return df
   
## load pickled object
def load_obj(target: str):
    '''
    target should be the name of the file. You don't need to add the .pickle extension
    '''
    with open(f'{target}.pickle', 'rb') as f:
        e = pickle.load(f)
    return e

## save pickled object
def save_obj(obj, target: str):
    '''
    target should be the name of the file. You don't need to add the .pickle extension
    '''
    with open(f'{target}.pickle', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL) 

def list_to_str_list(lst):
    '''Converts a list of values to a list of string representations of those values.'''
    return ["'" + str(x) + "'" for x in lst]

## Print SQL Code
def print_sql_code(ml_string: str):
    
    '''
    Prints SQL code with line numbers for each line.

    Args:
        sql: A multiline SQL string to format and print.

    Returns:
        None.
    '''
    
    # Split the multiline string into individual lines and create a list of formatted lines with line numbers
    formatted_lines = [f"{i}: {line}" for i, line in enumerate(ml_string.splitlines(), start=1)]

    # Concatenate the formatted lines with line breaks
    formatted_string = "\n".join(formatted_lines)

    # Print the formatted string
    print(formatted_string)
    
