from django.shortcuts import render, redirect
import requests
import json
from .models import Stock
from .forms import StockForm
from django.contrib import messages


def home(request):

	if request.method == "POST":
		ticker = request.POST['ticker']
		api_request = requests.get(f'https://cloud.iexapis.com/stable/stock/{ticker}/quote?token=pk_24ff01ef02954ffc9459e06ddc72dac8')

		try:
			api = json.loads(api_request.content)
		except Exception as e:
			api = 'Error.......'
		return render(request, 'home.html', {'api': api})
	else:
		return render(request, 'home.html', {'ticker': 'Enter Tickert Symbol'})


def about(request):
	return render(request, 'about.html', {})


def add_stock(request):

	if request.method == "POST":
		form = StockForm(request.POST or None)
		if form.is_valid():
			form.save()
			messages.success(request, ('Stock has been added successfully'))
			return redirect('add_stock')
	else:
		ticker = Stock.objects.all()
		ticker_output = []
		for ticker_item in ticker:
			api_request = requests.get(f'https://cloud.iexapis.com/stable/stock/{str(ticker_item)}/quote?token=pk_24ff01ef02954ffc9459e06ddc72dac8')

			try:
				api = json.loads(api_request.content)
				ticker_output.append(api)
			except Exception as e:
				api = 'Error.......'
		return render(request, 'add_stock.html', {'ticker': ticker, 'output': ticker_output})


def delete(request, stock_id):
	item = Stock.objects.get(pk=stock_id)
	item.delete()
	messages.success(request, ('Stock ticker has been deleted'))
	return redirect(delete_stock)


def delete_stock(request):
	ticker = Stock.objects.all()
	return render(request, 'delete_stock.html', {'ticker': ticker})
