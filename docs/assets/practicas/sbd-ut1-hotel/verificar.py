"""Comparar el resultado con expectativas calculadas sobre las seis reservas."""
import argparse,csv,json
from pathlib import Path
from decimal import Decimal
p=argparse.ArgumentParser();p.add_argument('salida');p.add_argument('--copias',type=int,default=1);a=p.parse_args()
r=Path(a.salida);actual={}
for f in (r/'resumen').glob('part-*.csv'):
 with f.open() as stream:
  for row in csv.DictReader(stream):
   key=(row['hotel'],row['canal']);assert key not in actual,'Grupo duplicado';actual[key]=row
esperado={('Laredo','ota'):(1,2,180,1),('Laredo','web'):(2,4,400,0),('Potes','ota'):(1,4,480,0),('Potes','web'):(2,5,600,1)}
assert set(actual)==set(esperado)
for key,values in esperado.items():
 row=actual[key]
 for field,value in zip(['reservas','noches','importe','canceladas'],values):assert Decimal(row[field])==value*a.copias,(key,field,row[field])
 assert abs(Decimal(row['tasa_cancelacion'])-Decimal(values[3])/values[0])<=Decimal('0.00005')
m=json.loads((r/'metricas.json').read_text());assert m['reservas']==6*a.copias and m['eventos']==8*a.copias and m['filas_integradas']==6*a.copias
print('Resultado verificado: grupos, reservas, noches, importes, cancelaciones y proporciones.')
