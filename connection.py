import pymongo
from pymongo import MongoClient

client = MongoClient('mongodb+srv://vic:1234@cluster0.ir6uj.mongodb.net/test?retryWrites=true&w=majority')

db = client.test.test

post_data = {
    'title': 'Succesfully wrote to database',
    'content': 'This was made using Flask as our python API and ReactJS',
    'author': 'Victor'
}
result = db.insert_one(post_data)
print('One post: {0}'.format(result.inserted_id))