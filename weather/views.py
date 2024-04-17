from django.shortcuts import render
import json   ## wee need this as when we call api, we will get response in json
import urllib.request

# Create your views here.
def index(request):
    if request.method=="POST":
        city=request.POST["place"]      ##place is coming from the form that is in index.html file
        
        #urlopen will open the url. we will call the api . In the url, q means query
        res=urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=5616e2e15029c44e1b0fec3de5479953').read()
        json_data=json.loads(res)  ## we are reading json data that we got from the api request
        data={
            "country_code":str(json_data['sys']['country']),
            "coordinate": str(json_data['coord']['lon'])+' '+str(json_data['coord']['lat']),
            "temp":str(json_data['main']['temp']) + 'k',  ## we can do this float, but as we want to add k we converted it to str
            "pressure":str(json_data['main']['pressure']) + "hPa",
            "humidity":str(json_data['main']['humidity'])+"%",
        }  


    else:           ## written else statement to avoid the local varible referenced  before assignment
    ## this error always happnens anytime we are using an if statement and there is a variable being assigned without adding else statement
        data={}       
    return render(request,'index.html',data)