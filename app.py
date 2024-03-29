# This flask app uses Machine learning to perform sentiment analysis on the movie reviews
# The model used is SVM. The webpage is scraped using beautiful soup

import os
import pickle
import re

import nltk
import pandas as pd
import requests
from bs4 import BeautifulSoup, SoupStrainer
# Importing libraries
from flask import Flask, render_template, request
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from urllib.parse import quote

nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')

# Data Cleaning
# Defining stop_words and lemmatizer
stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()


# Function to get reviews url from the movie name
def movie_name_to_reviews_url(movie_name):
    search_query = quote(movie_name)
    search_url = f"https://www.imdb.com/find?q={search_query}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }

    search_response = requests.get(search_url, headers=headers)
    search_soup = BeautifulSoup(search_response.content, "html.parser")
    a_tag = search_soup.find('a', class_='ipc-metadata-list-summary-item__t')

    movie_link = "https://www.imdb.com" + a_tag['href']
    movie_response = requests.get(movie_link, headers=headers)
    movie_soup = BeautifulSoup(movie_response.content, 'html.parser')
    reviews_section = movie_soup.find('section', {'cel_widget_id': 'StaticFeature_UserReviews'})
    if reviews_section:
        link_element = reviews_section.find('a', href=True)
        if link_element:
            reviews_url = "https://www.imdb.com" + link_element['href']
            return reviews_url

    return None


# Removing the html strips
def strip_html(text):
    soup = BeautifulSoup(text, "html.parser")
    return soup.get_text()


# Defining clean_text function
def clean_text(text):
    text = strip_html(text)
    text = re.sub(r'[^A-Za-z0-9]+', ' ', text)
    text = text.lower()
    text = [lemmatizer.lemmatize(token) for token in text.split(" ")]
    text = [lemmatizer.lemmatize(token, "v") for token in text]
    text = [word for word in text if not word in stop_words]
    text = " ".join(text)
    return text


# model_path = os.path.join(os.path.dirname(__file__), 'svmmodel.pkl')

# Loading the vectorizer
vect_pkl_file = "imdb_vect.pkl"
with open(vect_pkl_file, 'rb') as file:
    count_vect = pickle.load(file)

# Loading the model
model_pkl = "imdb_model.pkl"
with open(model_pkl, 'rb') as file:
    svm_from_joblib = pickle.load(file)

# # Loading the saved model using Joblib
# svm_from_joblib = joblib.load(model_path)


application = app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/analyze', methods=['POST'])
def analyze():
    try:
        print(request.form)

        # URL from the form
        # url = request.form['url']
        # print(f"url: {url}")

        # Manual URL for testing
        # url = 'https://www.imdb.com/title/tt9764362/reviews?ref_=tt_urv'

        # URL from Movie name
        movie_name = request.form['mname']
        print(f"movie name  : {movie_name}")
        url = movie_name_to_reviews_url(movie_name)
        print(f"url: {url}")

        webpage = requests.get(url)
        # Perform web scraping using BeautifulSoup
        soup = BeautifulSoup(webpage.content, "html.parser")

        # Get the review data using its class
        # Scrape the required data from the provided URL
        example_column = soup.find_all(attrs={"class": "text show-more__control"})
        example_list = []
        for x in example_column[1:]:
            example_list.append(x.get_text())

        # Converting the reviews list to dataframe
        page_df = pd.DataFrame(example_list, columns=["review"])

        # Creating new column for processed reviews
        page_df['Processed_Reviews'] = page_df.review.apply(lambda x2: clean_text(x2))

        # Vectorization and Bag of words method with default parameters
        bow_page = count_vect.transform(page_df['Processed_Reviews'].values.astype('U'))

        # Predicting the sentiment value of the reviews
        predicted_page = svm_from_joblib.predict(bow_page)

        # Calculate the results
        average_sentiment_score = predicted_page.mean()
        positive_count = sum(predicted_page)
        negative_count = len(predicted_page) - positive_count

        # Calculate the mean sentiment value from the predictions
        return render_template('result.html', sentiment_result=average_sentiment_score, positive_count=positive_count,
                               negative_count=negative_count, url=url)

    except Exception as e:
        # Log the exception for debugging purposes
        print(f"Exception occurred: {str(e)}")
        # Handle the exception gracefully by displaying an error message
        return render_template('error.html', error_message='An error occurred. Please try again later.')


if __name__ == '__main__':
    # app.run(debug=True)
    # app.run(host='0.0.0.0', port=5000)
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
