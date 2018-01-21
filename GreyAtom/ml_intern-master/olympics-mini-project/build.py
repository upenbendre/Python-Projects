import pandas as pd
import numpy as np

def load_data():
    df=pd.read_csv("olympics.csv", skiprows=1)
    df.index = [s.split("\xa0")[0] for s in df[df.columns[0]]]
    df.index.rename("Country_Name")
    cols = pd.MultiIndex(labels=[[0,0,0,0,0,1,1,1,1,1,2,2,2,2,2,3],[0,1,2,3,4,0,1,2,3,4,0,1,2,3,4,5]], 
                     levels=[['Summer', 'Winter','Combined','Country_Code'],['Games','Gold','Silver','Bronze','Total_Medals','']],
                     names=["Game_season", "Performance"])
    
    def getCountryCode(s):
        import re
        code = re.search(r'\([A-Z]{3,}\)',s)
        return ("" if type(code) == None.__class__ else code.group(0).lstrip("(").rstrip(")"))
    
    df["Country_Code"] = [getCountryCode(s) for s in df[df.columns[0]]]
    df.drop(df.columns[[0]], axis=1, inplace=True)
    df.drop('Totals', inplace=True)
    df.columns = cols
    df.drop(("Total_Medals"), level=1, axis=1, inplace=True)
    return(df)

def first_country(df):
    return(df.head(1))


def gold_medal(df):
    return(df["Summer"]["Gold"].argmax())


def biggest_difference_in_gold_medal(df):
    return(np.abs((df["Summer"]["Gold"] - df["Winter"]["Gold"]).astype(int)).argmax())

def get_points(df):
    return(df["Combined"]["Gold"]*3 + df["Combined"]["Silver"]*2 + df["Combined"]["Bronze"])

load_data()

