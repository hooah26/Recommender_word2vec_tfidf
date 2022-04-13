import pandas as pd

df = pd.read_csv('./crawling_data/cleaned_review_data2.csv')
print(df.head())
print(df.duplicated().sum())

df.drop_duplicates(inplace=True)
df.dropna(inplace=True)
df.info()

one_sentences = []
for product in df['product'].unique():
    temp = df[df['product'] == product]
    temp = temp['cleaned_sentences']
    one_sentence = ' '.join(temp)
    one_sentences.append(one_sentence)
df_one_sentences = pd.DataFrame(
    {'product':df['product'].unique(), 'cleaned_sentences':one_sentences})
print(df_one_sentences.head())
df_one_sentences.to_csv('./crawling_data/onesentence.csv', index=False)














