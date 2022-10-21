import random

lista=["vinst","vinst","nit"]
resultat=[]
a=int(input("Antal snurr : "))
for n in range (0,a):
    resultat.append(random.choice(lista))
print("Antal vinster ar",resultat.count("vinst"))
print("Andel vinster :",resultat.count("vinst")/(a*0.01),"%")