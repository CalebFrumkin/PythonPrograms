f=open('listb.txt')
count=1
listb=[]
for line in f:
    count-=1
    if count==0:
        title=line.lower()
        title=title.replace(' ','')
        title=title.replace(':','')
        title=title.replace('-','')
        title=title.replace('.','')
        title=title.replace('!','')
        listb.append(title)
        count=4
for i in range(len(listb)):
    listb[i]=listb[i].rstrip()
g=open('lista.txt')
count=1
lista=[]
for line in g:
    count-=1
    if count==0:
        if line[0:3].rstrip()==str(len(lista)+1):
            title=line[line.find('\t\t')+1:line.find(' Add')]
            title=title[:title.find(' Watch')]
            title=title[:title.find(' Edit')]
            title=title[:title.find(' (')]
            title=title.lower()
            title=title.replace(' ','')
            title=title.replace(':','')
            title=title.replace('-','')
            title=title.replace('.','')
            title=title.replace('!','')
            lista.append(title)
            count=3
        else:
            count+=1

for i in range(len(lista)):
    lista[i]= lista[i].strip('\t')

#MAl
for i in range(len(lista)):
    title=lista[i]
    #title=title[0:4]
    if title not in '\t'.join(listb):
        print(lista[i])

#anilist
for i in range(len(listb)):
    title=listb[i]
    #title=title[0:4]
    if title not in '\t'.join(lista):
        print(listb[i])
