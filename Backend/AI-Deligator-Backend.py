from os import curdir
import pymysql
import json
import datetime
from flask import Flask, request, jsonify, session, escape, url_for, redirect, render_template
from flask_cors import CORS
import pandas as pd
import time
db = None
cursor = None
#后端服务启动
app = Flask(__name__)
CORS(app, resources=r'/*')

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def welcome():
    return 'Hello. AI-Delegator backend! Contact: chongzhengzhao AT gmail.com'

@app.route('/tickets/customer', methods = ['POST', 'GET'])
def tickets_customer():
    try:
        # if request.method == "POST":
        if True:
            # page = request.form.get("page")
            # limit = request.form.get("limit")
            page = "1"
            limit = "3"
            try:
                cursor.execute("SELECT * FROM tickets ORDER BY id DESC LIMIT " + str((int(page)-1)*int(limit)) + "," + limit)
                data = cursor.fetchall()
                db.commit()
                cursor.execute("select count(*) from tickets")
                count = cursor.fetchone()
                db.commit()
                print(count[0])
            except Exception as e:
                print("出现问题，重新连接DB")
                db_connect()
                cursor.execute("SELECT * FROM tickets ORDER BY id DESC LIMIT " + str((int(page)-1)*int(limit)) + "," + limit)
                data = cursor.fetchall()
                db.commit()
                cursor.execute("select count(*) from tickets")
                count = cursor.fetchone()
                db.commit()
                print(count[0])
            if (data != None):
                    jasondata_data = ([{'case_id':a,
                                        'time':b,
                                        'app_name':c,
                                        'name':d,
                                        'email':e,
                                        'issue_type':f,
                                        'impact_rank':g,
                                        'description': h,
                                        'file': i,
                                        'assign': j,
                                        'status': k
                                            } for a,b,c,d,e,f,g,h,i,j,k in data])
                    jsondata = {"code":0, "data":jasondata_data, "count":count[0], "msg":"success"}
                    return jsonify(jsondata)
    except Exception as e:
        print(e)
        return "Failure"

@app.route('/tickets/manager', methods = ['POST', 'GET'])
def tickets_manager():
    try:
        # if request.method == "POST":
        if True:
            # page = request.form.get("page")
            # limit = request.form.get("limit")
            page = "1"
            limit = "100"
            try:
                cursor.execute("SELECT * FROM tickets LIMIT " + str((int(page)-1)*int(limit)) + "," + limit)
                data = cursor.fetchall()
                db.commit()
                cursor.execute("select count(*) from tickets")
                count = cursor.fetchone()
                db.commit()
                print(count[0])
            except Exception as e:
                print("出现问题，重新连接DB")
                db_connect()
                cursor.execute("SELECT * FROM tickets LIMIT " + str((int(page)-1)*int(limit)) + "," + limit)
                data = cursor.fetchall()
                db.commit()
                cursor.execute("select count(*) from tickets")
                count = cursor.fetchone()
                db.commit()
                print(count[0])
            if (data != None):
                    jasondata_data = ([{'case_id':a,
                                        'time':b,
                                        'app_name':c,
                                        'name':d,
                                        'email':e,
                                        'issue_type':f,
                                        'impact_rank':g,
                                        'description': h,
                                        'file': i,
                                        'assign': j,
                                        'status': k
                                            } for a,b,c,d,e,f,g,h,i,j,k in data])
                    jsondata = {"code":0, "data":jasondata_data, "count":count[0], "msg":"success"}
                    return jsonify(jsondata)
    except Exception as e:
        print(e)
        return "Failure"

@app.route('/tickets/resolve', methods = ['POST', 'GET'])
def resolved_issue():
    try:
        if request.method == "POST":
            id = request.form.get("case_id")
            if id is None:
                return jsonify({"code": 1, "msg":"empty id", "op": "resolve issue"})
        else:
            id = request.args.get("case_id")
            if id is None:
                return jsonify({"code": 1, "msg":"empty id", "op": "resolve issue"})
        cursor.execute("UPDATE tickets SET status='%s' WHERE id ='%s' " %("Resolved",id))
        db.commit()
        return jsonify({"code": 0, "msg": "success", "id": id, "op": "resolve issue"})
    except Exception as e:
        db.rollback()
        return jsonify({"code": 1, "msg": str(e), "op": "resolve issue"})


@app.route('/tickets/delete', methods = ['POST', 'GET','DELETE'])
def delete_issue():
    try:
        if request.method == "POST":
            id = request.form.get("case_id")
            if id is None:
                return jsonify({"code": 1, "msg":"empty id", "op": "delete issue"})
        else:
            id = request.args.get("case_id")
            if id is None:
                return jsonify({"code": 1, "msg":"empty id", "op": "delete issue"})
        cursor.execute("DELETE FROM tickets WHERE id ='%s' " %(id))
        db.commit()
        return jsonify({"code": 0, "msg": "success", "id": id, "op": "delete issue"})
    except Exception as e:
        db.rollback()
        return jsonify({"code": 1, "msg":"fail", "console": str(e), "op": "delete issue"})

def db_connect():
    #数据库连接
    global db
    global cursor
    db = pymysql.connect(******)
    cursor = db.cursor()
if __name__ == "__main__":
    #数据库连接
    db_connect()
    print("Good bye!")
    app.run(host='0.0.0.0',port=10241, debug = True)