from flask import Flask, render_template, request
from model import predict_sentiment, find_closest_word


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/predict", methods=["GET", "POST"])
def predict():
    if request.method == "GET":
        return render_template("predict.html")
    elif request.method == "POST":
        quote = request.form["name"]
        result = predict_sentiment(quote)
        label = result[0]["label"]
        score = round(result[0]["score"], 3)
        closest_word = find_closest_word(result[0]["label"], result[0]["score"])
        return render_template(
            "predict.html",
            quote=quote,
            label=label,
            score=score,
            closest_word=closest_word,
        )


if __name__ == "__main__":
    app.run(debug=True)
