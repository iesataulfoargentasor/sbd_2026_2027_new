"""Exportar catálogo desde MongoDB; conexión mediante MONGO_URI del entorno."""
import argparse,csv,os
from pymongo import MongoClient
p=argparse.ArgumentParser();p.add_argument('--base',required=True);p.add_argument('--coleccion',required=True);p.add_argument('--salida',required=True);a=p.parse_args()
with MongoClient(os.environ['MONGO_URI'],serverSelectionTimeoutMS=5000) as cliente:
 with open(a.salida,'x',newline='',encoding='utf-8') as f:
  w=csv.DictWriter(f,fieldnames=['id_hotel','hotel','localidad']);w.writeheader()
  for doc in cliente[a.base][a.coleccion].find({},dict(_id=0,id_hotel=1,hotel=1,localidad=1)):
   if any(k not in doc or doc[k] is None for k in w.fieldnames):raise ValueError('Documento incompleto')
   w.writerow(doc)
