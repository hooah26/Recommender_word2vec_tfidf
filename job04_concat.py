import pandas as pd
import glob
data_paths = glob.glob('./reviews_datas/*')
print(data_paths)
df = pd.DataFrame()
for path in data_paths:
    df = pd.read_csv(path)
    df.columns=['reviews_data']
    df['product'] = path[30:-4]
    df = pd.concat([df], ignore_index=True, axis='rows')
df.info()
df.to_csv('./crawling_data/crawling_data.csv', index=False)