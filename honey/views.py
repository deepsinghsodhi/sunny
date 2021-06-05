from django.http import HttpResponse
from django.shortcuts import render

def contact(request):
    return HttpResponse('''<a href="https://www.google.com">Google</a>''')
def source(request):
    context = {'name': "sunny", 'surname': "sodhi"}
    return render(request,"index.html",context)

    # return HttpResponse("this is source page")
