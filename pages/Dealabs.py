import streamlit as st
from dealabs import search_articles
# import sqlite3
# conn = sqlite3.connect("data.db")
# c = conn.cursor()

# Query and display the data you inserted
# list_deals = conn.query('select * from deals')
# st.dataframe(list_deals)

# c.execute("select count(*) from deals")
# db_size = c.fetchone()[0] 

st.set_page_config(page_title="Dealabs finder", page_icon="💲")

st.markdown("# Dealabs finder")
st.sidebar.header("Dealabs")


with st.form('FormSearchArticle'):
    col1, col2, col3 = st.columns(3)
    with col1:
        pattern = st.text_input('Entrez votre recherche')
    # with col2:
    #     page = st.text_input('Page de première recherche')
    # with col3:
    #     iterator = st.text_input('Nombre de pages à parcourir')


    # if st.form_submit_button('Lancer la recherche'):
    #     articles = search_articles(pattern)

st.write(
    """
    # Dealabs finder
    """
)

# if articles != []:
#     df = pd.DataFrame.from_dict(articles, orient='index')
#     df.to_csv('articles.csv')
#     st.download_button(
#         label="Télécharger les articles",
#         data=df.to_csv().encode('utf-8'),
#         file_name=pattern + '.csv',
#         mime='text/csv'
#     )
#     for article in articles:
#         # Création de colonnes
#         col1, col2 = st.columns(2)

#         with col1:
#             try:
#                 st.image(articles[article]['image'])
#             except:
#                 pass

#         with col2:
#             st.write('##', articles[article]['title'])
#             st.write('###', articles[article]['date'], articles[article]['categorie'])
#             st.write('###', articles[article]['link'])
#         st.write('---')