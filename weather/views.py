from django.shortcuts import render

# Create your views here.
def index(request):
    if request.method=="POST":
        city=request.POST["place"]      ##place is coming from the form that is in index.html file
    else:           ## written else statement to avoid the local varible referenced  before assignment
    ## this error always happnens anytime we are using an if statement and there is a variable being assigned without addina an else statement
        city=""       
    return render(request,'index.html',{'city':city})