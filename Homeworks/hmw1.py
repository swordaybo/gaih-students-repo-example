

ciftsayilar=[]
teksayilar=[]


for i in range(0,100):

    if i%2==0:
        ciftsayilar.append(i)
    else:
        teksayilar.append(i)


newlist=teksayilar+ciftsayilar

for i in newlist:
    print(i)

