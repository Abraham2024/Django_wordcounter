from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    #context = {
           # 'name':  'Abraham',
           # 'age' : 23,
          #  'nationality' : 'British'

         #   }
         #include the dictionary name when using dictionary and the var key and value when using a variable


    return render(request, 'count.html')


def counter(request):
    text = request.POST['text']
    amount_of_words = len(text.split())
    return render(request, 'counter.html', {'amount': amount_of_words})
