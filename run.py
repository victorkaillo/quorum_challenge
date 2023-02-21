# -*- coding: utf-8 -*-
from json import loads
import pandas as pd

from threading import Thread
from src.data_extract_service import DataExtract
from sanic import Sanic, json

app = Sanic("QuorumAPI")

HOST = "0.0.0.0"
PORT = 80


@app.get("/")
async def root(request):
    return json({"Version": "0.0.1"})


@app.get("/make_files_bills_and_legislators_count")
async def make_files_bills_and_legislators(request):
    # is_valid, message = handler_token(request.headers.get("Authorization")) # TODO: TOKEN TO LIMIT ACCESS
    # if is_valid:
    data_extract = DataExtract()
    x = Thread(target=data_extract.make_files)
    x.start()
    return json({"message": "Running the task"})
    # else:
    #     return json(message)


@app.get("/get_bills_count")
async def get_bills(request):
    # is_valid, message = handler_token(request.headers.get("Authorization")) # TODO: TOKEN TO LIMIT ACCESS
    # if is_valid:
    bills = pd.read_csv('bills.csv')
    bills_json = loads(bills.to_json(orient="index"))
    return json(bills_json)
    # else:
    #     return json(message)

@app.get("/get_legislators_support_oppose_count")
async def get_legislators_support_oppose(request):
    # is_valid, message = handler_token(request.headers.get("Authorization")) # TODO: TOKEN TO LIMIT ACCESS
    # if is_valid:
    legislators = pd.read_csv('legislators_support_oppose_count.csv')
    legislators_json = loads(legislators.to_json(orient="index"))
    return json(legislators_json)
    # else:
    #     return json(message)

if __name__ == "__main__":
    app.run(host=HOST, port=PORT, debug=True)
