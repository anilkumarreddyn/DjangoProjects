from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hydjobsinfo(request):
    s ='<h1>hyderabad jobs information group'</h1>
    return HttpResponse(s)

def chennaijobsinfo(request):
    s ='<h1>chennai  jobsjobs information group'</h1>
    return HttpResponse(s)
def mumbaijobsinfo(request):
    s ='<h1>mumbai  jobs information group'</h1>
    return HttpResponse(s)
def kolkatajobsinfo(request):
    s ='<h1>kolkata jobs information group'</h1>
    return HttpResponse(s)
