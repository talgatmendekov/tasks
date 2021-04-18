from django.shortcuts import render

def third(request):
    return render(request, 'tasks/test3.html')
