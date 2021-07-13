from django.shortcuts import render

# Create your views here.
def home(request):

    contex = {
        'key': 'value',
    }

    return render(request, 'home.html', contex)

