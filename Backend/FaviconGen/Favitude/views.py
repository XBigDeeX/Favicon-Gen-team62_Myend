from django.shortcuts import render

# Create your views here.
def home(request):
  return render(request, 'Favitude/index.html')  

def about(request):
  return render(request, 'Favitude/about.html')


def login_page(request):
  return render(request, 'Favitude/login.html')


def signup_page(request):
  return render(request, 'Favitude/signup.html')  

def contact_page(request):
  return render(request, 'Favitude/contact.html')

def error_page(request):
  return render(request, 'Favitude/error.html')

def generate_page(request):
  return render(request, 'Favitude/generate.html')

def imageGen_page(request):
  return render(request, 'Favitude/imageGen.html')            