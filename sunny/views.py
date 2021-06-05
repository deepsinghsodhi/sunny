from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,"index.html")
def about(request):
    return HttpResponse ("this is about section <a href='/'>back</a>")


def analyze(request):
    djtext=request.GET.get('text')
    removepunc =request.GET.get('removepunc','off')
    fullcaps=request.GET.get('fullcaps','off')
    newlineremover=request.GET.get('newlineremover','off')
    extraspaceremove=request.GET.get('extraspaceremove','off')
    charactercounter=request.GET.get('charactercounter','off')

    if removepunc == "on":
        analyzed= ""
        punctuations = '''{}[];':",.\<>?/*-+!@#$%^&*()_='''
        for item in djtext:
            if item not in punctuations:
                analyzed=analyzed+item

        params={'purpose':'Removed Punctutions','analyzed_text':analyzed}
        return render(request,"analyze.html",params)
    elif fullcaps=='on':
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        return render(request, "analyze.html", params)

    elif newlineremover=='on':
        analyzed=""
        for char in djtext:
            if char != "/n":
                analyzed=analyzed+char
        params = {'purpose': 'Remove new line', 'analyzed_text': analyzed}
        return render(request, "analyze.html", params)

    elif extraspaceremove =='on':
        analyzed=""
        for index,char in enumerate(djtext):
            if djtext[index]== " " and djtext[index+1]==" ":
                pass
            else:
                analyzed= analyzed+char


        params = {'purpose': 'Remove new line', 'analyzed_text': analyzed}
        return render(request, "analyze.html", params)

    elif charactercounter =='on':
        analyzed=0
        for char in djtext:
            analyzed=analyzed+1


        params = {'purpose': 'character count is', 'analyzed_text': analyzed}
        return render(request, "analyze.html", params)

    else:
        return HttpResponse('error')
def fullcaps(request):
    return HttpResponse ("this is fullcaps section <a href='/'>back</a>")
def newlineremover(request):
    return HttpResponse ("this is newlineremover section <a href='/'>back</a>")
def extraspace(request):
    return HttpResponse ("this is extraspace section <a href='/'>back</a>")
def charcount(request):
    return HttpResponse ("this is charcount section <a href='/'>back</a>")