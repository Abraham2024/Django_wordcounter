from django.shortcuts import render
from django.http import HttpResponse
from .models import Feature
# Create your views here.
def index(request):
    features = Feature.objects.all()
    #without using database
    #feature1 = Feature()


   # feature1.id = 0
    #feature1.name = 'Fast'
   # feature1.details = 'Our services are very fast'

    #feature2 = Feature()
   # feature2.id = 1
   # feature2.name = 'Reliable'
   # feature2.details = 'Our services are very reliable'


   # feature3 = Feature()
    #feature3.id = 2
   # feature3.name = 'Easy to use'
    #feature3.details = 'Our services are very easy to use'

   # feature4 = Feature()
   # feature4.id = 3
    #feature4.name = 'Trustworthy'
   # feature4.details = 'We are very trustworthy'

   # features = [feature1, feature2, feature3, feature4] 
    #context = {
           # 'name':  'Abraham',
           # 'age' : 23,
          #  'nationality' : 'British'

         #   }
         #include the dictionary name when using dictionary and the var key and value when using a variable


    return render(request, 'index.html', {'features': features})

def signup(request):
    return render(request, 'signup.html')

def login(request):

    return render(request, 'login.html')


def counter(request):
    text = request.POST['text']
    amount_of_words = len(text.split())
    return render(request, 'counter.html', {'amount': amount_of_words}

    )
