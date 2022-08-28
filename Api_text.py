from flask import Flask, request, jsonify
import pymongo

# call the flask class into an object app
app = Flask(__name__)

credential = "##############"
client = pymongo.MongoClient(
    f"mongodb+srv://{credential}@cluster1.tuzfyk7.mongodb.net/?retryWrites=true&w=majority")
db = client.test


# "@" is an annotation to let computer know that it should use the function just below the line
@app.route('/post', methods=['GET', 'POST'])  # GET will post data in the url
# POST method is more secure than the GET method
# POST will send the data with the body which won't reflect the data provided
def test1():
    if request.method == "POST":
        a = request.json['NUM1']
        b = request.json['NUM2']
        result = a + b
        return jsonify(str(result))


@app.route("/get", methods=['GET', 'POST'])
def test2():
    if request.method == "POST":
        a = request.json['NUM1']
        b = request.json['NUM2']
        result = a * b
        return jsonify(result)


@app.route("/mongo_test", methods=['GET', 'POST'])
def test_mongo():
    if request.method == "POST":
        data1 = request.json["name"]
        data2 = request.json["age"]
        data3 = request.json["e-mail"]
        complete_data = {
            "Name": data1,
            "Age": data2,
            "E-mail": data3
        }
        database = client['Json_formats']
        collection1 = database['collection1']
        collection1.insert_one(complete_data)

        status = "Success"
        return status


if __name__ == '__main__':
    app.run()
