import m_descarga
import m_crea_csv_sucio
import m_une_csvs
import m_crea_csv_todo_limpio
import m_control_urls
import m_crea_m3u
mylist = [["es.m3u8", 'https://i.mjh.nz/PlutoTV/es.m3u8', 'es'],
          ["mx.m3u8", 'https://i.mjh.nz/PlutoTV/mx.m3u8', 'mx'],
          ["r1.m3u8", 'https://raw.githubusercontent.com/emiliocuesta/milista/7539e0504f56413d853dcc01ccaf978a531e64a9/lista12', '']]
"""
mylist = [["es.m3u8", 'https://github.com/daedae2001/lista/raw/main/es.m3u8', 'es'],
          ["mx.m3u8", 'https://github.com/daedae2001/lista/raw/main/mx.m3u8', 'mx'],
          ["r1.m3u8", 'https://github.com/daedae2001/lista/raw/main/r1.m3u8', '']]
"""

for x in mylist:
    m_descarga.descarga(x[0], x[1], x[2])
    m_crea_csv_sucio.crea_csv_sucio(x[0])

li = []
for i in mylist:
    li.append(i[0])

m_une_csvs.une_csvs(li)
m_crea_csv_todo_limpio.crea_csv_todo_limpio("todo.csv")
m_control_urls.controla("todo.csv")
m_crea_m3u.crea_m3u("todo.csv")
