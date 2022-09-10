# Sentiment Analysis Flask API
 
* returning the positive or negative message base on this text that you take to the server


## Requirements

1. **Flask==1.1.1**

2. **nltk==3.4.5**


```shell

pip install -r requirement.txt

```

## Running

```shell

# 1. run with flask

false run

# 2. run with python 

python3 app.py

# 3. if you are ide just go to the app.py file and you see button to run the main and run it 

```

## Usage

Using GET method - 

    http://127.0.0.1:5000?q="Text String to check Sentiment."
Using POST method - 

    curl http://127.0.0.1:5000 -d "q='Text String to check Sentiment.'"


## Output

Output is JSON based which is as follows -

    {"sentiment":"Negative"}
or

    {"sentiment":"Positive"}
