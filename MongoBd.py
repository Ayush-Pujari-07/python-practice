import pymongo

client = pymongo.MongoClient("mongodb+srv://iNeuron:143OnePiece@cluster1.tuzfyk7.mongodb.net/?retryWrites=true&w"
                             "=majority")
db = client.test

number = int(input('Enter the number of data to enter: '))
n = 0
while n != number:
    name = input('Enter the name: ')
    email = input('Enter the email id: ')
    surname = input('Enter the surname: ')
    l = [12, 900, 90000]

    data1 = {
        'name': name,
        'email': email + '@gmail.com',
        'surname': surname,
        'Name List': l
    }
    # Database name is db1
    db1 = client['mongotest']
    # collection name is collection in this case which is same as tables in the MySQL.
    collection = db1['New one']
    # One or single data is pushed into the MongoDB database
    collection.insert_one(data1)
    n += 1

print(client.test)
