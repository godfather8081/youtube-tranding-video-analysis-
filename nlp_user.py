from textblob import TextBlob
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sys

non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)

#df_usa=pd.read_csv(r"C:\Users\god-father\Desktop\INvideos.csv")

df_usa=input("Enter Text here:: ")

df_usa=df_usa.split(".")
print(df_usa)

#print(len(df_usa))

bloblist_desc = list()

df_usa_descr_str=df_usa

for row in df_usa_descr_str:
    if(row!=non_bmp_map):
        blob = TextBlob(row)
        bloblist_desc.append((row,blob.sentiment.polarity, blob.sentiment.subjectivity))
        df_usa_polarity_desc = pd.DataFrame(bloblist_desc, columns = ['sentence','sentiment','polarity'])
 
def f(df_usa_polarity_desc):
    if df_usa_polarity_desc['sentiment'] > 0:
        val = "Positive"

        try:
            if(df_usa_polarity_desc['sentence']!=non_bmp_map):
                print(str(df_usa_polarity_desc)+val+'\n')
        except:
            print(".")
            
    elif df_usa_polarity_desc['sentiment'] == 0:
        val = "Neutral"
        
        try:
            if(df_usa_polarity_desc['sentence']!=non_bmp_map):
                print(str(df_usa_polarity_desc)+val+'\n')
        except:
            print(".")
    else:
        val = "Negative"
        
        try:
            if(df_usa_polarity_desc['sentence']!=non_bmp_map):
                print(str(df_usa_polarity_desc)+val+'\n')
        except:
            print(".")
            
    return val

df_usa_polarity_desc['Sentiment_Type'] = df_usa_polarity_desc.apply(f, axis=1)


plt.figure(figsize=(10,10))
sns.set_style("whitegrid")
ax = sns.countplot(x="Sentiment_Type", data=df_usa_polarity_desc)
plt.show()
