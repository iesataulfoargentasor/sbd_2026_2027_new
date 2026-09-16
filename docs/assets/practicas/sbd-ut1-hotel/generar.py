"""Generar fuentes sintéticas; una copia contiene seis reservas y ocho eventos."""
import argparse, csv, json
from pathlib import Path
p=argparse.ArgumentParser()
p.add_argument('--salida',required=True)
p.add_argument('--copias',type=int,default=1)
a=p.parse_args()
if a.copias<1:p.error('copias debe ser positivo')
r=Path(a.salida);r.mkdir(parents=True,exist_ok=False)
base=[(1,'web',3,'300.00'),(1,'ota',2,'180.00'),(1,'web',1,'100.00'),(2,'web',3,'400.00'),(2,'ota',4,'480.00'),(2,'web',2,'200.00')]
with (r/'hoteles.csv').open('w',newline='',encoding='utf-8') as f:
 w=csv.writer(f);w.writerow(['id_hotel','hotel','localidad']);w.writerows([(1,'Laredo','Laredo'),(2,'Potes','Potes')])
with (r/'reservas.csv').open('w',newline='',encoding='utf-8') as f,(r/'eventos.jsonl').open('w',encoding='utf-8') as e:
 w=csv.writer(f);w.writerow(['id_reserva','id_hotel','canal','fecha','noches','importe'])
 eid=0
 for copia in range(a.copias):
  for pos,(hotel,canal,noches,importe) in enumerate(base,1):
   rid=copia*6+pos
   w.writerow([rid,hotel,canal,'2026-09-01',noches,importe])
   for tipo in (['confirmacion','cancelacion'] if pos in (2,6) else ['confirmacion']):
    eid+=1;e.write(json.dumps(dict(id_evento=eid,id_reserva=rid,tipo=tipo,detalle={'origen':'simulador'}))+'\n')
(r/'origen.json').write_text(json.dumps({'sinteticos':True,'copias':a.copias,'regla_cancelacion':'existencia de evento; sin reapertura'},indent=2)+'\n')
print(f'{6*a.copias} reservas; {8*a.copias} eventos; {r}')
