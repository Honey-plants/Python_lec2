import pandas as pd

data = {
    '상품': ['노트북', '키보드', '마우스', '모니터', '헤드셋'],
    '매출': [1200, 150, 100, 800, 300],
    '판매수량' : [30, 200, 300, 50, 120]
}

frame1 = pd.DataFrame(data,
                      columns=['상품','매출','판매수량'])
print(frame1)
df =pd.DataFrame(data)

print('\n===매출 내림차순===')
print(df.sort_values(by='매출',ascending=False))

print('\n=== 판매수량 오림차순===')
print(df.sort_values(by='판매수량',ascending=True))

print('\n=== 인덱스 내림차순===')
print(df.sort_index(ascending=False))

print('\n=== 매출 Top 3===')
print(df.sort_values(by='매출',ascending=False).head(3))
