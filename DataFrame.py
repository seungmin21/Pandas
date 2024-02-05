import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'San Francisco', 'Los Angeles']}
df = pd.DataFrame(data)

df1 = pd.DataFrame({'ID': [1, 2, 3], 'Name': ['Alice', 'Bob', 'Charlie']})
df2 = pd.DataFrame({'ID': [2, 3, 4], 'Salary': [60000, 70000, 80000]})
merged_df = pd.merge(df1, df2, on='ID')

#numeric_columns = df.select_dtypes(include=['number']).columns
#grouped = df.groupby('Age')[numeric_columns].mean()

# 문자열 데이터에 대해서는 최빈값 계산
non_numeric_columns = df.select_dtypes(exclude=['number']).columns
grouped = df.groupby('Age')[non_numeric_columns].agg(lambda x: x.mode().iloc[0] if not x.mode().empty else None)

# 열 선택
#print(df['Name'])

# 행 선택
#print(df.loc[0])

# 조건에 따른 데이터 선택
#print(df[df['Age'] > 30])

# 열 추가
df['Salary'] = [50000, 60000, 70000]

# 열 삭제
df = df.drop('City', axis=1)

# 데이터 정렬
df = df.sort_values(by='Age')

#print(df)
print(grouped)