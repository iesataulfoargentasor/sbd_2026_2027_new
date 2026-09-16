"""Pruebas de negocio independientes y rechazo de datos corruptos."""
import subprocess,sys,tempfile,csv,json
from pathlib import Path
lab=Path('docs/assets/practicas/sbd-ut1-hotel').resolve()
def call(name,*args):
 subprocess.run([sys.executable,str(lab/name),*map(str,args)],check=True)
with tempfile.TemporaryDirectory() as tmp:
 r=Path(tmp)
 for copies in [1,2]:
  data=r/f'datos{copies}';out=r/f'salida{copies}'
  call('generar.py','--salida',data,'--copias',copies)
  call('analizar.py','--entrada',data,'--salida',out)
  call('verificar.py',out,'--copias',copies)
 call('streaming.py','--entrada',r/'datos1','--trabajo',r/'flujo')
 states=json.loads((r/'flujo/evidencias.json').read_text())
 assert states[0]['conteos']=={'confirmacion':6}
 assert states[1]['conteos']=={'confirmacion':6,'cancelacion':2}
 for error in ['duplicada','huerfana']:
  data=r/error;call('generar.py','--salida',data)
  f=data/'reservas.csv'
  with f.open() as stream:rows=list(csv.reader(stream))
  if error=='duplicada':rows.append(rows[1])
  else:rows[1][1]='999'
  with f.open('w',newline='') as stream:csv.writer(stream).writerows(rows)
  result=subprocess.run([sys.executable,str(lab/'analizar.py'),'--entrada',str(data),'--salida',str(r/(error+'_salida'))],text=True,capture_output=True)
  assert result.returncode!=0
  expected='clave duplicada' if error=='duplicada' else 'hotel desconocido'
  assert expected in result.stderr,result.stderr
print('PASS: resultados de 6/12 reservas, flujo 6→8 eventos y rechazo de duplicados/huérfanos')
