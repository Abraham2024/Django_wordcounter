from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
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
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email = email).exists():
                messages.info(request, 'Email has already been used' )
                return redirect('signup')
            elif User.objects.filter(username = username).exists():
                messages.info(request, 'Username already exists' )
                return redirect('signup')
            
            else:
                user = User.objects.create_user(username = username, email = email, password = password)
                user.save;
                return redirect('login')
        else:
            messages.info(request, 'Password is not the same')
            return redirect('signup')
    else:
        return render(request, 'signup.html')

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username, password = password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Username or password is incorrect')
            return redirect('login')

    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def courses(request):
    return render(request, 'courses.html')


def counter(request):
    text = request.POST['text']
    amount_of_words = len(text.split())
    return render(request, 'counter.html', {'amount': amount_of_words}

    )
