# parbaudes darba uzdevumi

import random
eriks = 20 + 3 + 2006
kozeris = []

for i in range (eriks):
    kozeris.append(random.randrange(-150, 150))

print(kozeris)


pozitivie = 0
negativie = 0

for i in range(eriks):
    if kozeris[i] >= 0:
        pozitivie += 1
    elif kozeris[i] < 0:
        negativie += 1
    i += 1

print("Negativo skaitlu skaits = ", negativie, "Pozitivo skaitlu skaits = ", pozitivie,)


paraskaitli = 0
neparaskaitli = 0

for i in range(eriks):
    if kozeris[i]%2 == 0:
        paraskaitli += 1
    else:
        neparaskaitli += 1
    i +=1

print("Para skaitlu skaits = ", paraskaitli, "Nepara skaitlu skaits = ", neparaskaitli)


videjaisaritmetiskais = 0

for i in range(eriks):
    videjaisaritmetiskais += kozeris[i]
    i += 1

print("Vidējais aritmētiskais =",videjaisaritmetiskais/eriks)



nepara = []
for i in range(eriks):
     if kozeris[i]%2 == 0:
         None
     else:
         nepara.append(kozeris[i])
     i += 1

print(nepara)

sk = 0
for i in range(eriks):
     if kozeris[i] == 20:
         sk += 1
     i += 1

if sk == 0:
    print("Skaitļi, kuri nesakrit ar manu dzimšanas dienu.")
else:
    print("Skaitļi, kuri sakrīt ar manu dzimšanas dienu ", sk)


    mazaki = 0
    for i in range(eriks):
        if kozeris[i] < mazaki/eriks:
            mazaki += 1
        i +=1

print("Skaitļi kas ir mazāki par vidējo aritmētisko ", mazaki)


divcipars = 0
for i in range(eriks):
     if kozeris[i] >= -99 and kozeris[i] < -9:
         divcipars += 1
     elif kozeris[i] >= 10 and kozeris[i] < 100:
         divcipars += 1
     i +=1

print("izvaditie skaitli divcipari ", divcipars)
 

 


