# Copyright 2020 Google, LLC.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START cloudrun_helloworld_service]
# [START run_helloworld_service]
import os

import sys
import sqlite3

from flask import Flask
from flask import g

app = Flask(__name__)

DATABASE = os.path.join(app.root_path, 'sqlite3.db')


@app.route("/root_path")
def base():
    return app.root_path


@app.route("/path")
def path():
    return DATABASE


@app.route("/")
def hello_world():

    # for user in query_db('select * from employees'):
    #     print (user)

    name = os.environ.get("NAME", "World")
    return "Hello {}!".format(name)

@app.route("/employees")
def employees():
    print(DATABASE)
    db = sqlite3.connect(DATABASE)
    cur = db.execute('select FirstName from employees;')
    rv = cur.fetchall()
    result=""
    for user in rv:
        print (user)
        result+=user[0]+";"

    cur.close()
    db.close()
    return result

@app.route("/tables")
def tables():
    print("DATABASE is ", DATABASE)
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    result =cursor.fetchall()
    print (result)
    # return result
    return "Tables!"

@app.route("/version")
def version():
    print("DATABASE is ", DATABASE)
    con = None

    try:
        con = sqlite3.connect(DATABASE)
        cur = con.cursor()
        cur.execute('SELECT SQLITE_VERSION()')
        data = cur.fetchone()[0]

        return data

    except sqlite3.Error, e:

        print "Error {}:".format(e.args[0])
        # sys.exit(1)
        return e

    finally:

        if con:
            con.close()    

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
# [END run_helloworld_service]
# [END cloudrun_helloworld_service]
