import requests
import sys
import pandas as pd


def controla(csv_file):
    df = pd.read_csv(csv_file, index_col=0)
    df.columns = ['estatus', 'channel-id', 'tvg-id',
                  'tvg-logo', 'group-title', 'nombre', 'url', 'a']
    df2 = pd.DataFrame()
    #df['estatus'] = df['estatus'].replace({0: 1})
    w = 0
    print(df)
    for index, row in df.iterrows():
        try:
            w = w+1
            if "/mpegts" in row['url']:
                pass
            else:
                resultado = requests.get(
                    row['url'].replace('url=', '').replace("\n", ""),  timeout=0.8)
                row['estatus'] = resultado.status_code
                nueva_fila = pd.Series(row, index=df.columns)
                df2 = df2.append(nueva_fila, ignore_index=True)
                print(str(index)+" , "+str(resultado.status_code) +
                      ", " + row['url'].replace("\n", "") + "\n")
            if w == 20000:
                break
            print(w)
        except:
            row['estatus'] = "1000"

    df2.to_csv(csv_file, index=False)
