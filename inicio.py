import m_descarga
import m_crea_csv_sucio
import m_une_csvs
import m_crea_csv_todo_limpio
import m_control_urls
import m_crea_m3u
import m_funciones
"""
mylist = [["1.m3u8", 'https://raw.githubusercontent.com/daedae2001/lista/main/tv21.m3u', ''],
          ["1.m3u8", 'https://github.com/daedae2001/lista/raw/main/r1.m3u8', ''],
          ["1.m3u8", 'https://raw.githubusercontent.com/daedae2001/lista/main/lista1x.m3u', ''],
          ["1.m3u8", 'https://raw.githubusercontent.com/daedae2001/lista/main/ln.m3u', ''],
          ["1.m3u8", 'https://raw.githubusercontent.com/daedae2001/lista/main/nn.m3u', ''],
          ["1.m3u8", 'https://raw.githubusercontent.com/daedae2001/lista/main/nn2.m3u', ''],
          ["r1.m3u8", 'https://raw.githubusercontent.com/emiliocuesta/milista/7539e0504f56413d853dcc01ccaf978a531e64a9/lista12', '']]
"""

mylist = [["1.m3u8", 'https://raw.githubusercontent.com/daedae2001/lista/main/tv21.m3u', ''],
          ["2.m3u8", 'https://github.com/daedae2001/lista/raw/main/r1.m3u8', ''],
          ["3.m3u8", 'https://raw.githubusercontent.com/daedae2001/lista/main/lista1x.m3u', ''],
          ["4.m3u8", 'https://raw.githubusercontent.com/daedae2001/lista/main/ln.m3u', ''],
          ["5.m3u8", 'https://raw.githubusercontent.com/daedae2001/lista/main/nn.m3u', ''],
          ["6.m3u8", 'https://raw.githubusercontent.com/daedae2001/lista/main/nn2.m3u', ''],
          ["7.m3u8", 'https://raw.githubusercontent.com/emiliocuesta/milista/7539e0504f56413d853dcc01ccaf978a531e64a9/lista12', ''],
          ["8.m3u8", 'https://raw.githubusercontent.com/daedae2001/lnueva/master/l2.m3u', ''],
          ["9.m3u8", 'https://raw.githubusercontent.com/Malder21/win.m3u/main/Sin.m3u', '']]
i = 0
for x in mylist:
    i = i+1
    m_descarga.descarga(x[0], x[1], x[2])
    a = m_funciones.recorre_m2u_original2(x[0])
    # m_crea_csv_sucio.crea_csv_sucio(x[0])
    #import pandas as pd
    #df = pd.DataFrame(a)
    #df.to_csv(x[0].replace('m3u8', 'csv'), index=False)


