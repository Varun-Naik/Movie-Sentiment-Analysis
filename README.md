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
* Python 3.7 or higher 
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



## Docker Deployment

To deploy the Flask app using Docker, follow these steps:

1. Install Docker on your machine.

2. Build the Docker image:

    ``` bash
    docker build --tag flask-sentiment .
    ```

3. Run the Docker container:

    ```bash
    docker run -d -p 5000:5000 flask-sentiment
    ```

4. Open a web browser and visit http://localhost:5000 to access the application.

5. Rename the image according to the Docker hub repository

    ```
    docker tag flask-sentiment:latest varunnaik29/flaskai:v2.0
    ```



6. Push the image to Docker Hub
    ``` bash
    docker push varunnaik29/flaskai:v2.0
    ```



## Heroku Deployment

To deploy the Flask app on Heroku, follow these steps:

1. Create a Heroku account if you don't have one.

2. Install the Heroku CLI and log in to your Heroku account:

    ```
    heroku login
    ```
3. Log in to the container registry:
    ```
    heroku container:login
    ```

4. Create a new Heroku app:

    ```bash
    heroku create flaskml
    ```

5. Push the Docker image to your app:
    ```
    heroku container:push web --app flaskml
    ```

6. Release the app to deploy it:
    ```
    heroku container:release web --app flasksentiment
    ```

7. Open a web browser and visit https://flaskml.herokuapp.com/ in this case to access the application or use CLI:
    ```
    heroku open -a flaskml
    ```


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


