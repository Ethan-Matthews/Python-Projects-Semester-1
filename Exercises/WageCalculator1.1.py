"""
Prompt user to input hours worked.  Varaibles used are hoursWorked, hourlyRate.
calculate pay from number of hours. Variables used are regPay, overTime.
conditional IF statement, if hours are over 40 pay increrases to 1.5x.
output variables in .format string.
"""

#Don't forget to rename this file after copying the template
#for a new program!
"""
Student Name:    Ethan Matthews
Program Title:   Wage Calculator
Description:     Calculate pay and overtime after 40hrs.
"""

def main(): #<-- Don't change this line!
    #Write your code below. It must be indented!

    hourlyRate = 10.00
    overtimeBracket = 40
    overtimePayRate = 1.5
    
    print("Welcome to the Pay Calculator!\n")
    hoursWorked = float(input("Enter the number of hours worked: "))
    

    if hoursWorked > overtimeBracket:
        overTime = ((hoursWorked - overtimeBracket) * (hourlyRate * overtimePayRate)) + (overtimeBracket * hourlyRate)  #Clac for overtime.                                                                #Conditional statement for overtimeBracket.
        print("\nYour total pay with overtime is ${0:.2f}.".format(overTime))                               #Print IF pay has overtime.
    else:
        regPay = hoursWorked * hourlyRate
        print("\nYou total pay is ${0:.2f}.".format(regPay))                                                #Print IF pay doesn't have overtime.

    print("\nThankyou for using the Pay Calculator!")

    #Your code ends on the line above

#Do not change any of the code below!
if __name__ == "__main__":
    main()