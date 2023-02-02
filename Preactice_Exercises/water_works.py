# https://web.archive.org/web/20220429062001/http://web.cs.ucla.edu/classes/spring22/cs31/

program_on = True


while program_on:
    initial_reading = int(input("Initial meter reading: "))
    if initial_reading < 0:
        print("The initial meter reading must not be negative.")
    program_on = False

final_reading = int((input("Final meter reading: ")))
customer_name = str(input("Customer name: "))
month_num = int(input("Month number (1=Jan, 2=Feb, etc.): "))


print("---")
print(f"The bill for {customer_name} is $bill")
