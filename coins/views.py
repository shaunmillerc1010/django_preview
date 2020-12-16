from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
from .util import candles_to_html, convert_time


def home(request):
	mytext = 'This is just something I wrote'
	btc_df = pd.read_csv('coins/bittrex-btc-usd.csv')[-20:]
	btc_df['Time'] = btc_df['Time'].apply(convert_time)
	eth_df = pd.read_csv('coins/bittrex-eth-usd.csv')[-20:]
	eth_df['Time'] = eth_df['Time'].apply(convert_time)
	context = {
		'text': mytext,
		'btc_candles': str(candles_to_html(btc_df)),
		'eth_candles': str(candles_to_html(eth_df)),
	}
	return render(request, 'coins/index.html', context)

def about(request):
	return render(request, 'coins/about.html')
