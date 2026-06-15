#for i in range(1, 11):
 #   print(i)

#for => kalit suz
#i => o'zgaruvchi 
# in
# range i + 0
#for i in range(11):
#    print(i) 



#for i in range(5, 11):
#    print(i)



#for i in range(5, 11, 2):
#    print(i)


#a = "salom"
#for i in a:
#    print(i.capitalize())





#a = 0
#matn = str(input("matn: "))
#for i in matn:
#    a = a + 1
#    print(a)



# for and if, elif, else


#for i in range(1, 11):
#    if i  % 2 !=0:  undov qoysak toq sonlarni chiqarib beradi
#       print(i)


print("1.Juft\n2.Toq")

a = int(input("Tanlash: "))
if a == 1:
    print("Juft son")
    son_1 = int(input("Boshlangich son: "))
    son_2 = int(input("Tugash son: "))
    for i in range(son_1, son_2):
        if i % 2 == 0:
            print(i, "Juft son: ")
elif a ==2:
    print("Toq son:")  
    son_1 = int(input("Boshlangich son:"))  
    son_2 = int(input("Tugash son: "))    
    for i in range(son_1, son_2):
        if i % 2 != 0:
            print(i, "Toq son")   
else:
    print("Error")             














