def calculo_complexo(a, b):
    # Variavel nao usada (Code Smell)
    x = 10 
    return a + b

# Bloco duplicado 1
def repeticao_um():
    print("Isso e um erro de duplicidade")
    print("Isso e um erro de duplicidade")
    print("Isso e um erro de duplicidade")

# Bloco duplicado 2 (Exatamente igual ao 1 = CRIME no Sonar)
def repeticao_dois():
    print("Isso e um erro de duplicidade")
    print("Isso e um erro de duplicidade")
    print("Isso e um erro de duplicidade")
