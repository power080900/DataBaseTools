import mysql.connector
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


config = {
    'user': 'diadmin',
    'password': 'Dinsight0625!',
    'host': '192.168.0.128',
    'port': '3306',
    'database': 'DeepInSight',
    'raise_on_warnings': True,
}

db = mysql.connector.connect(**config)
conn = db.cursor()

conn.execute('''
    SELECT * FROM DeepInSight.Gaze360_normalized_gaze_info;''')
result = conn.fetchall()

df = pd.DataFrame(result)

df.columns = ['id','img_dir', 'img_format', 'img_width', 'img_height', 'color_space', 'label_dir', 'label_format', 'x_3d', 'y_3d', 'z_3d', 'yaw_2d', 'pitch_2d', 'pitch_degrees', 'yaw_degrees', 'project_id']
df1 = df.drop(['id','img_dir', 'img_format', 'img_width', 'img_height', 'color_space', 'label_dir', 'label_format', 'x_3d', 'y_3d', 'z_3d', 'yaw_2d', 'pitch_2d', 'project_id'], axis=1)
df2 = df.drop(['id','img_dir', 'img_format', 'img_width', 'img_height', 'color_space', 'label_dir', 'label_format', 'x_3d', 'y_3d', 'z_3d', 'pitch_degrees', 'yaw_degrees', 'project_id'], axis = 1)
df3 = df.drop(['id','img_dir', 'img_format', 'img_width', 'img_height', 'color_space', 'label_dir', 'label_format', 'yaw_2d', 'pitch_2d', 'pitch_degrees', 'yaw_degrees', 'project_id'], axis = 1)

cor_df1 = df1.corr()
cor_df2 = df2.corr()
cor_df3 = df3.corr()

sns.jointplot(x='yaw_degrees', y='pitch_degrees', data=df, kind='reg')
# plt.show()
# sns.jointplot(x='yaw_2d', y='pitch_2d', data=df, kind='reg')
# plt.show()
sns.jointplot(x='x_3d', y='y_3d', data=df, kind='reg')
# plt.show()
sns.jointplot(x='x_3d', y='z_3d', data=df, kind='reg')
# plt.show()
sns.jointplot(x='y_3d', y='z_3d', data=df, kind='reg')
plt.show()