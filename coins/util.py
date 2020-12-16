import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
import plotly.io as plio
from datetime import datetime , timedelta, time
import pytz

def convert_time(milliseconds, tz = pytz.timezone('America/Chicago')):
	return datetime.fromtimestamp(milliseconds/1e3,tz = tz)

def candles_to_html(DF):
	df = DF.copy()
	df.reset_index(inplace = True)

	fig = go.Figure(data=[go.Candlestick(x=df['Time'],
		open=df['Open'],
		high=df['High'],
		low=df['Low'],
		close=df['Close'])])

	config = dict(scrollZoom = False,displayModeBar= False)
	fig.layout.dragmode = 'pan'#change defauly to pan instead of zoom
	#fig.layout.template = 'plotly_dark'#dark mode, fam
	fig.layout.xaxis.range = [df['Time'][0], df['Time'][len(df)-1] + timedelta(minutes = 10)]
	fig.layout.yaxis.showgrid=False
	fig.layout.xaxis.showgrid=False
	fig.layout.height = 200
	fig.layout.margin.l = 30
	fig.layout.margin.r = 10
	fig.layout.margin.t = 10
	fig.layout.margin.b = 10

	fig.update_layout(legend=dict(
    yanchor="top",
    y=0.99,
    xanchor="left",
    x=0.01
	),
	paper_bgcolor='rgba(0,0,0,0)',
	plot_bgcolor='rgba(0,0,0,0)',
	title_font_color="white",
	font_color="white"
	)
	fig.layout.yaxis.showgrid=False
	fig.layout.yaxis.mirror=True
	fig.layout.yaxis.ticks='outside'
	fig.layout.yaxis.showline=True
	fig.layout.xaxis.showgrid=False
	fig.layout.xaxis.mirror=True
	fig.layout.xaxis.ticks='outside'
	fig.layout.xaxis.showline=True
	fig.layout.yaxis.fixedrange = True
	fig.layout.xaxis.fixedrange = True
	fig.update_layout(xaxis_rangeslider_visible=False)
	return plio.to_html(fig,full_html=False, config = config)

