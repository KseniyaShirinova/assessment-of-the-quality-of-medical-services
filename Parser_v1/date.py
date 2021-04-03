import codecs
data= codecs.open('alldata.txt','r', encoding='utf-8').read().split("***")
f1 = open("data_train.txt", 'w', encoding="utf-8")
f2=open("data_test.txt", 'w', encoding="utf-8")
data_train=""
data_test=""
print(len(data))
for i in range(len(data)):
    if i<170:
        data_train+=data[i]+"***"
    else:
        data_test+=data[i]+"***"
f1.write(data_train)
f2.write(data_test)
f1.close()
f2.close()


