from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification
import pandas as pd

model = AutoModelForSequenceClassification.from_pretrained("jarvisx17/japanese-sentiment-analysis")
tokenizer = AutoTokenizer.from_pretrained("jarvisx17/japanese-sentiment-analysis")

def predict_sentiment(text):
    nlp = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)
    result = nlp(text)
    return result

def find_closest_word(label, score):
    df = pd.read_csv("./static/csv/manga_np.csv", index_col=0, header=0)
    df_np = df.query("nega_posi == @label")
    differences = [abs(df_np.iloc[i,4]-score) for i in range(len(df_np))]
    closest_id = differences.index(min(differences))
    return df_np.iloc[closest_id]["セリフ"]
