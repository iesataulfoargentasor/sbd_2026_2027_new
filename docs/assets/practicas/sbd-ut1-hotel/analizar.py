"""Pipeline de RA1: validar, relacionar, agregar y escribir sin sobrescribir."""
import argparse,json,time
from pathlib import Path
from pyspark.sql import SparkSession,functions as F
RESERVAS='id_reserva long, id_hotel int, canal string, fecha date, noches int, importe decimal(12,2)'
HOTELES='id_hotel int, hotel string, localidad string'
EVENTOS='id_evento long, id_reserva long, tipo string, detalle struct<origen:string>'
def validar(df,campos,clave,nombre):
 for c in campos:
  if df.filter(F.col(c).isNull()).limit(1).count():raise ValueError(f'{nombre}: nulo en {c}')
 if df.groupBy(clave).count().filter('count > 1').limit(1).count():raise ValueError(f'{nombre}: clave duplicada {clave}')
def ejecutar(entrada,salida,master='local[2]',catalogo=None):
 t=time.perf_counter();base=Path(entrada);out=Path(salida)
 if out.exists():raise FileExistsError(out)
 out.mkdir(parents=True)
 spark=SparkSession.builder.master(master).appName('SBD-hotel-RA1').config('spark.sql.shuffle.partitions','2').getOrCreate()
 spark.sparkContext.setLogLevel('ERROR')
 try:
  r=spark.read.schema(RESERVAS).option('header',True).option('mode','FAILFAST').csv(str(base/'reservas.csv'))
  h=spark.read.schema(HOTELES).option('header',True).option('mode','FAILFAST').csv(str(catalogo or base/'hoteles.csv'))
  e=spark.read.schema(EVENTOS).option('mode','FAILFAST').json(str(base/'eventos.jsonl'))
  r=r.withColumn('canal',F.lower(F.trim('canal')))
  validar(r,r.columns,'id_reserva','reservas');validar(h,h.columns,'id_hotel','hoteles');validar(e,['id_evento','id_reserva','tipo'],'id_evento','eventos')
  if r.filter((F.col('noches')<=0)|(F.col('importe')<0)|(~F.col('canal').isin('web','ota'))).limit(1).count():raise ValueError('reservas: valor fuera de dominio')
  if e.filter(~F.col('tipo').isin('confirmacion','cancelacion')).limit(1).count():raise ValueError('eventos: tipo desconocido')
  if r.join(h,'id_hotel','left_anti').limit(1).count():raise ValueError('reservas: hotel desconocido')
  if e.join(r,'id_reserva','left_anti').limit(1).count():raise ValueError('eventos: reserva desconocida')
  c=e.filter(F.col('tipo')=='cancelacion').select('id_reserva').distinct().withColumn('cancelada',F.lit(1))
  integrado=r.join(h,'id_hotel','left').join(c,'id_reserva','left').fillna({'cancelada':0})
  n=r.count();ni=integrado.count()
  if n!=ni:raise ValueError('Integración multiplicó o perdió reservas')
  total=r.agg(F.sum('importe')).first()[0]
  if total!=integrado.agg(F.sum('importe')).first()[0]:raise ValueError('El importe no se conserva')
  resumen=integrado.groupBy('hotel','canal').agg(F.count('*').alias('reservas'),F.sum('noches').alias('noches'),F.sum('importe').alias('importe'),F.sum('cancelada').alias('canceladas')).withColumn('tasa_cancelacion',F.round(F.col('canceladas')/F.col('reservas'),4))
  integrado.write.mode('errorifexists').parquet(str(out/'integrado'))
  resumen.orderBy('hotel','canal').write.mode('errorifexists').option('header',True).csv(str(out/'resumen'))
  entradas=[base/'reservas.csv',base/'eventos.jsonl',Path(catalogo) if catalogo else base/'hoteles.csv']
  metrics=dict(reservas=n,eventos=e.count(),filas_integradas=ni,importe_nominal=str(total),bytes_entrada=sum(f.stat().st_size for f in entradas),segundos=time.perf_counter()-t,master=spark.sparkContext.master,spark=spark.version,controles='superados')
  (out/'metricas.json').write_text(json.dumps(metrics,indent=2)+'\n')
  print(json.dumps(metrics,indent=2))
 finally:spark.stop()
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--entrada',required=True);p.add_argument('--salida',required=True);p.add_argument('--master',default='local[2]');p.add_argument('--catalogo');a=p.parse_args();ejecutar(a.entrada,a.salida,a.master,a.catalogo)
