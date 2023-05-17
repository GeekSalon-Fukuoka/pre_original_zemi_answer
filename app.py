from flask import Flask,render_template, request
from model import predict_sentiment, find_closest_word


app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/predict", methods =['GET', 'POST'])
def predict():
    if request.method == 'GET':
        return render_template('predict.html')
    elif request.method == 'POST':
        quote = request.form['name']
        result = predict_sentiment(quote)
        label = result[0]['label']
        score = round(result[0]['score'], 2)
        closestWord = find_closest_word(result[0]['label'], result[0]['score'])
        return render_template('predict.html',quote=quote, label=label, score=score, closestWord=closestWord)


if __name__ == "__main__":
    app.run(debug=True)

