sexo = str(input('Digite seu sexo [M/F]: ')).upper().strip()[0]

while sexo not in "MmFf":
    sexo = str(input('Favor verifique os dados informados e digite corretamente. Digite seu sexo [M/F]: ')).upper().strip()[0]


sexo = str(input('Digite seu sexo [M/F]: ')).upper().strip()[0]

while sexo != "M" and sexo != "F":
    sexo = str(input('Favor verifique os dados informados e digite corretamente. Digite seu sexo [M/F]: ')).upper().strip()[0]