import os 
import sys
import requests
import json

def GetWeighted_Price(url):
    #outputs the url to see date and HH requested
    #print("Sending request "+ " "+ url)
    #sends a get request to collect the data and format the data into Json arr
    responce = requests.get(url).json()
    # split the arry
    data = responce['arr']
    #Calculate the volume and MWH for APX and N2EX
    nVol = (float(data[0]['MarketIndexPrice']) * float(data[0]['marketIndexVolume']))+(float(data[1]['MarketIndexPrice']) * float(data[1]['marketIndexVolume']))
    nMwh = float(data[0]['marketIndexVolume']) + float(data[1]['marketIndexVolume'])
    #Print the result

    print(round(nVol / nMwh, 4))
    #return round(nVol / nMwh, 4)

def Check_SSP_Price(url, HH):
    #outputs the url to see date and HH requested
    #print("Sending request "+ " "+ url)
    #sends a get request to collect the data and format the data into Json arr
    responce = requests.get(url).json()
    # split the arry
    data = responce['arr']
    #print(data)

    for i in data:
        if i['sp'] == HH:
            print("SSP :" + i['ssp'] + " SBP : " + i['sbp'])
            break

#Code starts from here

if __name__ == "__main__":

    pPrice = sys.argv[1] #Price
    pdate = sys.argv[2] #Date
    phh = sys.argv[3] #HH

    if pPrice == 'APX':

        #Concates the prmas into the url
        url = 'https://bmreports.com/bmrs/?q=ajax/alldata/MID/Date,SP,Provider,Price,Volume/null/'+ pdate + "/" + phh
        #Calls the function to get the data
        GetWeighted_Price(url)

    if pPrice == 'SSP':
        url = 'https://bmreports.com/bmrs/?q=ajax/alldata/DERSYSDATA/settlementDate,Period,SSP,SBP,BD,PDC,RSP,NIV,SPA,BPA,RP,RPRV,OV,BV,TOV,TBV,ASV,ABV,TASV,TABV,Linkstodata/NULL/'+ pdate
        Check_SSP_Price(url, phh)
