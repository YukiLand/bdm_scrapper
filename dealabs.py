from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# Gestion d'une base de données
import sqlalchemy as db

class DataBase():
    def __init__(self, name_database='dealabs'):
        self.name = name_database
        self.url = f"sqlite:///{name_database}.db"
        self.engine = db.create_engine(self.url)
        self.connection = self.engine.connect()
        self.metadata = db.MetaData()
        self.table = self.engine.table_names()


    def create_table(self, name_table, **kwargs):
        colums = [db.Column(k, v, primary_key = True) if 'id_' in k else db.Column(k, v) for k,v in kwargs.items()]
        db.Table(name_table, self.metadata, *colums)
        self.metadata.create_all(self.engine)
        print(f"Table : '{name_table}' are created succesfully")

    def read_table(self, name_table, return_keys=False):
        table = db.Table(name_table, self.metadata, autoload=True, autoload_with=self.engine)
        if return_keys:table.columns.keys()
        else : return table


    def add_row(self, name_table, **kwarrgs):
        name_table = self.read_table(name_table)

        stmt = (
            db.insert(name_table).
            values(kwarrgs)
        )
        self.connection.execute(stmt)
        print(f'Row id added')


    def delete_row_by_id(self, table, id_):
        name_table = self.read_table(name_table)

        stmt = (
            db.delete(name_table).
            where(students.c.id_ == id_)
            )
        self.connection.execute(stmt)
        print(f'Row id {id_} deleted')

    def select_table(self, name_table):
        name_table = self.read_table(name_table)
        stm = db.select([name_table])
        return self.connection.execute(stm).fetchall()

def disable_popup():
    try: 
        driver.find_element(By.CLASS_NAME, "space--ml-a button button--shape-circle button--type-tertiary button--mode-default button--size-s button--square".replace(" ", ".")).click()
    except:
        pass
    time.sleep(0.5)

def collect_data(articles, keyword):
    datas = []
    for article in articles:
        data = {}
        img = ""
        link = ""
        price  = ""
        name = ""
        seller = ""
        pattern = keyword.replace(" ", "_")


        try:
            img = article.find_element(By.CLASS_NAME, "thread-image width--all-auto height--all-auto imgFrame-img".replace(' ', '.')).get_attribute("src")
        except:
            pass
        try:
            link = article.find_element(By.CLASS_NAME, "cept-tt thread-link linkPlain thread-title--list js-thread-title".replace(' ', '.')).get_attribute("href")
        except:
            pass
        try:
            price = article.find_element(By.CLASS_NAME, "thread-price text--b cept-tp size--all-l size--fromW3-xl".replace(' ', '.')).text
        except:
            pass
        try:
            name = article.find_element(By.CLASS_NAME, "cept-tt thread-link linkPlain thread-title--list js-thread-title".replace(' ', '.')).text
        except:
            pass
        try:
            seller = article.find_element(By.CLASS_NAME, "overflow--wrap-off text--b text--color-brandPrimary link".replace(' ', '.')).text
        except:
            pass

        data = {
            "img": img,
            "link": link,
            "price": price,
            "name": name,
            "seller": seller,
            "pattern": pattern
        }
        print(data)
        datas.append(data)
    return datas

def search_articles(keyword):
    driver = webdriver.Chrome("./chromedriver")
    driver.get("https://www.dealabs.com/")

    time.sleep(2)

    driver.find_element(By.CLASS_NAME, "overflow--wrap-on flex--grow-1 flex--fromW3-grow-0 width--fromW3-ctrl-m space--mb-3 space--fromW3-mb-0 space--fromW3-mr-2 button button--shape-circle button--type-primary button--mode-brand".replace(" ", ".")).click()

    time.sleep(0.5)

    driver.find_element(By.CLASS_NAME, "input width--all-12 input-with-icon--l input--search".replace(" ", ".")).click()

    driver.find_element(By.CLASS_NAME, "input width--all-12 input-with-icon--l input--search".replace(" ", ".")).send_keys(keyword)

    driver.find_element(By.CLASS_NAME, "input width--all-12 input-with-icon--l input--search".replace(" ", ".")).send_keys(Keys.ENTER)

    disable_popup()

    articles = driver.find_elements(By.CLASS_NAME, "thread cept-thread-item thread--type-list imgFrame-container--scale thread--deal".replace(" ", "."))

    dataCollected = collect_data(articles, keyword)

    # Définir une classe

    class Deals:
        def __init__(self, img:str, link:str, price:str, name:str, seller:str, pattern:str):
            self.img = img
            self.link = link
            self.price = price
            self.name = name
            self.seller = seller
            self.pattern = pattern
        
        def show_data(self, *args):
            for arg in args:
                print(arg)

        def show_data_kwargs(self, **kwargs):
            print(kwargs)

    database = DataBase('data')
    database.create_table('deals', img=db.String, link=db.String, price=db.String, name=db.String, seller=db.String, pattern=db.String)
    i = 0
    for line in range(len(dataCollected)):
        database.add_row('deals', **dataCollected[i])
        i += 1

    database.select_table('deals')

