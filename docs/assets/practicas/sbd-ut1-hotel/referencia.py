"""Referencia independiente pequeña con biblioteca estándar. No usar a gran escala."""
import csv,json,sys
from decimal import Decimal
from pathlib import Path
r=Path(sys.argv[1])
with (r/'hoteles.csv').open() as f:hoteles={h['id_hotel']:h['hotel'] for h in csv.DictReader(f)}
with (r/'eventos.jsonl').open() as f:canceladas={str(e['id_reserva']) for e in map(json.loads,f) if e['tipo']=='cancelacion'}
res={}
with (r/'reservas.csv').open() as f:
 for row in csv.DictReader(f):
  k=(hoteles[row['id_hotel']],row['canal'].strip().lower())
  v=res.setdefault(k,dict(reservas=0,noches=0,importe=Decimal(0),canceladas=0))
  v['reservas']+=1;v['noches']+=int(row['noches']);v['importe']+=Decimal(row['importe']);v['canceladas']+=row['id_reserva'] in canceladas
for k,v in sorted(res.items()):print(k,v)
