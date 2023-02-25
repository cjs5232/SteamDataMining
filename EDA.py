import numpy
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
from datetime import datetime

warnings.filterwarnings("ignore")
from scipy.stats import ttest_ind, ttest_rel
from scipy import stats


# Run simple univariate analysis on columns with intergers
# Saves analysis to txt found in dataOut
def UnivariateAnalysis(data):
    f = open('dataOut/UnivariateAnalysis.txt', 'w')
    f.write(data.describe().to_string())
    f.close()


# Create Histograms for columns
# TO BE ADDED:
#   Save said hists to dataOUt as images with proper names
def showHists(data):
    data['votes_helpful'].hist()
    plt.show()

    data['votes_funny'].hist()
    plt.show()

    data['comment_count'].hist()
    plt.show()

    data['author.num_games_owned'].hist()
    plt.show()

    data['author.num_reviews'].hist()
    plt.show()

    data['author.playtime_forever'].hist()
    plt.show()

    data['author.playtime_last_two_weeks'].hist()
    plt.show()

    data['author.playtime_at_review'].hist()
    plt.show()


def cleanData(data):
    timestamps = data[["timestamp_created", "timestamp_updated"]]

    for x in range(0, 5000):
        created = timestamps.iloc[x][0]
        updated = timestamps.iloc[x][1]
        print(created)
        print(updated)
        createdDate = datetime.fromtimestamp(created).strftime("%A, %B %d, %Y %I:%M:%S")
        updatedDate = datetime.fromtimestamp(updated).strftime("%A, %B %d, %Y %I:%M:%S")



# Starts the EDA process by loading sample set into a pandas data frame
# Calls several helper methods for EDA
def startEDA(conn):
    cursor = conn.cursor()

    data = pd.read_sql('select * from sample', conn)
    data = data.drop("Index", axis='columns')
    data = data.drop("review_id", axis='columns')
    data = data.drop("author.steamid", axis='columns')

    # UnivariateAnalysis(data)
    # showHists(data)
    cleanData(data)
