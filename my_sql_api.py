from flask import Flask, request, jsonify
import pymongo

app = Flask(__name__)

client = pymongo.MongoClient("mongodb+srv://iNeuron:143OnePiece@cluster1.tuzfyk7.mongodb.net/?retryWrites=true&w"
                             "=majority")


@app.route("/insert", methods=['POST'])
def insert():
    if request.method == "POST":
        data1 = request.json["name1"]
        data2 = request.json["age1"]
        data3 = request.json["e-mail"]
        clint_name = request.json["database_name"]
        table_name = request.json["table_name"]
        complete_data = {
            "Name": data1,
            "Age": data2,
            "E-mail": data3
        }

        database = client[clint_name]
        collection1 = database[table_name]
        collection1.insert_one(complete_data)

        return jsonify(str("Successful"))


@app.route("/delete", methods=['POST'])
def delete():
    if request.method == 'POST':
        data = request.json['name']
        clint_name = request.json["database_name"]
        table_name = request.json["table_name"]
        db = client[clint_name]
        tables = db[table_name]
        tables.delete_one({"Name": data})
        return jsonify(str("Successful"))


@app.route("/test_fun")
def test():
    get_name = request.args.get("get_name")
    mobile_number = request.args.get("mobile")
    mail_id = request.args.get('mail_id')
    return "This is my first api calling on website by: {} {} {}".format(get_name, mobile_number, mail_id)


if __name__ == '__main__':
    app.run(port=5001)
