# Python2
import os
from tqdm import tqdm
import numpy as np
import json
import requests
import pickle
from tensorboardX import SummaryWriter

alldata = {}

if os.path.exists('result.pkl'):
    with open('result.pkl', 'rb') as f:
        alldata = pickle.load(f)
else:
    s = requests.Session()
    for _, _, files in os.walk('.'):
        for name in tqdm(sorted(files)):
            if name[-3:] == 'jpg':
                with open(name, 'rb') as f:
                    r = s.post('https://sandbox.api.sap.com/ml/imagefeatureextraction/feature-extraction', files={'files': f}, headers={'apikey':'fhGKsGZAzwCFjVkRAijRnQRuslYaHVaw'})
                resp = json.loads(r.text)
                alldata[name] = resp['predictions'][0]['featureVectors']

    with open('result.pkl', 'wb') as f:
        pickle.dump(alldata, f)

if not os.path.exists('./runs'):
    os.mkdir('./runs')

writer = SummaryWriter(os.path.join('runs', 'data'))
writer.add_embedding(np.array(alldata.values()), metadata=alldata.keys())

