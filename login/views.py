from django.shortcuts import render
from django.http import HttpResponse
from .models import Feature
# Create your views here.
def index(request):
    feature1 = Feature()
    feature1.id = 0
    feature1.name = 'Fast'
    feature1.details = 'Our services are very fast'
    #context = {
           # 'name':  'Abraham',
           # 'age' : 23,
          #  'nationality' : 'British'

         #   }
         #include the dictionary name when using dictionary and the var key and value when using a variable


    return render(request, 'index.html', {'Feature': feature})


def counter(request):
    text = request.POST['text']
    amount_of_words = len(text.split())
    return render(request, 'counter.html', {'amount': amount_of_words})
