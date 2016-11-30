print 'programando bubble sort reverso com python'

tamVetor = input('digite o tamanho do vetor: ')
vetor = []
for i in range(tamVetor):
    vetor.append(input("insira o " + str(i + 1) + " item: "))
print ''
print 'vetor inicial'
for e in range(tamVetor):
    print vetor[e],
print ''
for i in range(0,len(vetor)):
    for c in range(0,len(vetor)-1):
        if vetor[c] < vetor[c+1]:
            aux = vetor[c+1]
            vetor[c+1] = vetor[c]
            vetor[c] = aux
            print ''
            print vetor[c], 'troca', vetor[c+1]
            for e in range(tamVetor):
                print vetor[e],
            print ''
print ''
print 'vetor ordenado reverso'            
for i in range(tamVetor):
    print vetor[i],
