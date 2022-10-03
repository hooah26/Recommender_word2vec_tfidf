import pandas as pd
import glob
data_paths = glob.glob('./review_datas/*')
df = pd.DataFrame()

# for path in data_paths:
#     path = glob.glob(path+'/')
for i in data_paths:
    df_temp = pd.read_csv(i)
    df_temp['product']=i[22:-4]
    df = pd.concat([df, df_temp], ignore_index=True, axis='rows')
df.dropna(inplace=True)
print(df.head())
df.info()
df.to_csv('./crawling_data/crawling_data.csv', index=False)