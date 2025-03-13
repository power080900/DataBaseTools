import pandas as pd
import matplotlib.pyplot as plt

match_csv = 'C:\\lee\\work\\Database\\code\\DB_Tools\\datasets\\SAI\\match.csv'
face_check_csv = 'C:\\lee\\work\\Database\\code\\DB_Tools\\datasets\\SAI\\face_check.csv'

match_df = pd.read_csv(match_csv)
face_check_df = pd.read_csv(face_check_csv)

plt.figure(figsize=(10, 5))
plt.pie(match_df['match'].value_counts(), labels=match_df['match'].value_counts().index, autopct='%1.1f%%')
plt.title('Match Check')
plt.savefig('match_check.png')
plt.close()

plt.figure(figsize=(10, 5))
plt.pie(face_check_df['point_cnt'].value_counts(), labels=face_check_df['point_cnt'].value_counts().index, autopct='%1.1f%%')
plt.title('Face Check')
plt.savefig('face_check.png')
plt.close()

