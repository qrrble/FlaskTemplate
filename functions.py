import io
import base64
import pickle
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from random import random

def PlottingFunction(n_points):
	# Generates a bunch of random values
	x_values = [random() for i in range(n_points)]
	y_values = [random() for i in range(n_points)]

	img = io.BytesIO()

	fig = plt.figure(figsize=(10,4))

	plt.plot(x_values, y_values,'ro')
	plt.grid(True)
	plt.savefig(img, format='png')
	img.seek(0)

	graph_url = base64.b64encode(img.getvalue()).decode()

	plt.close() 
	return 'data:image/png;base64,{}'.format(graph_url)





