from random import seed
from random import randint
import math
class DNA:
    def __init__ (self,PopSize,Target,MutationRate):                 
        Population = []
        # for i in range(PopSize):
        #      Population.append((self.Gene(n)))
        Population = [self.Gene(Target) for i in range(PopSize)]
        self.population = Population
        self.target = Target  
        self.mutRate = MutationRate             
    pass

    def NewChar(self):    
        value = randint(32,122)
        return(chr(value))        
        
    def Gene(self,n):
        arr = []
        arr = [self.NewChar() for i in enumerate(n)]
        # for i in range(n):
        #     text = self.NewChar()
        #     arr.append(str(text))
        return arr  

    def GetScore(self,Ele):               
        m = len(self.target)        
        # scores = []
        score = 0       
        for i in range(m):
            if self.target[i] == Ele[i]:
                score +=1
        return score/m           
            
    
    def MatPool (self,Population):
        Mat = []
        for i in Population:
            n = math.floor(self.GetScore(i)*100)
            for m in range(n):
                Mat.append(i)        
        return Mat
        
    def Selection (self,Population):
        Mating  = self.MatPool(Population)        
        m = len(Mating)
        # print('MAting size: '+ str(m))
        if m !=0:
            A = randint(0,m-1)
            B = randint(0,m-1) 
            
            # print("Value A: %d and B: %d" %(A,B))   
            ParentA = Mating[A]
            ParentB = Mating[B]
        else:
            ParentA = Population[randint(0,len(Population))-1]
            ParentB = Population[randint(0,len(Population))-1]
        return ParentA,ParentB

    def CrossOver(self,Population):
        A,B = self.Selection(Population)
        MidPoint = randint(0,len(A))
        C = A[0:MidPoint] + B[MidPoint:len(B)]      
        return C

    def Reproduction_First(self): #How can I eliminate the arguments passed to Reproduction??        
        child = DNA(len(self.population),self.target,self.mutRate)        
        ScoreChild = 0
        teste = child.population
        for i in range(len(child.population)):            
            child.population[i] = self.CrossOver(self.population)
            for ii in range(len(child.population[i])):                   
                child.population[i][ii] = str(self.Mutation(child.population[i][ii]))
            ScoreChild = ScoreChild + child.GetScore(child.population[i])        
        AvgScore = ScoreChild/len(child.population)
        return child.population, AvgScore

    def Reproduction_General(self,Population):#How can I eliminate the arguments passed to Reproduction??    
        ScoreChild = 0
        for i in range(len(Population)):            
            Population[i] = self.CrossOver(Population)
            for ii in range(len(Population[i])):                   
                Population[i][ii] = str(self.Mutation(Population[i][ii]))
            ScoreChild = ScoreChild + self.GetScore(Population[i])        
        AvgScore = ScoreChild/len(Population)
        A,B = self.the_best(Population)  
        return Population, AvgScore, A, B           
    
    def Mutation (self,gene):
        n = randint(0,100)/1000
        if n <= self.mutRate:
            c = self.NewChar()
        else:
            c = gene
        return c

    def the_best(self,Population):
        s = 0
        for ele in Population:
            M = self.GetScore(ele)
            if M > s:
                s = M
                bigger = ele
        return s,bigger




    
        



    

        

    



    #def NaturalSelection (Population,Scores):
    #Need to get the max individual fitness and give them equivalenty probability to be picked.
    #So 
    

    

    

    
