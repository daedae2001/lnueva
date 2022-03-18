def une_csvs(li):
    todo = ""
    for arc in li:
        ar = arc.replace('.m3u8', '.csv').replace('.m3u', '.csv')
        f = open(ar, 'r', encoding="utf8")
        todo = todo+f.read()
        f.close()
    f = open('todo.csv', 'w', encoding="utf8")
    f.write(todo)
    f.close()
def une_csvs2(li):
    todo = ""
    i=1
    for arc in li:
        ar = arc
        f = open(ar, 'r', encoding="utf8")
        todo = f
        todo1=''
        for y in todo:
            todo1=todo1+y.replace('http','#EXTINF:-1 ,c'+str(i)+'\nhttp')
            i=i+1
        f.close()
    f = open('todo1.csv', 'w', encoding="utf8")
    f.write(todo1)
    f.close()