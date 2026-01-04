import argparse
import json
import datetime
parser=argparse.ArgumentParser()
parser.add_argument("filename", default="data.json")
parser.add_argument("category")
parser.add_argument("name")
parser.add_argument("amount", type=int)
arglist=parser.parse_args()
date=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
filename=arglist.filename
category=arglist.category
name=arglist.name
amount=arglist.amount
container={
        "date":date,
        "category":category,
        "name":name,
        "amount":amount        
}
with open(filename,'a') as file:
    json.dump(container, file, indent=4)
    print("Expense added ")