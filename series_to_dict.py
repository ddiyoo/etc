import pandas as pd

df1 = pd.read_csv('./jeju201906.csv', engine='python')
edit_df1 = df1.loc[(df1["ETC"] == "visit"),:]
df = []
df = pd.DataFrame(columns=['date','age','gender'])

for i in range(1,32):
    day = str(i).zfill(2)
    date=f'201906{day}'

    eidt_day = edit_df1[(edit_df1["STD_YMD"].astype('int')) == int(date)]
    age = eidt_day['AGE'].value_counts().to_dict()  ## series to dict
    gender = eidt_day['GENDER'].value_counts().to_dict()

    df = df.append(pd.DataFrame([[date, age, gender]], columns=['date', 'age', 'gender']))

df.to_csv('./umti.csv',header=True, index=False, encoding='euc-kr')


