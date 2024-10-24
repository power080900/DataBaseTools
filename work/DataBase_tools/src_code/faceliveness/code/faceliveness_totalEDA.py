import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df1 = pd.read_csv('celeb_A_spoof.csv')
df2 = pd.read_csv('robo_anti_spoof.csv')

df = pd.concat([df1, df2])

# attack_type별로 count를 계산하고 정렬
df_attack = df.value_counts('attack_type').sort_values(ascending=False).reset_index()
df_attack.columns = ['attack_type', 'count']

# 그래프 크기 설정
plt.figure(figsize=(13, 13))

# barplot 생성
sns.barplot(x='count', y='attack_type', data=df_attack, color='skyblue')

# 각 막대 위에 빈도 값 표시
for index, value in enumerate(df_attack['count']):
    plt.text(value, index, str(value), va='center')

# 축 및 제목 설정
plt.xlabel('Count')
plt.ylabel('Attack Type')
plt.title('Spoof Attack Type')

# 그래프 저장 및 출력
plt.savefig('spoof_attack_type.png')
plt.show()

df_light = df.value_counts('light_type').sort_values(ascending=False).reset_index()
df_light.columns = ['light_type', 'count']

plt.figure(figsize=(13, 13))
sns.barplot(x='count', y='light_type', data=df_light, color='skyblue')

for index, value in enumerate(df_light['count']):
    plt.text(value, index, str(value), va='center')

plt.xlabel('Count')
plt.ylabel('Light Type')
plt.title('Light Type')

plt.savefig('light_type.png')
plt.show()

df_env = df.value_counts('Environment_type').sort_values(ascending=False).reset_index()
df_env.columns = ['Environment_type', 'count']

plt.figure(figsize=(13, 13))
sns.barplot(x='count', y='Environment_type', data=df_env, color='skyblue')

for index, value in enumerate(df_env['count']):
    plt.text(value, index, str(value), va='center')

plt.xlabel('Count')
plt.ylabel('Environment Type')
plt.title('Environment Type')

plt.savefig('Environment_type.png')
plt.show()

