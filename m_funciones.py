from ast import Try
from types import TracebackType
import requests
resultado = ['channel-id="x"', 'tvg-id="x"', 'tvg-logo="x"',
                 'group-title="x"', 'nombre=x', 'url="x"']
resultado2 = ['channel-id="x"', 'tvg-id="x"', 'tvg-logo="x"',
                 'group-title="x"', 'nombre=x', 'url="x"']
resultado_csv = ['"x"', '"x"', '"x"','"x"', '"x"', '"nn"']
titulos = ['channel-id', 'tvg-id', 'tvg-logo',
            'group-title']
    

def extrae(t, b):
    """
    b
    'channel-id'
    t
    '#EXTINF:-1 channel-id="canalsamsum"  tvg-id="samsung1"  
    tvg-logo="https://img.rtve.es/imagenes/multisenal-24/1361962728583.png" 
     group-title="10_Noticias"  ,canal se samsung 1\n'"""
    f = '"'
    try:
        esta = t.find(b)

        if esta >= 0:
            inicio = t.find(b)+len(b)+1
            fin = t.find(f, inicio+1)+1
            r = t[inicio: fin]
            return r
        else:
            pass
    except:
        r = '"x"'
        return r


def procesa_linea_m3u_sucia(linea ,  tipo='m3u'):
    """
    linea
    '#EXTINF:-1 channelId="canalsamsum"  tvg-id="samsung1" 
        tvg-logo="https://img.rtve.es/imagenes/multisenal-24/1361962728583.png" 
        group-title="10_Noticias"  ,canal se samsung 1\n'
    """
 
    #linea = linea.lower()
  

    """
    linea
    '#EXTINF:-1 channel-id="canalsamsum"  tvg-id="samsung1"  
    tvg-logo="https://img.rtve.es/imagenes/multisenal-24/1361962728583.png"  
    group-title="10_Noticias"  ,canal se samsung 1\n'
    """


def recorre_m2u_original(arch):

    m3u_dat = []

    f = open(arch, 'r', encoding="utf8")

    for linea in f:
        try:
            resultado = procesa_linea_m3u_sucia(linea, resultado,'m3u')
            #resultado_csv = procesa_linea_m3u_sucia(linea, resultado,'csv')

            if resultado[5] == 'url="x"' or resultado[5] == None:
                pass
            else:
                try:
                    if "mpegts?" in resultado[5]:
                        m3u_dat.append(resultado)
                    
                    else:
                            
                        
                        print(ht.headers)
                        if "video/mp2t" in ht.headers:
                            pass
                        else:
                            
                            if ht.status_code!=9999:
                                m3u_dat.append(resultado)
                            else:
                                resultado = ['channel-id="x"', 'tvg-id="x"', 'tvg-logo="x"',
                                            'group-title="x"', 'nombre=x', 'url="x"']
                except requests.exceptions.ConnectionError as ex:
                    resultado = ['channel-id="x"', 'tvg-id="x"', 'tvg-logo="x"',
                                 'group-title="x"', 'nombre=x', 'url="x"']
                                 #m3u_dat.append(resultado)
                except requests.exceptions.ReadTimeout as ex:
                    resultado = ['channel-id="x"', 'tvg-id="x"', 'tvg-logo="x"',
                                 'group-title="x"', 'nombre=x', 'url="x"']

        except:
            pass

    f.close()
    return m3u_dat

def recorre_m2u_original2(arch):

    #arch = 'lista_controladan1.m3u8'

    #ht = requests.get(resultado[5],  timeout=0.5)
    f = open(arch, 'r', encoding="utf8")

    for linea in f:
        linea = linea.replace(' channelId=', ' channel-id=')
        linea = linea.replace(' channelid=', ' channel-id=')
        linea = linea.replace(' id=', ' tvg-id=')
        linea = linea.replace(' name=', ' tvg-name=')
        linea = linea.replace(' logo=', ' tvg-logo=')
        linea = linea.replace(' grupo=', ' group-title=')
        """
        linea
        '#EXTINF:-1 channel-id="canalsamsum"  tvg-id="samsung1" 
         tvg-logo="https://img.rtve.es/imagenes/multisenal-24/1361962728583.png" 
          group-title="10_Noticias"  ,canal se samsung 1\n'

        """
        try:
            if linea[0:7] == "#EXTINF":
                p1 = linea.split((','))
                """
                ['#EXTINF:-1 channel-id="canalsamsum"  tvg-id="samsung1"  
                tvg-logo="https://img.rtve.es/imagenes/multisenal-24/1361962728583.png" 
                group-title="10_Noticias"  ', 'canal se samsung 1\n']
                """
                nombre = p1[1].replace('\n', '').strip(' \n_')

                p2 = p1[0].split((' '))
                """
                ['#EXTINF:-1', 'channel-id="canalsamsum"', '', 'tvg-id="samsung1"', '',
                'tvg-logo="https://img.rtve.es/imagenes/multisenal-24/1361962728583.png"', 
                '', 'group-title="10_Noticias"', '', '']
                """
                i = 0
                for ti in titulos:
                    rr = extrae(linea, ti.replace('"x"', ''))
                    if rr != None:
                       resultado[i] = ti+"="+rr
                    i = i+1
                resultado[4] = nombre
            elif linea[0: 4] == "http":
                    #print(linea.replace('\n', ''))
                    resultado[5] = linea.replace('\n', '')
            #resultado_csv = procesa_linea_m3u_sucia(linea, 'csv')
            else:
                pass
            if resultado[5] == 'url="x"' or resultado[5] == '':
                pass
            else:
                texto_m3u='#EXTINF:-1 '
                t=0
                for u in resultado:
                    
                    if t==5:
                        texto_m3u=texto_m3u+u.replace('http','\nhttp')
                    if t==4:
                        texto_m3u=texto_m3u+' ,'+u
                            
                    else:
                        texto_m3u=texto_m3u+u+' '
                    t=t+1
                #m = open('n_'+arch, 'r', encoding="utf8")
                if texto_m3u!='':
                    q=texto_m3u+'\n'
                    texto_m3u=''
                    #m.close()
                    m = open('n_'+arch, 'a', encoding="utf8")
                    m.write(q)
                    resultado=resultado2
                    q=''
                    m.close()
                else:
                    pass

                """
                for u in resultado_csv:
                    texto_csv=(texto_csv+u)+' ,'
                    
                c = open('n_'+arch.replace('m3u8','csv').replace('m3u','csv'), 'a', encoding="utf8")
                c.write(texto_csv.strip(', ')+'\n')
                c.close()
                """
        except BaseException as err:
            print(f"Unexpected {err=}, {type(err)=}")
            
            resultado = ['channel-id="x"', 'tvg-id="x"', 'tvg-logo="x"',
                                 'group-title="x"', 'nombre=x', 'url="x"']

    f.close()
# print(recorre_m2u_original('r1.m3u8'))
