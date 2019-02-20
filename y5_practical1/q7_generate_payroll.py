#7 (Payroll)
#Write a program q7_generate_payroll.py
#that reads the following information and
#prints a payroll statement. A sample input
#and output session is as follows:

#Sample input:

#Enter name: Lim Ah Seng
#Enter number of hours worked weekly: 10
#Enter hourly pay rate: 6.75
#Enter CPF contribution rate(%): 20

#Sample output:

#Payroll statement for Lim Ah Seng
#Number of hours worked in week: 10
#Hourly pay rate: $6.75
#Gross pay = $67.50
#CPF contribution at 20% = $13.50
#Net pay = $54.00

def payroll(name,work_hours,pay_rate,cpf_rate):
    print("{0} {1}".format("Payroll statement for",name))
    print("{0} {1}".format("Number of hours worked in week:",work_hours))
    print("{0}{1}".format("Hourly pay rate: $",pay_rate))
    gross_pay=pay_rate*work_hours
    print("{0}{1:.2f}".format("Gross pay = $",gross_pay))
    cpf_pay=gross_pay*cpf_rate/100
    print("{0}{1} {2}{3:.2f}".format("CPF contribution at ",cpf_rate,"= $",cpf_pay))
    print("{0}{1:.2f}".format("Net pay = $",gross_pay-cpf_pay))

name=input("Enter name: ")
work_hours=int(input("Enter number of hours worked weekly: "))
pay_rate=float(input("Enter hourly pay rate: $"))
cpf_rate=float(input("Enter CPF contribution rate(%): "))
payroll(name,work_hours,pay_rate,cpf_rate)
