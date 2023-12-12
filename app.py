import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
import plotly.express as px
from bdm import search_articles_from_bdm

st.set_page_config(
    page_title="My Streamlit App",
    page_icon='🔎',
    layout="wide"
)

st.title("Article Finder")  
articles = []

st.sidebar.success("Select a demo above.")


with st.form('FormSearchArticle'):
    col1, col2, col3 = st.columns(3)
    with col1:
        pattern = st.text_input('Entrez votre recherche')
    with col2:
        page = st.text_input('Page de première recherche')
    with col3:
        iterator = st.text_input('Nombre de pages à parcourir')


    if st.form_submit_button('Lancer la recherche'):
        articles = search_articles_from_bdm(pattern, iterator, page)

if articles != []:
    df = pd.DataFrame.from_dict(articles, orient='index')
    df.to_csv('articles.csv')
    st.download_button(
        label="Télécharger les articles",
        data=df.to_csv().encode('utf-8'),
        file_name=pattern + '.csv',
        mime='text/csv'
    )
    for article in articles:
        # Création de colonnes
        col1, col2 = st.columns(2)

        with col1:
            try:
                st.image(articles[article]['image'])
            except:
                pass

        with col2:
            st.write('##', articles[article]['title'])
            st.write('###', articles[article]['date'], articles[article]['categorie'])
            st.write('###', articles[article]['link'])
        st.write('---')