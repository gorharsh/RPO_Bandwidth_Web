import pandas
df1 = pandas.read_csv("data.csv")
df1['change_gb'] = df1['capacity'] * df1['change']
df1['bw'] = (df1['change_gb']*8*1000) / (df1['rpo']*60)
df1['fr'] = (df1['capacity']*8*1000)/ df1['bw']
df1['dd'] = pandas.to_timedelta(df1['fr'], unit='s')
df1.to_csv('data_out.csv', encoding='utf-8',index=False)