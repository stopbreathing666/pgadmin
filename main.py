import psycopg2
import requests
from API import RequestManager

request_manager = RequestManager()
categories = request_manager.get('/products/categories/')

connection = psycopg2.connect(
    database='json_19_30',
    user='postgres',
    password='123456',
    host='localhost'
)

cursor = connection.cursor()

cursor.execute('''
DROP TABLE IF EXISTS categories;
CREATE TABLE IF NOT EXISTS categories(
    category_id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    category_name VARCHAR(50)
);
''')

connection.commit()
# connection.close()

request_manager = RequestManager()
categories = request_manager.get('/products/categories/')

for category in categories:
    cursor.execute('INSERT INTO categories(category_name) VALUES (%s)', (category,))
    connection.commit()
