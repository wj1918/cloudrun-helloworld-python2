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

DATABASE = "sqlite3.db"
db = sqlite3.connect(DATABASE)

def query_db(query, args=(), one=False):
    cur = db.execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# DATABASE = os.path.join(BASE_DIR, "sqlite3.db")


for user in query_db('select * from employees'):
    print (user)

if db is not None:
    db.close()
