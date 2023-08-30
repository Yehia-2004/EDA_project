import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns
import plotly.express as px
import re
import sqlite3

def read_data():
    while True:
        filepath = input("Enter file path you wanna analyze: ")

        if bool(re.search(r".csv",filepath)) == True:
            try:
                df = pd.read_csv(filepath)
            except OSError:
                print("You write a wrong file path, please try again")
                continue

        elif bool(re.search(r".xls",filepath)) == True:
            try:
                df = pd.read_csv(filepath)
            except OSError:
                print("You write a wrong file path, please try again")
                continue
    
        elif bool(re.search(r".db",filepath)) == True:
            conn = sqlite3.connect(filepath)
            try:
                df = pd.read_sql(sql=f"SELECT * FROM {filepath}", con=conn)
            except OSError:
                print("You write a wrong file path, please try again")
                continue

        else:
            print("The file path you entered is wrong, please try again")
            continue

        break
    
    return df

def explore_data(df):
    while True:
        explore = input("If you want the data's first five rows press 'h': \nIf you want the data's last five rows press 't': \nIf you want the data's shape press 's': \nIf you want the data's info press 'i': \nIf you want the data's describe press 'd':\nIf you wanna know how many null values in each column write 'n': \n")
        if explore.lower() == 's':
            print(str(df.shape) + '\n')

        elif explore.lower() == 'i':
            print(str(df.info()) + '\n')

        elif explore.lower() == 't':
            print(str(df.head()) + '\n')

        elif explore.lower() == 'h':
            print(str(df.tail()) + '\n')
        
        elif explore.lower() == 'd':
            print(str(df.describe()) + '\n')

        elif explore.lower() == 'n':
            print(str(df.isnull().sum()) + '\n')

        y = input("If you wanna continue exploring the data press y, but if not press x: ")

        if y.lower() == 'y': continue
        elif y.lower() == 'x': break
        else: continue
    return df

def clean_data(df):
 while True:
    clean = input("If you wanna clean null values by drop them write 'drop'\nIf you wanna clean null values by fill by mean of the column write 'mean'\nIf you wanna clean null values by fill by median of the column write 'median'\nIf you wanna clean null values by fill by mode of the column write 'mode'\nIf you wanna drop any column write 'dropc'\n")
    
    if clean.lower() == "drop":
        df = df.dropna()
        print(str(df.isnull().sum()) + "\n" + str(df.shape))

    elif clean.lower() == "mean":
        df = df.fillna(df.mean())
        print(str(df.isnull().sum()) + "\n" + str(df.shape))

    elif clean.lower() == "median":
        df = df.fillna(df.median())
        print(str(df.isnull().sum()) + "\n" + str(df.shape))

    elif clean.lower() == "mode":
        df = df.fillna(df.mode())
        print(str(df.isnull().sum()) + "\n" + str(df.shape))

    elif clean.lower() == "dropc":
        column = input("Please Enter column's name that you wanna drop: ")
        try:
            df = df.drop(column,axis = 1)
        except KeyError:
            print(f"{column} is not found in the axis, please try again")
            continue
        print(str(df.columns) + str(df.head()) + "\n" + str(df.shape))

    y = input("If you wanna continue cleaning the data press y, but if not press x: ")

    if y.lower() == 'y': 
        continue
    elif y.lower() == 'x': 
        break
    else: continue
 return df

def visualize_data(df):
    while True:
        visualize = input("If you wanna see bar chart write 'bar'\nIf you wanna see histogram chart write 'hist'\nIf you wanna see scatter chart write 'scat'\nIf you wanna see pie chart write 'pie'\nIf you wanna see boxplot chart write 'box'\nIf you wanna see violinplot chart write 'vio'\n")
    
        if visualize.lower() == "bar":
            column1 = input("Enter the x-axis column's name: ")
            column2 = input("Enter the y-axis column's name: ")

            try:
                sns.barplot(x=column1,y=column2,data=df)
                plt.show()
            except ValueError:
                print("There is at least column's name not found in your dataset, please try again")
                continue

        elif visualize.lower() == "hist":
            column = input("Enter the column's name: ")

            try:
                sns.histplot(x=column,data=df)
                plt.show()
            except ValueError:
                print("There is at least column's name not found in your dataset, please try again")
                continue

        elif visualize.lower() == "scat":
            column1 = input("Enter the x-axis column's name: ")
            column2 = input("Enter the y-axis column's name: ")

            try:
                sns.scatterplot(x=column1,y=column2,data=df)
                plt.show()
            except ValueError:
                print("There is at least column's name not found in your dataset, please try again")
                continue

        elif visualize.lower() == "pie":
            values = input("Enter column's name: ")
            counts = df[values].value_counts()

            try:
                show = px.pie(counts,values=counts.values, names=counts.index)
                show.show()
            except ValueError:
                print("There is at least column's name not found in your dataset, please try again")
                continue

        elif visualize.lower() == "box":
            column = input("Enter the column's name: ")

            try:
                sns.boxplot(df[column])
                plt.show()
            except ValueError:
                print("There is at least column's name not found in your dataset, please try again")
                continue
        elif visualize.lower() == "vio":
            column = input("Enter the column's name: ")

            try:
                sns.violinplot(df[column])
                plt.show()
            except ValueError:
                print("There is at least column's name not found in your dataset, please try again")
                continue

        else: continue

        y = input("If you wanna continue visualizing data press y, but if not press x: ")

        if y.lower() == 'y': continue
        elif y.lower() == 'x': break
        else: continue


while True:
    df = read_data()
    while True:
        analyze = input("If you wanna explore data press 'e':\nIf you wanna clean data press 'c':\nIf you wanna visualize data press 'v':\n")

        if analyze.lower() == 'e': 
            df = explore_data(df)
    
        elif analyze.lower() == 'c':
            df = clean_data(df)
        
        elif analyze == 'v':
            df = visualize_data(df)
        
        y = input("If you wanna do another thing in this file press y, if not press x:  \n")
        if y.lower() == 'y': continue
        elif y.lower() == 'x': break
        else: continue
    
    z = input("If you wanna save the changes press y, if not press any button: ")
    if z.lower() == 'y':
        new_file = input("Enter the new file name you want: ")
        df.to_csv(f'{new_file}.csv', index=False)
    
    y = input("If you wanna analyze another file press y, if not press x: ")
    if y.lower() == 'y': continue
    elif y.lower() == 'x': break
    else: continue