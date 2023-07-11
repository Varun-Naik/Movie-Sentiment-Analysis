# Movie Sentiment Analyzer
 

Movie Sentiment Analyzer is a web application that utilizes machine learning to perform sentiment analysis on movie 
reviews. The app scrapes movie reviews from IMDb and uses a Support Vector Machine (SVM) model to predict the sentiment 
of the reviews. It provides valuable insights into the sentiments expressed by viewers towards a particular movie.

## Sentiment Analysis Application

This repository contains a sentiment analysis application that analyzes movie reviews. The application is deployed on Heroku and can be accessed at: [https://flaskml.herokuapp.com/](https://flaskml.herokuapp.com/).


## Features
* Scrapes movie reviews from IMDb using Beautiful Soup.
* Performs data cleaning and preprocessing on the reviews.
* Uses a pre-trained SVM model to predict the sentiment of the reviews.
* Calculates the average sentiment score, positive count, and negative count.
* Provides a user-friendly web interface to input movie names and analyze reviews.



## Technologies Used
* Python
* Flask
* BeautifulSoup
* scikit-learn
* Docker
* Heroku

## Model Development

The sentiment analysis model was trained using the IMDB dataset, which contains movie reviews labeled with positive or negative sentiment. The training process involved several steps, as outlined below.

1. Data Preprocessing:
   - The IMDB dataset was imported and the sentiment labels were converted to binary values, with 'positive' mapped to 1 and 'negative' mapped to 0.
   - Text cleaning techniques were applied to the reviews, including removing HTML tags, non-alphanumeric characters, and converting the text to lowercase.
   - Lemmatization was performed to reduce words to their base form, and stop words were removed.

2. Deploying SVM Model:
   - The scikit-learn library was utilized to implement a Support Vector Machine (SVM) model.
   - The dataset was split into training and testing sets using an 80:20 ratio.
   - The text data was transformed into numerical features using the Bag-of-Words (BoW) method with the CountVectorizer class.
   - An SVM model was instantiated and trained on the preprocessed training data.
   - Classification was performed on the testing data, and predictions were obtained.

Please note that the specific code details and the dataset itself are not included in this repository. However, the outlined steps provide a summary of the model training process and the techniques used for sentiment analysis.

## Flask App/Web Interface
This Flask app is deployed on a Heroku Server and also tested on AWS Elastic Beanstalk successfully. However currently 
only Heroku server is live. This was done by containerizing the app using Docker for easier deployment.

The Flask app does the following tasks:
1. Does the webscraping from the IMDb reviews page
2. Performs the sentiment analysis using the saved model trained earlier
3. Shows the results to the user with other metrics


## Code Structure
* `app.py`: This is the main Flask application file that handles routing, HTTP requests, and connects different components
of the application.
* `imdb_model.pkl`: This file represents the pre-trained SVM model used for sentiment analysis. 
* `imdb_vect.pkl`: This file represents the saved CountVectorizer object for transforming text data.



## Output Example

Upon analyzing a movie review, the application provides the following output on the result page:

![Output Example](/static/images/output%20example.jpeg)

The output consists of the following information:

- Sentiment Score: The sentiment score of the movie review, indicating the overall sentiment. This score is displayed as a progress bar, visually representing the sentiment score on a scale of 0 to 100.
- Positive Count: The count of positive sentiments detected in the movie review.
- Negative Count: The count of negative sentiments detected in the movie review.
- URL: A clickable URL that redirects to the original source of the movie review.

Additionally, a "Back" button is provided to return to the input page.




## License
This project is licensed under the MIT License.


## Acknowledgments
* The SVM model used for sentiment analysis is trained on IMDb movie reviews data.
* The web scraping is done using Beautiful Soup library.

## References

- [Sentiment Analysis on an IMDB Movie Review Dataset with a Support Vector Machines Model in Python](https://towardsdatascience.com/sentiment-analysis-on-a-imdb-movie-review-dataset-with-a-support-vector-machines-model-in-python-50c1d487327e) 




