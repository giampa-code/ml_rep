# import used libraries
import joblib
from sklearn.linear_model import Ridge
import numpy as np
import antropo.utils.utils as utils
import os

dirname = os.path.dirname(__file__)


''
# load female models
model_residual_f = joblib.load(os.path.join(dirname,'../data/trained/f/masa_residual_f.sav'))
model_piel_f = joblib.load(os.path.join(dirname,'../data/trained/f/masa_piel_f.sav'))
model_osea_f = joblib.load(os.path.join(dirname,'../data/trained/f/masa_osea_f.sav'))
model_adiposa_f = joblib.load(os.path.join(dirname,'../data/trained/f/masa_adiposa_f.sav'))
model_muscular_f = joblib.load(os.path.join(dirname,'../data/trained/f/masa_muscular_f.sav'))

# load male models
model_residual_m = joblib.load(os.path.join(dirname,'../data/trained/m/masa_residual_m.sav'))
model_piel_m = joblib.load(os.path.join(dirname,'../data/trained/m/masa_piel_m.sav'))
model_osea_m = joblib.load(os.path.join(dirname,'../data/trained/m/masa_osea_m.sav'))
model_adiposa_m = joblib.load(os.path.join(dirname,'../data/trained/m/masa_adiposa_m.sav'))
model_muscular_m = joblib.load(os.path.join(dirname,'../data/trained/m/masa_muscular_m.sav'))



sample_m = {'peso':97.5, 'talla':169, 'per_brazo_rel':38, 
      'per_brazo_ten':41.8, 'per_antebrazo':31.2,'per_torax':116, 
      'per_cintura':97, 'per_cadera':109.4, 'per_muslo_max':61,
      'per_muslo_medial':57, 'per_pantorrilla':38.5}

    
# predictions functions per sex

def get_data(request):
   """
   Extract the data from the request.
   """

   keys = ['sexo','peso', 'talla', 'per_brazo_rel', 
      'per_brazo_ten', 'per_antebrazo','per_torax', 
      'per_cintura', 'per_cadera', 'per_muslo_max',
      'per_muslo_medial', 'per_pantorrilla']

   sample = dict()
   for key in keys:
      if key == 'sexo':
         sample[key] = request.GET[key]
      else:
         sample[key] = float(request.GET[key])

   return sample

def predict_male(sample):
   """
   Receive a dict with the following keys: 
      ['peso', 'talla', 'per_brazo_rel', 
      'per_brazo_ten', 'per_antebrazo','per_torax', 
      'per_cintura', 'per_cadera', 'per_muslo_max',
      'per_muslo_medial', 'per_pantorrilla']
   First the values are z-scaled and then make the prediction.
   Return a dict of masa residual, piel, osea, adiposa y muscular. 
   """
   
   # remove key sexo
   sample.pop('sexo',None)

   # scale and reshape data
   sample_scaled = {k:utils.z_scale(k,'m',v) for (k,v) in zip(sample.keys(),sample.values())}
   sample_scaled = np.array(list(sample_scaled.values())).reshape(1, -1)

   # predict
   masa_residual = model_residual_m.predict(sample_scaled)
   masa_piel = model_piel_m.predict(sample_scaled)
   masa_osea = model_osea_m.predict(sample_scaled)
   masa_adiposa = model_adiposa_m.predict(sample_scaled)
   masa_muscular = model_muscular_m.predict(sample_scaled)

   masas_dict = {'residual':round(float(masa_residual),2),'piel':round(float(masa_piel),2),
               'osea':round(float(masa_osea),2),'adiposa':round(float(masa_adiposa),2),'muscular':round(float(masa_muscular),2),
               }
   return masas_dict

def predict_female(sample):
   """
   Receive a dict with the following keys: 
      ['peso', 'talla', 'per_brazo_rel', 
      'per_brazo_ten', 'per_antebrazo','per_torax', 
      'per_cintura', 'per_cadera', 'per_muslo_max',
      'per_muslo_medial', 'per_pantorrilla']
   First the values are z-scaled and then make the prediction.
   Return a dict of masa residual, piel, osea, adiposa y muscular. 
   """
   
   # remove key sexo
   sample.pop('sexo',None)

   # scale and reshape 
   sample_scaled = {k:utils.z_scale(k,'m',v) for (k,v) in zip(sample.keys(),sample.values())}
   sample_scaled = np.array(list(sample_scaled.values())).reshape(1, -1)

   # predicts
   masa_residual = model_residual_f.predict(sample_scaled)
   masa_piel = model_piel_f.predict(sample_scaled)
   masa_osea = model_osea_f.predict(sample_scaled)
   masa_adiposa = model_adiposa_f.predict(sample_scaled)
   masa_muscular = model_muscular_f.predict(sample_scaled)

   masas_dict = {'residual':round(float(masa_residual),2),'piel':round(float(masa_piel),2),
               'osea':round(float(masa_osea),2),'adiposa':round(float(masa_adiposa),2),'muscular':round(float(masa_muscular),2),
               }
   return masas_dict


import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg
import uuid, base64
from io import BytesIO
from matplotlib import pyplot as plt


# funciones sacadas de internet para plotear 
def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph

def get_plot(masas):

   osea = masas['osea']
   piel = masas['piel']
   muscular = masas['muscular']
   adiposa = masas['adiposa']
   residual = masas['residual']

    
    
   
   plt.switch_backend('AGG')

   figure = plt.figure(figsize=(5,5))
   plt.pie(masas.values(), labels=masas.keys(), autopct='%1.1f%%')
   plt.title('Body mass')
   #plt.plot(xs,ys,'g')
   plt.legend()

   plt.tight_layout()
   plot = get_graph()
   return plot