from ast import Try
from types import TracebackType
import requests
resultado = ['channel-id="x"', 'tvg-id="x"', 'tvg-logo="x"',
                 'group-title="x"', 'nombre=x', 'url="x"']
resultado_csv = ['x', 'x', 'x','x', 'x', '']

def extrae(t, b):
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
    titulos = ['channel-id', 'tvg-id', 'tvg-logo',
               'group-title']
    
    #linea = linea.lower()
    linea = linea.replace(' channelId=', ' channel-id=')
    linea = linea.replace(' channelid=', ' channel-id=')
    linea = linea.replace(' id=', ' tvg-id=')
    linea = linea.replace(' name=', ' tvg-name=')
    linea = linea.replace(' logo=', ' tvg-logo=')
    linea = linea.replace(' grupo=', ' group-title=')
    try:
        # print(linea+'\n')

        # print(linea[0:7]+'\n')
        if linea[0:7] == "#EXTINF":
            p1 = linea.split((','))
            nombre = p1[1].replace('\n', '').strip(' \n_')
            p2 = p1[0].split((' '))
            # print('limpia')

            i = 0
            for ti in titulos:
                rr = extrae(linea, ti.replace('"x"', ''))
                if rr != None:
                    if tipo=='m3u':
                        resultado[i] = ti+"="+rr
                    else:
                        resultado_csv[i] = rr.replace('"','')
                i = i+1
            resultado[4] = nombre

        elif linea[0: 7] == "#EXTM3U":
            pass
        elif linea[0: 4] == "http":
            #print(linea.replace('\n', ''))
            resultado[5] = linea.replace('\n', '')

        return resultado
    except:
        resultado


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
                            
                        ht = requests.get(resultado[5],  timeout=0.5)
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
    m3u_dat = []
    
    f = open(arch, 'r', encoding="utf8")

    for linea in f:
        try:
            resultado = procesa_linea_m3u_sucia(linea, 'm3u')
            resultado_csv = procesa_linea_m3u_sucia(linea, 'csv')

            if resultado[5] == 'url="x"' or resultado[5] == '':
                pass
            else:
                texto_m3u='#EXTINF:-1 '
                t=0
                for u in resultado:
                    
                    if t==5:
                        texto_m3u=texto_m3u+u.replace('http','\nhttp')
                    else:
                        texto_m3u=texto_m3u+u+' '
                    t=t+1
                m = open('n_'+arch, 'a', encoding="utf8")
                m.write(texto_m3u+'\n')
                m.close()
                texto_csv=''
               
                for u in resultado_csv:
                    texto_csv=(texto_csv+u)+' ,'
                    
                c = open('n_'+arch.replace('m3u8','csv').replace('m3u','csv'), 'a', encoding="utf8")
                c.write(texto_csv.strip(', ')+'\n')
                c.close()
               
        except BaseException as err:
            print(f"Unexpected {err=}, {type(err)=}")
            
            resultado = ['channel-id="x"', 'tvg-id="x"', 'tvg-logo="x"',
                                 'group-title="x"', 'nombre=x', 'url="x"']

    f.close()
# print(recorre_m2u_original('r1.m3u8'))
