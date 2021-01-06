# Hybrid Recommendation Engine
Developed a hybrid recommendation engine for movie recommendations. 

# Model
-Designed and developed a hybrid recommendation engine using Collaborative filtering, Sentiment Analysis and Content Based filtering.

## Collaborative Filtering
-Collaborative filtering systems recommend movies based on similarity measures between users and/or items.
-Correction for movie bias and Correction for user bias is also included.
-Predicted ratings based on matrix factorization techniques such as SVD and NMF. To add the weightage of bias based on user preferences and items, we also did user based and item based collaborative filtering through KNN classification. Using the movies plot and genres provided in the data, a movie similarity matrix was created. Using the similarity of the user profile and movie-movie similarity matrix, we obtain the predictions for different users.

## Sentiment Analysis of Reviews
Implemented is we analyzed the sentiment of user reviews and generate a new rating based on this sentiment. 


## Content Based Filtering
-Description and category from Supplemental metadata are combined into a single text plot.
-Resulting text is cleaned by removing punctuation, articles and other unnecessary data.
-For each movie, an important bag of words is extracted.
-Movie / Word matrix is vectorized using nltk.countvector
package.
<b>NOTE:</b> Countvector is used instead of TF-iDF since TF-iDF
performs poorly when used on movie plots which have
frequently occuring information like genre.
-Similarity matrix is calculated using cosine similarity from the vectorized Movie / Important Word matrix. This will give us information about the word /importance relevance to a movie.

-Weighted average scores are calculated for movies watched and rated by the user and this information is used to calculate individual scores for movies user hasn’t watched. 
-<b>Cold Start</b>To calculate Cold Start movie score, movies are given average
ratings.



# Dataset
The data set that is being considered is Amazon small, 5-core Movies and TV review data ( 1.7m records) set from Julian McAuley’s
(UCSD)(data page ) site provided as a part of the assignment. 5-core implies each user and movie has at least 5 reviews. This is a json
tuple with following fields in table 1: data set titles
<p align="center">
    <img src="readmeImages/json_format_for_recsys .png">
</p>
Link: https://nijianmo.github.io/amazon/index.html


# Evalution Metrics
Quality of recommendation list is validated by comparing the results against rating data in test set using the following 
measures:
 Precision: Average for all users of % of testing items in recommendation list for each user. Precision gives the proportion of recommended items that are relevant.
 Recall: Average for all users of % of items in recommendation list in all testing items for each user. Recall gives the proportion of relevant items.
 F-measure: F=2*Precision*Recall / (Precision + Recall). The F score can provide a more realistic measure of a test’s performance by using both precision and recall.
 NDCG: Normalized Discounted Cumulative Gain. This is another metric which measures the quality of the ranking of the predictions.

# Tools
For the implementation part we have used surprise package which is a python scikit library for building and analyzing the performance of our hybrid recommender system. To perform sentiment analysis of the reviews we have used Natural Language Toolkit (NLTK) a NLP library in python.

# Contributions:
ashshetty-prog, Sreeram Maddineni, Krishnamurthy Subramanian



