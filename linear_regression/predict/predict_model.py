# import used libraries
from cProfile import label
import joblib
from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg
from sklearn.metrics import r2_score

from django.http import HttpResponse


def get_equation(request):
    """
    Given 4 x and y coordinates, fit the LR model
    """
    x1 = float(request.GET['x1'])
    x2 = float(request.GET['x2'])
    x3 = float(request.GET['x3'])
    x4 = float(request.GET['x4'])
    y1 = float(request.GET['y1'])
    y2 = float(request.GET['y2'])
    y3 = float(request.GET['y3'])
    y4 = float(request.GET['y4'])

    # convert model into the proper arrays
    X = np.array([x1,x2,x3,x4]).reshape(-1,1)
    y = np.array([y1,y2,y3,y4]).reshape(-1,1)

    # model fit
    model = LinearRegression().fit(X,y)
    a  = round(float(model.coef_),2)
    b = round(float(model.intercept_),2)
    equation = 'y = '+ str(a) + '*x + ' + str(b)

    return equation

import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg
import uuid, base64
from io import BytesIO
from matplotlib import pyplot


# funciones sacadas de internet para plotear 
def get_graph():
    buffer = BytesIO()
    pyplot.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph

def get_plot(request):

    x1 = float(request.GET['x1'])
    x2 = float(request.GET['x2'])
    x3 = float(request.GET['x3'])
    x4 = float(request.GET['x4'])
    y1 = float(request.GET['y1'])
    y2 = float(request.GET['y2'])
    y3 = float(request.GET['y3'])
    y4 = float(request.GET['y4'])


    # convert model into the proper arrays
    X = np.array([x1,x2,x3,x4]).reshape(-1,1)
    y = np.array([y1,y2,y3,y4]).reshape(-1,1)

    # model fit
    model = LinearRegression().fit(X,y)
    
    

    Xp = [x1,x2,x3,x4]
    yp = [y1,y2,y3,y4]

    # to plot the trend line
    xs = [min(Xp), max(Xp)]
    ys = [float(model.predict([[min(Xp)]])),float(model.predict([[max(Xp)]]))]

    pyplot.switch_backend('AGG')

    r2 = r2_score(X,y)
    figure = plt.figure(figsize=(5,5))
    plt.plot(Xp,yp,'bo',label=(f'R2 = {round(r2,2)}'))
    plt.title('Regression')
    plt.plot(xs,ys,'g')
    plt.legend()

    pyplot.tight_layout()
    plot = get_graph()
    return plot

