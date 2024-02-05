import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'San Francisco', 'Los Angeles']}
df = pd.DataFrame(data)

# 열 선택
#print(df['Name'])

# 행 선택
#print(df.loc[0])

# 조건에 따른 데이터 선택
#print(df[df['Age'] > 30])

# 열 추가
df['Salary'] = [50000, 60000, 70000]

print(df)