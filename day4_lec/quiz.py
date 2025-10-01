import pandas as pd
df_students = pd.DataFrame({
    "학번":[101, 102, 103],
    "이름":["철수", "영희", "민수"],
    "학년":[1,2,1]
})

df_enroll = pd.DataFrame({
    "학번":[101, 101, 102, 103, 103],
    "과목코드": [ "m101", "E101", "m101","s101", "e101"]
})

df_courses = pd.DataFrame({
    "과목코드":["M101", "E101", "S101"],
    "과목명":["수학","영어","과학"],
    "교수": ["김교수", "이교수", "박교수"]
})



df1= pd.merge(df_students, df_enroll, on='학번', how="inner")

df_final = pd.merge(df1, df_courses, on="과목코드", how="outer")
print(df_final)
df_final["수강과목수"] = df_final["학번"].map(df_final["학번"].value_counts())

print(df_final)