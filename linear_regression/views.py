from django.shortcuts import render
from linear_regression.predict import predict_model

# Create your views here.


def lr_home(request):
    #import pdb; pdb.set_trace()
    if len(request.GET.keys()) == 0:
        return render(request,'linear_regression/predict.html')
    else:
        prediction = predict_model.get_equation(request)
        plot = predict_model.get_plot(request)
        return render(request,'linear_regression/predict.html', {'prediction':prediction, 'plot':plot})