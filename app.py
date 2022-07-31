import streamlit as st
import pickle
import pandas as pd
import requests
import base64

# ------------------------------------------------------------------------------------------------------------------------
# Functions:

def add_background(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True)


def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=*****'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse = True, key = lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []

    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        # fetch poster from API
        recommended_movies_posters.append(fetch_poster(movie_id))

    return recommended_movies, recommended_movies_posters


#------------------------------------------------------------------------------------------------------------------------
# Reading files:

movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))


#-------------------------------------------------------------------------------------------------------------------------------
# Content: Web app buttons and design

st.title('Movie Recommender System')
add_background('background.jpg')

selected_movie_name = st.selectbox(
    'Select a movie',
    movies['title'].values)

if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)
    
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.image(posters[0], caption = names[0])

    with col2:
        st.image(posters[1], caption = names[1])

    with col3:
        st.image(posters[2], caption = names[2])
    
    with col4:
        st.image(posters[3], caption = names[3])

    with col5:
        st.image(posters[4], caption = names[4])