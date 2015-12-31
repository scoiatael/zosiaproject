from django.shortcuts import render

def index(request):
    title = "Program"
    return render(request, 'agenda.html', locals())
