import m_une_csvs
li = ['n_1.m3u8',
      'n_2.m3u8',
      'n_3.m3u8',
      'n_4.m3u8',
      'n_5.m3u8',
      'n_6.m3u8',
      'n_7.m3u8',
      'n_8.m3u8',
      'n_9.m3u8'
      ]
li1=['todon.csv'  ]
#m_une_csvs.une_csvs2(li1)
f=open('lista_controlada.m3u','r')
texto=f.read()
texto=texto.replace('logo="http','logo="wttp')
texto=texto.replace('http','\nhttp')
texto=texto.replace('#','\n#')
texto=texto.replace('logo="wttp','logo="http')
texto=texto.replace('\n\n','\n')
texto=texto.replace('\n \n','\n')
#texto=texto.replace('%%%','\n')
f.close
f=open('lista_controlada1.m3u','w')
f.write(texto)
f.close

