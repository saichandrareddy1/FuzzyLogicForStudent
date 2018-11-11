import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
print("================LPU GRADING SYSTEM WITH FUZZY LOGIC SYSTEM=================")

class MarksAverage():
    '''We have taken the class for the marksAverage for finding'''
    def __init__(self, CA1, CA2, MTE, ETE, ATTD): #parameterised constructors
        self.CA1 = CA1
        self.CA2 = CA2
        self.MTE = MTE
        self.ETE = ETE
        self.ATTD = ATTD
        
    def ClassAssingn(self): #function for the CA'S
        self.results = ((self.CA1 + self.CA2)/60) * 25 
        return self.results

    def Average_mid(self): #Function for the AverageMid
        self.Mte_results = (self.MTE / 40) *20
        return self.Mte_results

    def Ete_Average(self): #Funcion for ETE
        self.ETE_results = (self.ETE / 70) * 50
        return self.ETE_results

    def ATT_marks(self): #attendence with If Else statements
        if self.ATTD >= 90:
            self.ATTDE = 5
            return self.ATTDE
        elif self.ATTD >= 85:
            self.ATTDE = 4
            return self.ATTDE
        elif self.ATTD >= 80:
            self.ATTDE = 3
            return self.ATTDE
        elif self.ATTD >= 75:
            self.ATTDE = 2
            return self.ATTDE
        else:
            self.ATTDE = 0
            return self.ATTDE

    def TotalMarks(self): #Adding all the marks of CAS, MID, ETE
        self.Total = self.results + self.Mte_results + self.ETE_results + self.ATTDE
        return self.Total

    def Grade_SY(self): #Grading Scale for the Final result
        if self.Total >= 90:
            return 10
        elif self.Total >= 85:
            return 9
        elif self.Total >= 80:
            return 8
        elif self.Total >= 75:
            return 7
        elif self.Total >= 60:
            return 6 
        elif self.Total >= 50:
            return 5
        else:
            return 0
        
Total_List = list() #Empty list we declared

print("===============PLEASE ENTER THE NUMBER OF THE SUBJECTS=================")
Total_SUB = int(input("Enter the total number of the subjects:-"))  #Enter Total Number Of The Subjects
print("================Enter  the marks of the each sub=================== ")
for _ in range(Total_SUB): #It will run with the number of the subjects in a loop
    SubjectName = input("Enter name of the SUBJECT :-")
    CA1 = int(input("Enter the marks of the CA1 marks out of 30:-"))
    CA2 = int(input("Enter the marks of the CA2 marks out of 30:-"))
    MTE = int(input("Enter the marks of the MTE marks out of 40:-"))
    ETE = int(input("Enter the marks of the ETE marks out of 70:-"))
    ATTD = int(input("Enter the marks of the ATTENDENCE PERCENTAGE out of 100:-"))
    x = MarksAverage(CA1, CA2, MTE, ETE, ATTD)
    m = x.ClassAssingn()
    n = x.Average_mid()
    z = x.Ete_Average()
    y = x.ATT_marks()
    r = x.TotalMarks()
    G = x.Grade_SY()
    Total_List.append(G) #it will enter grade into the Empty list
    print("Are the marks of the CAS, MID,ETE and ATTENDENCE\nCA:-{}\nMID:-{}\nETE:-{}\nATTENDENCE:-{}\nTotal:-{}\nGrade:-{}".format(m, n, z, y, r, G))
Final_Grade = sum(Total_List)/Total_SUB #it will give final grade of the Caluclator
print("TOTAL LIST OF THE MARKS:- {}".format(Total_List))
print("final grade :-{}".format(Final_Grade))



print("===============Fuzzy logic  was started in this======================")



results = ctrl.Antecedent(np.arange(0, 11, 1), 'results')
'''Input to the user it is in the form of crisp logic'''
credit = ctrl.Antecedent(np.arange(0, 11, 1), 'credit')
end = ctrl.Consequent(np.arange(0, 11, 1), 'end')
'''output of the code after the defuzzification'''
results.automf(3)
credit.automf(3)

end['low'] = fuzz.trimf(end.universe, [0, 0, 5]) #Tringular membershipfunction, universe refers to all
end['medium'] = fuzz.trimf(end.universe, [0, 5, 10])
end['high'] = fuzz.trimf(end.universe, [5, 10, 10])

results.view()
credit.view()
end.view()

#Rules for the control system
rule1 = ctrl.Rule(results['poor'] | credit['poor'], end['low'])
rule2 = ctrl.Rule(credit['average'], end['medium'])
rule3 = ctrl.Rule(credit['good'] | results['good'], end['high'])

#Control system for the Fuzzylogic
tipping_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
tipping = ctrl.ControlSystemSimulation(tipping_ctrl)

tipping.input['results'] = Final_Grade
tipping.input['credit'] = int(input("enter the Credits of the bhavior of the student:-"))
#it will defuzzicate all to human understandle method
tipping.compute()
print (tipping.output['end'])
end.view(sim=tipping) #it will shade the graph
