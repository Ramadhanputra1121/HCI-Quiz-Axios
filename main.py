from flask import Flask, render_template,request, jsonify
import pymongo
app= Flask(__name__)
client=pymongo.MongoClient("localhost",27017)
db=client.fishapi

# Habis run sekali pastiin line dibawah ini udah diapus, supaya data gak numpuk di database
pond={"name": "alpha", "location":"jakarta", "material": "beton", "shape":"bundar","fish_count":200,"date": "11-11-2022"}
db.pond.insert_one(pond)

# Code buat mengambil data dari front end. Nama gak boleh sama buat semua user
@app.route("/api/v1/registrasi",methods=["POST"])
def regis():
    getdata=request.get_json()
    result=db.pond.find({"name":getdata["name"]})
    if result:
        return "Gak Bisa"
    result=db.pond.insert_one(getdata)
    return "OK"

# Code buat memberi data pond ke front end
@app.route("/api/v1/pondinfo",methods=["GET"])
def pondinfo():
    datas= db.pond.find({},{"_id":0})
    return jsonify([data for data in datas])

# Code buat update data, data terupdate sesuai dengan parameter pondname
@app.route("/api/v1/pondinfo/<pondname>",methods=["PUT"])
def update(pondname):
    getdata=request.get_json()
    result=db.pond.update_one( {"name":pondname} , { "$set" : getdata})
    return "OK"

@app.route("/api/v1/pondinfo/<name>",methods=["GET"])
def pondinfosingle(name):
    datas= db.pond.find({"name":name},{"_id":0})
    return jsonify([data for data in datas])