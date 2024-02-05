import pandas as pd

# CSV 파일 읽기
df = pd.read_csv('example.csv')

# Excel 파일 쓰기
df.to_excel('example.xlsx', index=False)
