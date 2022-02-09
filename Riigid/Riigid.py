import random 
def failist_lugemine():
    sõnastic={}
    file=open ("riig.txt",'r')
    for line in file:
        k,v=line.strip().split("-")
        sõnastic[k.strip()]=v.strip()
    file.close()
    print(sõnastic)
    return sõnastic



def kontrol(l1:list,l2:list):
    summa=0
    lists=[]
    lists.extend(l1)
    lists.extend(l2)
    random.shuffle(lists)
    print('random list ',lists)
    for i in range(len(l1)):
        otvet=input(f"Введи столицу - '{lists[i]}': ")
        if otvet in l1 or otvet in l2:
            if lists[i] in l1:
               if l1.index(lists[i])==l2.index(otvet):
                    summa+=1
                    print('правильно!')
                    print()
            elif lists[i] in l2:
                if l2.index(lists[i])==l1.index(otvet):
                    summa+=1
                    print('правильно!')
                    print()
        else:
            print('Неправильно!')
            print()
    resultPer=(summa/len(l1))*100
    print(f"Ваш результат: {resultPer}%")

def tõlkimine(l1:list,l2:list):
	sõna=input("Введите слово:")
	if sõna in l1:
		tõlk=l2[l1.index(sõna)]
		print(sõna+"-"+tõlk)
	elif sõna in l2:
		tõlk =l1[l2.index(sõna)]
		print(sõna+"-"+tõlk)
	else:
		print("Слова нет")

def uus_sõna(f:str,rida:str,l:list)->list:
	"""
    :param str f : имя файла 
    :param str rida : добавить слово
    """
	l=[]
	with open(f,"a",encoding="utf-8-sig") as fail:
		fail.write(rida+"\n")

def correction(sõna:str,l:list):
	for i in range(len(l)):
		if l[i]==sõna:
			uus_sona=sõna.replace(sõna,input("Новое слово: "))
			l.insert(i,uus_sõna)
			l.remove(sõna)
	return l
riig=[]
pealinad=[]
riig=failist_lugemine('pealinad.txt',riig)
pealinad=failist_lugemine('riig.txt',pealinad)

print("***Столицы***")
while True :
	menu=input("Новое слово-H,\nДобавить слово-W\nПеревод-A\nКонтроль-K\n")
	if menu.upper()=="A":
		tõlkimine(riig,pealinad)
	elif menu.upper()=="K":
		kontrol()
    elif menu.upper()=="W":
		correction()
