import seaborn as sns
import getpass
import matplotlib.pyplot as plt
import mysql.connector 
import pandas as pd
import numpy as np

class SQL():
    def __init__(self):
        user = input('user: ')
        password = getpass.getpass('password: ')
        host = input('host: ')
        port = input('port: ')
        database = input('database: ')
        config = {
            'user': user,
            'password': password,
            'host': host,
            'port': port,
            'database': database,
            'raise_on_warnings': True,
            }
        self.config = config      
    
    def create_table(self,query):
        db = mysql.connector.connect(**self.config)
        conn = db.cursor()
        conn.execute(query)
        db.commit()
        conn.close()
        db.close()
        print('create table done')

    def insert_dataset_values(self,query,value_list):
        db = mysql.connector.connect(**self.config)
        conn = db.cursor()
        print(value_list[0])
        conn.executemany(query,value_list)
        db.commit()
        print(f'insert {len(value_list)} done')

    def search_SQL(self,dataset):
        db = mysql.connector.connect(**self.config)
        conn = db.cursor()
        conn.execute(f'''
            SELECT * FROM DeepInSight.{dataset}_info;''')
        result = conn.fetchall()
        conn.close()
        db.close()

        return pd.DataFrame(result)

# 시각화 함수
class visualization():
    def draw_jointplot(dataset, xlabel, ylabel, save_name, xlim, ylim, unit='degree', reverse=False):
        plt.figure(figsize=(16, 12))
        sns.jointplot(x=xlabel, y=ylabel, data=dataset, kind='kde', cmap='RdYlGn')
        plt.xlabel(f'{xlabel}_{unit}', fontsize=20)
        plt.ylabel(f'{ylabel}_{unit}', fontsize=20)
        plt.xlim(-xlim, xlim)
        plt.ylim(-ylim, ylim)
        if reverse == True: 
            plt.gca().invert_yaxis()
        plt.savefig(save_name)
        print('save',save_name)

    def plot_bar(data, col, xlabel, ylabel, title, filename, rotation=0):
        plt.figure(figsize=(8, 5))
        plt.bar(data.index.astype(str), data.values, color='skyblue')
        plt.xticks(rotation=rotation)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(title)
        plt.grid(True)
        for i, count in enumerate(data.values):
            plt.text(i, count, count, ha='center', va='bottom')
        plt.savefig(filename)
        plt.close()

    def plot_barh(data, col, xlabel, ylabel, title, filename, rotation=30):
        plt.figure(figsize=(12, 10))
        plt.barh(data.index.astype(str), data.values, color='skyblue')
        plt.gca().invert_yaxis()
        plt.yticks(rotation=rotation)
        plt.subplots_adjust(left=0.2)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(title)
        plt.grid(True)
        for i, count in enumerate(data.values):
            plt.text(count, i, count, ha='left', va='center')
        plt.savefig(filename)
        plt.close()

    # 히트맵 함수
    def plot_heatmap(df, x, y, xlabel, ylabel, title, filename):
        plt.figure(figsize=(8, 5))
        heatmap = pd.crosstab(df[x], df[y])
        sns.heatmap(heatmap, cmap='Blues', annot=True, fmt='d')
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(title)
        plt.gca().invert_yaxis()
        plt.savefig(filename)
        plt.close()

    def multi_plot_bar(data,cols, xlabel, ylabel, title, filename, rotation=0):
        # label_id와 label_name으로 그룹화하여 개수 세기
        grouped = data.groupby(cols).size().unstack(fill_value=0)
        
        # 막대 너비와 위치 설정
        num_cols = len(grouped.columns)
        x = np.arange(len(grouped))  # 레이블 위치
        width = 0.8 / num_cols  # 막대 너비

        plt.figure(figsize=(12, 7))

        for i, col in enumerate(grouped.columns):
            plt.bar(x + i * width, grouped[col], width, label=col)

    # print(rotation)

        plt.xticks(x + width * (num_cols - 1) / 2, grouped.index.astype(str), rotation=rotation)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(title)
        plt.legend()
        plt.grid(True, axis='y')

        for i in range(len(grouped)):
            for j, col in enumerate(grouped.columns):
                plt.text(i + j * width, grouped[col].iloc[i], grouped[col].iloc[i], ha='center', va='bottom')

        plt.savefig(filename)
        plt.close()

    def plot_pie(data, col, title, filename):
        plt.figure(figsize=(8, 5))
        plt.pie(data, labels=data.index, autopct='%1.1f%%', startangle=90, labeldistance=1.1, pctdistance=0.85)
        plt.title(title)
        plt.axis('equal')
        plt.savefig(filename)
        plt.close()