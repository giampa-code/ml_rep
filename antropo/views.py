from django.shortcuts import render
from antropo.predict import predict_model

# Create your views here.

def antropo_home(request):
    #import pdb; pdb.set_trace()
    if len(request.GET.keys()) == 0:
        return render(request,'antropo/predict.html')
    else:
        try:
            sample = predict_model.get_data(request)
            if sample['sexo'] == 'f':
                prediction = predict_model.predict_female(sample)
            if sample['sexo'] == 'm':
                prediction = predict_model.predict_male(sample)
            plot = predict_model.get_plot(prediction)
            error = False
        except:
            error = True
            plot = None
        #import pdb; pdb.set_trace()
        return render(request,'antropo/predict.html', {'plot':plot, 'error':error})