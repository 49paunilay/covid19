from django.shortcuts import render
import requests
import json
url = "https://covid-193.p.rapidapi.com/statistics"

headers = {
    'x-rapidapi-key': "99c4b22076mshf1457f3160ac6a4p17cb27jsn3fb12f3333d5",
    'x-rapidapi-host': "covid-193.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers).json()
def heloWorld(request):
    noOfResult = int(response['results'])
    countryList=[]
    for i in range(0,noOfResult):
        countryList.append(response['response'][i]['country'])
    if request.method=='POST':
        selectedcountry=request.POST['countryselect']
        for i in range(0,noOfResult):
            if selectedcountry == response['response'][i]['country']:
                newCase =response['response'][i]['cases']['new']
                ActiveCases = response['response'][i]['cases']['active']
                criticalCase = response['response'][i]['cases']['critical']
                recoveredCase=response['response'][i]['cases']['recovered']
                total = response['response'][i]['cases']['total']
                try:
                    death = total-ActiveCases-recoveredCase
                except:
                    death='undefined'
        context = {
            'selectedcountry':selectedcountry,
            'countryList':countryList,
            'newCase':newCase,
            'ActiveCases':ActiveCases,
            'criticalCase':criticalCase,
            'recoveredCase':recoveredCase,
            'total':total,
            'death':death
        }
        return render(request,'h.html',context)
    context={
        'countryList':countryList
    }
    return render(request,'h.html',context)