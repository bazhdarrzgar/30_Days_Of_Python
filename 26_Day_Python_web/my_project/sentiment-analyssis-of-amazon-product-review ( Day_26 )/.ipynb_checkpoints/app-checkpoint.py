# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 21:49:27 2022

@author: 91960
"""

from bs4 import BeautifulSoup
# import urllib.request as url
import requests
import streamlit as st
import statistics as sts
import pickle
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# so we can see the output side by side
st.set_page_config(layout="wide")


# load model
def load_model():
    with open('model.pkl', 'rb') as file:
        model = pickle.load(file)
    return model


model = load_model()

# load tf_idf vectorizer
vectorizer = pickle.load(open('vectorizer.pkl', "rb"))


def get_soup(url):
    # url = url
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    return soup


reviewlist = []


# fetching only data which is necessary like rating title and content given by the customers
def get_reviews(soup):
    reviews = soup.find_all('div', {'data-hook': 'review'})
    try:
        for item in reviews:
            review = {
                'title': item.find('a', {'data-hook': 'review-title'}).text.strip(),
                'rating': float(
                    item.find('i', {'data-hook': 'review-star-rating'}).text.replace('out of 5 stars', '').strip()),
                'content': item.find('span', {'data-hook': 'review-body'}).text.strip(),
            }
            reviewlist.append(review)
    except:
        pass


# compare easier
st.title("AMAZON PRODUCT REVIEWS")
# col1,col2 = st.columns(2)
# with col1:
# url = input('URL link to scrape')
urls = st.text_input("enter the page url , you want to get the data")
# creating a loop from 1 to 100 reviews pages of the product
for x in range(1, 100):
    soup = get_soup(urls)
    get_reviews(soup)
    if not soup.find('li', {'class': 'a-disabled a-last'}):
        pass
    else:
        break

df = pd.DataFrame(reviewlist)
df['reviews'] = df['title'] + " " + df["content"]
df['reviews']

col1, col2 = st.columns(2)
with col1:
    st.subheader("PRODUCT SENTIMENT")
    ok = st.button("get sentiment")
if ok:
    test = vectorizer.transform(df['reviews'])
    prediction = model.predict(test)
    res = sts.mode(prediction)
    if res == 2:
        st.write("positive sentiment")
        # st.image(posit,caption='positive sentiment')
    elif res == 1:
        st.write("nutral sentiment")
    else:
        st.write("negative sentiment")

with col2:
    # for show the accurance of sentiments
    d = {'results': prediction}
    pred = pd.DataFrame(data=d)


    def lable(score):
        if score == 0:
            return 'Negative'
        elif score == 1:
            return 'Neutral'
        else:
            return 'Positive'


    pred['lable'] = pred['results'].apply(lable)


    def countplot():
        fig = plt.figure(figsize=(5, 5))
        sns.countplot(pred['lable'])
        st.pyplot(fig)


    st.subheader("COUNT THE SENTIMENTS")
    ok = st.button("Reviews countplot")
    if ok:
        countplot()
