#%%
import pathlib
import pandas as pd

input_file_path = pathlib.Path('topical_chat.csv')
all_output_file_path = pathlib.Path('all_topical_chat.txt')
curious_output_file_path = pathlib.Path('curious_topical_chat.txt')
happy_output_file_path = pathlib.Path('happy_topical_chat.txt')
neutral_output_file_path = pathlib.Path('neutral_topical_chat.txt')
surprised_output_file_path = pathlib.Path('surprised_topical_chat.txt')
disgusted_output_file_path = pathlib.Path('disgusted_topical_chat.txt')
sad_output_file_path = pathlib.Path('sad_topical_chat.txt')
fearful_output_file_path = pathlib.Path('fearful_topical_chat.txt')
angry_output_file_path = pathlib.Path('angry_topical_chat.txt')
df = pd.read_csv(input_file_path)
df.head()
#%%
df['sentiment'].unique()
# %%
all_messages = df['message'].values
curious_messages = df[df['sentiment'] == "Curious to dive deeper"]['message'].values
happy_messages = df[df['sentiment'] == " Happy"]['message'].values
neutral_messages = df[df['sentiment'] == " Neutral"]['message'].values
surprised_messages = df[df['sentiment'] == " Surprised"]['message'].values
disgusted_messages = df[df['sentiment'] == " Disgusted"]['message'].values
sad_messages = df[df['sentiment'] == " Sad"]['message'].values
fearful_messages = df[df['sentiment'] == " Fearful"]['message'].values
angry_messages = df[df['sentiment'] == " Angry"]['message'].values
# %%
with output_file_path.open('w+', encoding='utf-8') as f:
    for t in all_messages:
        print(t, file=f)
with curious_output_file_path.open('w+', encoding='utf-8') as f:
    for t in curious_messages:
        print(t, file=f)
with happy_output_file_path.open('w+', encoding='utf-8') as f:
    for t in happy_messages:
        print(t, file=f)
with neutral_output_file_path.open('w+', encoding='utf-8') as f:
    for t in neutral_messages:
        print(t, file=f)
with surprised_output_file_path.open('w+', encoding='utf-8') as f:
    for t in surprised_messages:
        print(t, file=f)
with disgusted_output_file_path.open('w+', encoding='utf-8') as f:
    for t in disgusted_messages:
        print(t, file=f)
with sad_output_file_path.open('w+', encoding='utf-8') as f:
    for t in sad_messages:
        print(t, file=f)
with fearful_output_file_path.open('w+', encoding='utf-8') as f:
    for t in fearful_messages:
        print(t, file=f)
with angry_output_file_path.open('w+', encoding='utf-8') as f:
    for t in angry_messages:
        print(t, file=f)
# %%

# %%

# %%
