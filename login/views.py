from django.shortcuts import render
from django.http import HttpResponse
from .models import Feature
# Create your views here.
def index(request):
    feature1 = Feature()
    feature1.id = 0
    feature1.name = 'Fast'
    feature1.details = 'Our services are very fast'

    feature2 = Feature()
    feature2.id = 1
    feature2.name = 'Reliable'
    feature2.details = 'Our services are very reliable'


    feature3 = Feature()
    feature3.id = 2
    feature3.name = 'Easy to use'
    feature3.details = 'Our services are very easy to use'
    #context = {
           # 'name':  'Abraham',
           # 'age' : 23,
          #  'nationality' : 'British'

         #   }
         #include the dictionary name when using dictionary and the var key and value when using a variable


    return render(request, 'index.html', {'feature1': feature1, 'feature2' : feature2, 'feature3' : feature3})


def counter(request):
    text = request.POST['text']
    amount_of_words = len(text.split())
    return render(request, 'counter.html', {'amount': amount_of_words})
