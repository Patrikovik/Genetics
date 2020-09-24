from inco import DNA
Target = "To be or not to be"
PopSize = 500
Mutation = 0.007
Teste = DNA(PopSize,Target,Mutation)

A,B = Teste.Reproduction_First()
C,D,E,F = Teste.Reproduction_General(A)
for i in range(3):
    C,D,E,F = Teste.Reproduction_General(C)
    TheBestScore = ""    
    print(" Best_Score:  "+str(E)+"   AVG Score: " + str(D))
    print('\n')

    if E == 1.0:
        print(C)
        break

for ele in F:
    TheBestScore = TheBestScore+ele
    print(TheBestScore)


