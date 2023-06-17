# Movie Sentiment Analyzer
 

Movie Sentiment Analyzer is a web application that utilizes machine learning to perform sentiment analysis on movie 
reviews. The app scrapes movie reviews from IMDb and uses a Support Vector Machine (SVM) model to predict the sentiment 
of the reviews. It provides valuable insights into the sentiments expressed by viewers towards a particular movie.

## Features
* Scrapes movie reviews from IMDb using Beautiful Soup.
* Performs data cleaning and preprocessing on the reviews.
* Uses a pre-trained SVM model to predict the sentiment of the reviews.
* Calculates the average sentiment score, positive count, and negative count.
* Provides a user-friendly web interface to input movie names and analyze reviews.


## Prerequisites
* Python 3.7 or higher /br
* Flask
* pandas
* requests
* nltk
* BeautifulSoup
* scikit-learn


## Local Deployment

To run the Flask app locally, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/Varun-Naik/Movie-Sentiment-Analysis.git
   cd Movie-Sentiment-Analysis
   ```
   
2. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```
   
3. Run the Flask app:

    ```bash
    python app.py
    ```
4. Open a web browser and visit http://localhost:5000 to access the application.


