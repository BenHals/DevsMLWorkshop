#%%
import pathlib
import pandas as pd

input_file_path = pathlib.Path('trump_insult_tweets_2014_to_2021.csv')
output_file_path = pathlib.Path('trump_insult_tweets_2014_to_2021.txt')
df = pd.read_csv(file_path)
df.head()
# %%
tweets = df['tweet'].values
# %%
with output_file_path.open('w+') as f:
    for t in tweets:
        print(t, file=f)