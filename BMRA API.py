import os 
import sys
import requests
from pprint import pprint
import json

#if __name__ == "__main__":

#url = 'https://bmreports.com/bmrs/?q=ajax/alldata/MID/Date,SP,Provider,Price,Volume/null/'

#    sFile_Path = sys.argv[1]
#    sDate = sys.argv[2]

url = 'https://bmreports.com/bmrs/?q=ajax/alldata/MID/Date,SP,Provider,Price,Volume/null/2021-06-12/7'

print("Sending request "+ " "+ url)
#responce = requests.Get(url)
#return responce.json()

#print(response)

#response_json = response.json()
#pprint(response_json)