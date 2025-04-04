qtdsim = 0 

pergunta1 = str(input("Telefonou para a vitima?: "))
if pergunta1 == "sim":
    qtdsim = qtdsim + 1 

pergunta2 = str(input("Esteve no local do crime?: "))
if pergunta2 == "sim":
    qtdsim = qtdsim + 1 

pergunta3 = str(input("Mora perto da vitima: "))
if pergunta3 == "sim":
    qtdsim = qtdsim + 1 

pergunta4= str(input("Devia pra vitima?: "))
if pergunta4 == "sim":
    qtdsim = qtdsim + 1 

pergunta5 = str(input("Ja trabalhou com a vitima?: "))
if pergunta5== "sim":
    qtdsim = qtdsim + 1 

if qtdsim == 2:
    qtdsim = qtdsim + 1 
    print("suspeito")

elif qtdsim == 3 and 4:
    qtdsim = qtdsim + 1 
    print("Cúmplice")

elif qtdsim == 5: 
    qtdsim = qtdsim + 1 
    print("culpado")
    

else:
    print("inocente")
