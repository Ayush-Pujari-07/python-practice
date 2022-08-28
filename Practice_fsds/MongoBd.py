import pymongo

credential = "##########"
client = pymongo.MongoClient(f"mongodb+srv://{credential}@cluster1.tuzfyk7.mongodb.net/?retryWrites=true&w"
                             "=majority")
db = client.test

print(db)

def mongo_enterdata():
    global collection
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
    list_of_records = [
        {'companyName': 'iNeuron',
         'product': 'Affordable AI',
         'courseOffered': 'Machine Learning with Deployment'},

        {'companyName': 'iNeuron',
         'product': 'Affordable AI',
         'courseOffered': 'Deep Learning for NLP and Computer vision'},

        {'companyName': 'iNeuron',
         'product': 'Master Program',
         'courseOffered': 'Data Science Masters Program'}
    ]
    # MongoDb can can take dictionary type data sets

    collection.insert_many(list_of_records)
    print(client.test)

    data2 = {"packetType": "D",
             "data": {"checkEngineLightFlag": "F", "batteryVoltageStableTime": 0, "batteryVoltageStable": "0",
                      "batteryVoltageOff": "12.42", "batteryCrankParamTN": "-0.08", "batteryCrankParamVN": "0.00",
                      "batteryCrankParamTP": "-0.08", "batteryCrankParamVP": "0.00", "batteryCrankParamTT": "-0.00008",
                      "batteryCrankParamV0": "0.00", "batteryVoltageMaxOn": "13.05", "batteryVoltageMinOn": "12.97",
                      "batteryVoltageMaxOff": "12.46", "batteryVoltageMinOff": "12.36",
                      "batteryVoltageOnAverage": "13.02",
                      "engineLoadMax": "84", "engineLoadAverage": "39.98", "rpmMax": "3487", "rpmAverage": "1431.29",
                      "gpsSpeedAverage": "21.99", "vssMax": "53.44", "vssAverage": "23.06",
                      "tcuTemperatureMin": "82.40",
                      "tcuTemperatureMax": "109.40", "tcuTemperatureAverage": "104.87", "coolantMin": "158.00",
                      "coolantMax": "188.60", "coolantAverage": "180.20", "packetStartLocal": 1508143346000,
                      "tripStartLocal": 1508143346000, "milIndicator": "F", "monitorsNotReady": 0, "imei": "60DF5417",
                      "gatewayTs": 1515613306592, "diagnosticTroubleCodeData": [345345],
                      "diagnosticPidData": [[64768, 47, 100], [64768, 1, 517376], [64800, 1, 262144], [64768, 5, 125]]},
             "header": {"wrapVer": "1.9.20", "sourceSystem": "CDP", "configVer": "1.1", "oemName": "HUM", "unitType": 0,
                        "cpVer": "7.50.1.9", "igpsVer": "1.3.7", "messageType": "Notification", "pomVer": "1.0",
                        "headerVer": "V6", "timestamp": 0, "deviceType": "InDrive", "visorVer": "1.4.35",
                        "transactionId": "53098471-7787-4160-94b3-cd69dcc70416", "deviceSerialNo": "60DF5417",
                        "subOrganization": "HUM", "organization": "HUM", "imei": "60DF5417",
                        "operation": "Notification"}}

    database = client['Json_formats']
    collection1 = database['collection1']
    collection1.insert_one(data2)

    record = collection.find()

    for i in record:
        print(i)


db1 = client['mongotest']
collection = db1['New one']

record = collection.find()
# for i in record:
# print(i)

fetch = collection.find({'companyName': 'iNeuron'})
course = collection.find({'courseOffered': {'$gte': 'E'}})
for i in course:
    print(i)

print(db1.command('buildinfo'))
# print(db1.command('collstats', collection))

data_new = [
    {
        "item": "canvas",
        "qty": 100,
        "size": {"h": 28, "w": 35.5, "uom": "cm"},
        "status": "A",
    },
    {
        "item": "journal",
        "qty": 25,
        "size": {"h": 14, "w": 21, "uom": "cm"},
        "status": "A",
    },
    {
        "item": "mat",
        "qty": 85,
        "size": {"h": 27.9, "w": 35.5, "uom": "cm"},
        "status": "A",
    },
    {
        "item": "mousepad",
        "qty": 25,
        "size": {"h": 19, "w": 22.85, "uom": "cm"},
        "status": "P",
    },
    {
        "item": "notebook",
        "qty": 50,
        "size": {"h": 8.5, "w": 11, "uom": "in"},
        "status": "P",
    },
    {
        "item": "paper",
        "qty": 100,
        "size": {"h": 8.5, "w": 11, "uom": "in"},
        "status": "D",
    },
    {
        "item": "planner",
        "qty": 75,
        "size": {"h": 22.85, "w": 30, "uom": "cm"},
        "status": "D",
    },
    {
        "item": "postcard",
        "qty": 45,
        "size": {"h": 10, "w": 15.25, "uom": "cm"},
        "status": "A",
    },
    {
        "item": "sketchbook",
        "qty": 80,
        "size": {"h": 14, "w": 21, "uom": "cm"},
        "status": "A",
    },
    {
        "item": "sketch pad",
        "qty": 95,
        "size": {"h": 22.85, "w": 30.5, "uom": "cm"},
        "status": "A",
    },
]

db2 = client['Inventory']
collection = db2['table']
# collection.insert_many(data_new)

# d = collection.find({'status': {'$in': ['A', 'P']}})
# d = collection.find({'status': {'$gt': 'C'}})
# d = collection.find({'qty': {'$gte': 80}})
# d = collection.find({'item': 'sketch pad', 'qty': {'$gte': 95}})  # representation of 'and' operation.
# d = collection.find({'$or': [{'item': 'sketch pad'}, {'qty': {'$gt': 75}}]})

# for i in d:
# print(i)

collection.update_one({'item': 'canvas'}, {'$set': {'item': 'Ayush'}})  # will update the selected field the way we want
# collection.delete_one({'item': 'Ayush'}) # to delete the specific field called
d = collection.find({'item': 'Ayush'})
for i in d:
    print(i)
