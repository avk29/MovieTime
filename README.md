# MovieTime
MovieTime is a **Content-Based Movie Recommender System** that works on the principles on **Unsupervised Machine Learning.**  
- <a href="https://movietime-avk.herokuapp.com">MovieTime (Website Link)</a>

## About The Project

Data of 5000 movies from two separate datasets is **preprocessed** (this also includes **stemming** of text data) and **EDA** is performed. Next, a **Bag of Words NLP model** is used to **vectorize** the text input. 

The model then uses **cosine similarity** to offer **recommendations**. It calculates the **cosine similarities** of a given movie with all the other movies present in the dataset and returns **five** movies that are **most similar**.

The **TMDB API** is used to fetch the data, **Streamlit** is used to build the **web application**, and **Heroku** is used to deploy it.

<p align="center">

https://user-images.githubusercontent.com/66971874/182031442-0334cab9-d5b3-42cf-a880-d15b2a631542.mp4

</p>


## Libraries Used

- Numpy
- Pandas
- Scikit Learn
- Nltk
- Streamlit
- Pickle


## Datasets Used
- [TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata?select=tmdb_5000_movies.csv)


## References
- [CampusX](https://www.youtube.com/c/CampusX-official)
  
  
## Author

Hi, I am Arjun Kohli. I'm currently pursuing a Computer Science major at Krea University. Look forward to knowing you!
- [Linkedin](linkedin.com/in/arjunveerkohli)


## Contributions

Anybody interested in contributing to this project is more than welcome to do so!
