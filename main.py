from fastapi import FastAPI
import mariadb
import json

app = FastAPI()

class create_dict(dict):
    def __init__(self):
        self = dict()

    def add(self, key, value):
        self[key] = value

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/users")
async def users():
    try:
        conn = mariadb.connect(
            user="web",
            password="vagrant",
            host="10.10.1.9",
            port=3306
        )

        cur = conn.cursor()

        cur.execute("SELECT Host,User FROM mysql.user")

        result = cur.fetchall()

        conn.close()

        #mydict = create_dict()
        #i=1
        #for row in result:
        #    mydict.add(str(i),({"Host":row[0],"User":row[1]}))
        #    i+=1

        #stud_json = json.dumps(mydict, indent=2, sort_keys=True)

        return json.dumps(result, indent=2)
    
    except mariadb.Error as e:
        return {"message": "error database"}
