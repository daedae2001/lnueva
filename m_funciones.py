import requests


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


def procesa_linea_m3u_sucia(linea, resultado):
    titulos = ['channel-id', 'tvg-id', 'tvg-logo',
               'group-title']
    linea = linea.lower()
    linea = linea.replace(' channelid=', ' channel-id=')
    linea = linea.replace(' id=', ' tvg-id=')
    linea = linea.replace(' name=', ' tvg-name=')
    linea = linea.replace(' logo=', ' tvg-logo=')
    linea = linea.replace(' grupo=', ' group-title=')
    try:
        # print(linea+'\n')

        # print(linea[0:7]+'\n')
        if linea[0:7] == "#extinf":
            p1 = linea.split((','))
            nombre = p1[1].replace('\n', '')
            p2 = p1[0].split((';'))
            # print('limpia')

            i = 0
            for ti in titulos:
                rr = extrae(linea, ti.replace('"x"', ''))
                if rr != None:
                    resultado[i] = ti+"="+rr
                i = i+1
            resultado[4] = nombre

        elif linea[0: 7] == "#extm3u":
            pass
        elif linea[0: 4] == "http":
            #print(linea.replace('\n', ''))
            resultado[5] = linea.replace('\n', '')

        return resultado
    except:
        resultado


def recorre_m2u_original(arch):
    m3u_dat = []
    resultado = ['channel-id="x"', 'tvg-id="x"', 'tvg-logo="x"',
                 'group-title="x"', 'nombre=x', 'url="x"']
    f = open(arch, 'r', encoding="utf8")

    for linea in f:
        try:
            resultado = procesa_linea_m3u_sucia(linea, resultado)

            if resultado[5] == 'url="x"' or resultado[5] == None:
                pass
            else:
                try:
                    print(resultado[5])
                    ht = requests.get(resultado[5],  timeout=0.1)
                    print(ht.headers)
                    if ht.status_code < 300:
                        m3u_dat.append(resultado)
                    else:
                        resultado = ['channel-id="x"', 'tvg-id="x"', 'tvg-logo="x"',
                                     'group-title="x"', 'nombre=x', 'url="x"']
                except requests.exceptions.ConnectionError as ex:
                    m3u_dat.append(resultado)
                except requests.exceptions.ReadTimeout as ex:
                    resultado = ['channel-id="x"', 'tvg-id="x"', 'tvg-logo="x"',
                                 'group-title="x"', 'nombre=x', 'url="x"']

        except:
            pass

    f.close()
    return m3u_dat


# print(recorre_m2u_original('r1.m3u8'))
