import pandas as pd
import pickle

X = pickle.load(open("input/breast_cancerX", "rb"))
Y = pickle.load(open("input/breast_cancerY", "rb"))

def analyze_outlier(df):
    sorted_df = df.sort_values(by=['OF'], ascending=False)
    first30 = sorted_df.head(30)
    first30_Y = first30['Y'].tolist()
    first30_0count = first30_Y.count(0)
    first30_accuracy = (first30_0count / 30) * 100
    
    print ("Within the top 30 ranked cases (ranked according to the Outlier Factor), {} of the malignant cases (the outliers), comprising {}% of all malignant cases, were identified.".format(first30_0count, first30_accuracy))