from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, '<h1>This is a paper page </h1>', {})