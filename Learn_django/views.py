from django.http import HttpResponse
from django.shortcuts import render

def index(request):
        return render(request,'index.html')

def analyze(request):
    djtext=request.POST.get('text','default')
    removepun= request.POST.get('removepun','off')
    fullcap = request.POST.get('fullcap','off')
    newline = request.POST.get('newline','off')
    extraspaceremover = request.POST.get('extraspace','off')

    if removepun == 'on':
        punctuation =''''!@#$%^&*()_'"{}[]:\;<>,.?/-|'''
        analyzed = ""

        for i in djtext:
            if i not in punctuation:
                analyzed = analyzed + i
        params ={'purpose':"removed punctuation",'analyzed_text':analyzed }
        djtext=analyzed

    if(fullcap == "on"):
        analyzed =""
        for i in djtext:
            analyzed =analyzed + i.upper()
        params ={'purpose':"changed to uppercase",'analyzed_text':analyzed }
        djtext = analyzed

    if(extraspaceremover =="on"):
        analyzed =""
        for index, i in enumerate(djtext):
            if not(djtext[index]==" " and djtext[index+1]==" ") :
                analyzed =analyzed + i

        params ={'purpose':"extra space is removed",'analyzed_text':analyzed }
        djtext=analyzed

    if(newline =="on"):
        analyzed =""
        for i in djtext:
            if i !="\n" and i!="\r":
                analyzed =analyzed + i
        params ={'purpose':"new line removed",'analyzed_text':analyzed }

    if(removepun!="on" and newline !="on" and fullcap !="on" and extraspaceremover!="on"):
        return HttpResponse("please select any operation and try again")

    return render(request,'analys.html',params)
