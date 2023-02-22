import numpy
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")
from scipy.stats import ttest_ind, ttest_rel
from scipy import stats


# Run simple univariate analysis on a chosen column
def UnivariateAnalysis(conn, column):
    cursor = conn.cursor()
    cursor.execute(f'select SUM("{column}"), AVG("{column}"), COUNT("{column}") from steam_reviews')
    results = cursor.fetchone()

    print(f"{column}, Sum, %s" % results[0])
    print(f"{column}, Average, %s" % results[1])
    print(f"{column}, Count, %s" % results[2])

    # Dont run these yet lmao
    #cursor.execute(f'select "{column}" from steam_reviews')
    #numpy.std(cursor.fetchone())