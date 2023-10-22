## Title: Stock News Headlines Sentiment Analysis

### A. Project Overview:
This project focused on analyzing the sentiment of stock news headlines to predict whether the stock price would go up or down.

### B. Dataset Description: 
The dataset contained 27 columns of information related to stock news headlines.
We will be using the following dataset:

      Stock_Headlines.csv
-----

## -Tasks Performed:

### 1. Data Preprocessing:
* Performed Exploratory Data Analysis (EDA) on the dataset to addressnull values as needed.
* Utilized NLTK (Natural Language Toolkit) for text preprocessing.
* Employed NLTK's stopwords to remove common words that don't carry significant meaning.
* Applied the Porter Stemmer algorithm to reduce words to their root form, enhancing text analysis efficiency.
* Tokenized the text, removed stopwords, stemmed the words, and reassembled them into a final corpus of news titles.

### 2. Model Implementation:
* Implemented Logistic Regression, Support Vector Machine (SVM), Decision Tree, Random Forest, Gaussian Naive Bayes, Bernoulli Naive Bayes, Multinomial Naive Bayes Algorithm using appropriate libraries.

### 3. Visualization:
* Created word clouds for both up_words and down_words to visually represent the most frequent words in positive and negative news headlines.

### 4. Feature Representation:
* Built a Bag-of-Words (BoW) model using the CountVectorizer, transforming the text data into numerical features for machine learning.

### 5. Model Evaluation:
Evaluated model performance using the following metrics:
 * **Accuracy Score:** To assess the overall accuracy of the predictions
 * **Precision:** To measure the proportion of true positive predictions out of all positive predictions.
 * **Recall:** To evaluate the proportion of true positives correctly identified.
 * Created and visualized **Confusion Matrices** to gain insights into model performance.

### 6. Deployment:
* Deployed a web application using **Flask** to provide an interface for users to input news headlines and receive stock sentiment predictions.

### 7. Final Prediction:
* Employed a **Decision Tree** model to make the final predictions. This model demonstrated an impressive Accuracy of **85.44%**

---

## Final Screenshots

- ***Home Page***

![App Screenshot](https://github.com/abhishekdeshmukh001/Stock-News-Headlines-Sentiment-Analysis/blob/main/HomePage.png?raw=true)

- ***Enter the News***

![App Screenshot](https://github.com/abhishekdeshmukh001/Stock-News-Headlines-Sentiment-Analysis/blob/main/Type_Input.png?raw=true)

- ***Predicted Output***

![App Screenshot](https://github.com/abhishekdeshmukh001/Stock-News-Headlines-Sentiment-Analysis/blob/main/Predicted_Output.png?raw=true)


## 🔗 Link
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/abhishek-sachin-deshmukh/)


## Authors

- [@abhishekdeshmukh001](https://github.com/abhishekdeshmukh001)
