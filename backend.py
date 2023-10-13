import streamlit as st
import pickle
import requests
def fetch_poster(movie_id):
     response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=1ceeac204991c0f414cbe767d2d69dff&language=en-US'.format(movie_id))
     data = response.json()
     return 'https://image.tmdb.org/t/p/w500/'+data['poster_path']


st.title("AdilMovies Recommender System")
movies_list = pickle.load(open('movies.pkl','rb'))
similarity=pickle.load(open('similarity.pkl','rb'))
selected_movie= st.selectbox(
    'Choose a movie',
(movies_list['title'].values))
def recommend(movie):
            recommended_movies=[]
            recommended_movies_poster=[]
            movie_index = movies_list[movies_list['title']== movie].index[0]
            distances = similarity[movie_index]
            movies_list_recommended=sorted(enumerate(distances),reverse=True,key=lambda x:x[1])[1:6]
    
            for i in movies_list_recommended :
                movie_id=movies_list.iloc[i[0]].id
                recommended_movies_poster.append(fetch_poster(movie_id))
                recommended_movies.append(movies_list.iloc[i[0]].title)
                
            return recommended_movies,recommended_movies_poster
        

if st.button('Recommend'):
    names,posters = recommend(selected_movie)
    
    col1, col2, col3,col4,col5 = st.columns(5)

    with col1:
      #st.text(names[0]),
      st.markdown(names[0], unsafe_allow_html=True)
      st.image(posters[0])

    with col2:
    #  st.text(names[1])
      st.markdown(names[1], unsafe_allow_html=True)
      st.image(posters[1])

    with col3:
      # st.text(names[2])
       st.markdown(names[2], unsafe_allow_html=True)
       st.image(posters[2])
    
    with col4:
     #  st.text(names[3])
       st.markdown(names[3], unsafe_allow_html=True)
       st.image(posters[3])
    
    with col5:
    #   st.text(names[4])
       st.markdown(names[4], unsafe_allow_html=True)
       st.image(posters[4])



