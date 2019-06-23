import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#/*
#from flask import Flask
#from flask.ext.sqlalchemy import SQLAlchemy
#app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/[YOUR_DATABASE_NAME]'
#db = SQLAlchemy(app)
#*/

app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
from models import Bank

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/add")
def add_banks():
    name=request.args.get('name')
    bankHeadAddress=request.args.get('bankHeadAddress')
    bankUrl=request.args.get('bankUrl')
    bankSwiftCode=request.args.get('bankSwiftCode')
    try:
        bank=Bank(
            name=name,
            bankHeadAddress = bankHeadAddress,
            bankUrl = bankUrl,
            bankSwiftCode = bankSwiftCode
        )
        db.session.add(bank)
        db.session.commit()
        return "bank added. bank id={}".format(bank.id)
    except Exception as e:
        return(str(e))

@app.route("/getall")
def get_all():
    try:
        banks=Bank.query.all()
        return jsonify([e.serialize() for e in banks])
    except Exception as e: 
           return(str(e))

@app.route("/get/<id_>")
def get_by_id(id_):
    try:
        bank=Bank.query.filter_by(id=id_).first()
        return jsonify(bank.serialize())
    except Exception as e:
        return(str(e))


"""@app.route("/name/<name>")
def get_bank_name(name):
    return "name : {}".format(name)

@app.route("/details")
def get_bank_details():
    bankHeadAddress=request.args.get('bankHeadAddress')
    bankUrl=request.args.get('bankUrl')
    bankSwiftCode=request.args.get('bankSwiftCode')
    return "Bank Head Office : {}, Swift Code: {}, and  Website: {}".format(bankHeadAddress,bankSwiftCode,bankUrl)
"""
if __name__ == '__main__':
    app.run()
