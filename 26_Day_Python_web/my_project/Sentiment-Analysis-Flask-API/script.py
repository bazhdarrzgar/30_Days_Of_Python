from flask import Flask, render_template, abort, request, jsonify
import nltk
# we use this package (nltk) to use ( SentimentIntensityAnalyzer() ) function to analyse the word for possitive and negative
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# creating flask app for routing
app = Flask(__name__)

# all the output we get from function sentiment will store in this dictionary
output = {}

# create function sentiment for analyze the score of this word that we are sending to the function Sentiment intensity analyze
def sentiment(sentence):
    # create Setiment intensity analyzer that we use later
    sid = SentimentIntensityAnalyzer()
    # get the score of this word that we put to the    ?q=""    this quotes
    score = sid.polarity_scores(sentence)['compound']
    # if score of the word is greater than 0
    if(score>0):
        # returning Positive for the function sentiment
        return "Positive"
    else:
        # returning Positive for the function sentiment
        return "Negative"

# creating route method for Get data from user and also Post it for Sentiment intensity analyze
@app.route("/", methods = ["GET","POST"])
# create function request for sending the word to the Sentiment intensity analyzer
def request():
    # if my method is POST en
    if request.method == "POST":
        # get the input sentiment
        sentence = request.form["sentiment_input"]
        # put this sentiment to the function sentiment
        sentiment = sentiment(sentence)
        # get the output base on this sentiment
        output['sentiment'] = sentiment
        # in the end send json format for this output that we get
        return jsonify(output)
    
    else:
        # if the method is not POST means POST is not happen then
        # get the sentiment input
        sentence = request.args.get('sentiment_input')
        # sent this entiment to the funciton sentiment
        sentiment = sentiment(sentence)
        # print this sentiment for user
        print(sentiment)
        # send this sentiment for output 
        output['sentiment'] = sentiment
        # returing this output
        return {output}

# debuging mode is enable
app.run(debug=True)