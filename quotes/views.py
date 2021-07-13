from django.shortcuts import render

# Create your views here.
def home(request):
    # pk_4795a3382d6442558cd97acafe4b28ec 
    # https://cloud.iexapis.com/stable/stock/aapl/quote/?token=pk_4795a3382d6442558cd97acafe4b28ec
    import requests
    import json

    api_request = requests.get('https://cloud.iexapis.com/stable/stock/aapl/quote/?token=pk_4795a3382d6442558cd97acafe4b28ec')
    try:
        api = json.loads(api_request.content)
    except Exception as e:
        api = 'Error...'

    contex = {
        'key': 'value',
        'api': api,
    }

    return render(request, 'home.html', contex)

def about(request):

    contex = {
        'key': 'value',
    }
    return render(request, 'about.html', contex)

