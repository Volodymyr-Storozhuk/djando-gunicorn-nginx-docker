from django.shortcuts import render


# Create your views here.
def hello_app(request):
    return render(request, 'app_1/index.html')
