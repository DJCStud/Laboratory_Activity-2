class DownPaymentSys():
    Downhas = False
    def Enroll(Downhas,Cash):
        if Downhas == False:
            print("Cannot enroll without downpayment, pay a downpayment?")
            Choice = input("(Y/N): ")
            if Choice == "Y":
                Cash -= 1000
                if Cash < 0:
                    print("Insufficient cash")
                    Cash += 1000
                print("Cash 1000P paid\n BudgetBalance: ", Cash)
                print("Downpayment Completed")
                Downhas = True
            elif Choice == "N":
                print("Going back to main menu")
            else:
                print("Invalid Choice")
        elif Downhas == True:
            EnrollUnits = int(input("Input desired UnitAmount(25 Units max, 1200 per unit)"))


    def Viewtuition():
        s        

    def pay():
        s
        
    def deposit():
        s

    def Downpayment():
        s

class main(DownPaymentSys):
    print("---Student Enrollment System")
    Cash = int(input("Input Cash budget: "))

    print("Menu \n1. Enroll Courses \n2. View Tuition \n3. Payment \n4. View/Deposit Cash to budget \n5. Exit")
    Choice = int(input("Input Choice(1-5): "))
    if Choice == 1:
        Enroll(Downhas, Cash)
    if Choice == 2:
        Enroll(Cash)
    if Choice == 3:
        Enroll(Cash)
    if Choice == 4:
        Enroll(Cash)