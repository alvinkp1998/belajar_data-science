import streamlit as st
import pandas as pd
from utils import filter_recommendation

def recommendation_system(mode):
    df = pd.read_csv('./data/demographic_with_overview.csv')
    
    if mode == 'Demographic Filtering':
        st.title('Best recommendations for you!')
        st.sidebar.subheader('Please input your data:')
        
        # genre selection
        genre = st.sidebar.multiselect('Genres', df.columns[6:-1])

        # data for slider
        _, _, _, runtime_min, runtime_q1, _, runtime_q3, runtime_max = df['runtime'].describe()
        _, _, _, year_min, year_q1, _, year_q3, year_max = df['release_year'].describe()

        # year slider
        min_year, max_year = st.sidebar.slider(
            'Select release year:',
            year_min, year_max, (year_q1, year_q3) 
        )

        # minutes slider
        min_duration, max_duration = st.sidebar.slider(
            'Select movie duration:',
            runtime_min, runtime_max, (runtime_q1, runtime_q3)
        )

        # confirm selected paramters above and query the best recommendation
        search = st.sidebar.button('Search!')


        if search:
            recommendations = filter_recommendation(
                df=df,
                genres=genre,
                min_duration=min_duration,
                max_duration=max_duration,
                min_year=min_year,
                max_year=max_year,
                topN=10
            )
            for movie in recommendations.values:
                title, genre, release_year, runtime, _,_,_, overview = movie
                list_template = f"""
                <ul class="collection">
                    <li class="collection-item avatar">
                        <i class="material-icons circle">{title[0]}</i>
                        <span class="title">{title}</span>
                        <p>{genre} <br>
                            {overview}
                        </p>
                        <a href="#!" class="secondary-content"><i class="material-icons">{release_year}</i></a>
                    </li>
                </ul>
                """
                st.markdown(list_template, unsafe_allow_html=True)
                
def main():
    st.sidebar.title('WebApp')
    main_mode = st.sidebar.radio('Choose option below:',
    ['Home', 'Demographic Filtering']
    )

    if main_mode == 'Home':
        st.title('Home')
        st.markdown('This is homepage')
    elif main_mode == 'Demographic Filtering':
        recommendation_system(main_mode)

if __name__ == '__main__':
    main()