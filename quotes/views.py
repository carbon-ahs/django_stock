from django.shortcuts import render, redirect
from . models import Stock
from . forms import StockForm
from django.contrib import messages
# Create your views here.
def home(request):
    # pk_4795a3382d6442558cd97acafe4b28ec 
    # https://cloud.iexapis.com/stable/stock/aapl/quote/?token=pk_4795a3382d6442558cd97acafe4b28ec
    import requests
    import json

    if request.method == 'POST':
        ticker = request.POST['ticker']
        link = 'https://cloud.iexapis.com/stable/stock/' + ticker + '/quote/?token=pk_4795a3382d6442558cd97acafe4b28ec'
        api_request = requests.get(link)
        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = 'Error...'

        contex = {
            'key': 'value',
            'api': api,
            'ticker': ticker,
            'link': link,
        }

        return render(request, 'home.html', contex)
    
    else:
        api_request = requests.get('https://cloud.iexapis.com/stable/stock/aapl/quote/?token=pk_4795a3382d6442558cd97acafe4b28ec')
        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = 'Error...'
        
        contex = {
            'key': 'value',
            'api': api,
            'ticker': 'get a ticker man',
        }
        return render(request, 'home.html', contex)




def about(request):

    contex = {
        'key': 'value',
    }
    return render(request, 'about.html', contex)


def add_stock(request): 
    import requests
    import json

    if request.method == 'POST':
        form = StockForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, "Stock added successfully")
        return redirect(add_stock)

    else:
        tickers = Stock.objects.all()
        output_api = []

        for ticker in tickers:
            ticker = str(ticker)
            link = 'https://cloud.iexapis.com/stable/stock/' + ticker + '/quote/?token=pk_4795a3382d6442558cd97acafe4b28ec'
            api_request = requests.get(link)
            try:
                api = json.loads(api_request.content)
                output_api.append(api)
            except Exception as e:
                api = 'Error...'

        
        contex = {
            'key': 'value',
            'tickers': tickers,
            'output_api' : output_api,
        }
        return render(request, 'add_stock.html', contex)


def delete_stock(request, stock_id): 
    item = Stock.objects.get(pk=stock_id)
    item.delete()
    messages.success(request, ("deleed"))
    
    return redirect(add_stock)
