# Create your tests here.
import requests

def getaccount(id=None):
    BASE_URL='http://127.0.0.1:8000/'
    ENDPOINT='account/'
    id=input("Enter the id")
    resp=requests.get(BASE_URL+ENDPOINT+id+'/')
    print(resp.json())

getaccount(1)
