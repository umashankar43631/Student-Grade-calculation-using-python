def studentGrade(user_input):
    
    #This if condition checks whether user enters value between 0.0 and 1.0
    if(user_input>=0.0 and user_input<=1.0):

        #This function calculates grade of a student
        """Calculation of grades is as follows

           Score Grade
           
                >= 0.9 A
                >= 0.8 B
                >= 0.7 C
                >= 0.6 D
                <0.6 F

        """
        if(user_input>=0.9):
            return 'A'
        elif(user_input>=0.8):
            return 'B'
        elif(user_input>=0.7):
            return 'c'
        elif(user_input>=0.6):
            return 'D'
        else:
            return 'F'
    return False

#User enters a number,it will be converted into float and stored in user_input
user_input=float(input("Enter a score for the test"))

#The function studentGrade return value is stored in result object
result=studentGrade(user_input)
if(result):
    print(user_input,result )
else:
    print("Score is out of range!  Please enter valid test score between 0.0 and 1.0")



