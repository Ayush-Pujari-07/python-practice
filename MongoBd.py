import pymongo

client = pymongo.MongoClient("mongodb+srv://iNeuron:143OnePiece@cluster1.tuzfyk7.mongodb.net/?retryWrites=true&w"
                             "=majority")
db = client.test


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

for i in fetch:
    print(i)
