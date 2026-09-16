"""Ensayo finito de dos llegadas: memoria como salida exclusivamente didáctica."""
import argparse,json,shutil,time
from pathlib import Path
from pyspark.sql import SparkSession
from analizar import EVENTOS
p=argparse.ArgumentParser();p.add_argument('--entrada',required=True);p.add_argument('--trabajo',required=True);a=p.parse_args()
r=Path(a.trabajo);r.mkdir(parents=True,exist_ok=False);inbox=r/'entrada';inbox.mkdir()
spark=SparkSession.builder.master('local[2]').appName('SBD-eventos').config('spark.sql.shuffle.partitions','2').getOrCreate();spark.sparkContext.setLogLevel('ERROR')
q=None
try:
 flujo=spark.readStream.schema(EVENTOS).json(str(inbox))
 q=flujo.groupBy('tipo').count().writeStream.outputMode('complete').format('memory').queryName('conteo_eventos').option('checkpointLocation',str(r/'checkpoint')).start()
 pruebas=[];acumulado={}
 for tipo in ['confirmacion','cancelacion']:
  inicio=time.perf_counter();temporal=r/(tipo+'.json');cuantos=0
  with Path(a.entrada,'eventos.jsonl').open() as fuente,temporal.open('w') as dest:
   for line in fuente:
    evento=json.loads(line)
    if evento['tipo']==tipo:dest.write(line);cuantos+=1
  # Publicación completa por renombrado en el mismo sistema de ficheros.
  temporal.rename(inbox/temporal.name)
  q.processAllAvailable()
  filas={row['tipo']:row['count'] for row in spark.sql('SELECT * FROM conteo_eventos').collect()}
  acumulado[tipo]=cuantos
  assert filas==acumulado,(filas,acumulado)
  pruebas.append(dict(lote=tipo,conteos=filas,segundos=time.perf_counter()-inicio))
 (r/'evidencias.json').write_text(json.dumps(pruebas,indent=2)+'\n');print(json.dumps(pruebas,indent=2))
finally:
 if q:q.stop()
 spark.stop()
