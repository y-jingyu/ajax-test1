from django.shortcuts import render,HttpResponse
import json
# Create your views here.
def index(request):
    return render(request, 'hi.html', {'qq':123})


def index3(request):
    return render(request, 'dome2.html', {'content':[1,2,3]})

def jq1(request):
    rt = {
        'qq': '123'
    }
    rt1 = json.dumps(rt)
    return HttpResponse(rt1)
    

def jq2(request):
    rt = {
        'qq': '123'
    }
    rt1 = json.dumps(rt)
    return HttpResponse(rt1)