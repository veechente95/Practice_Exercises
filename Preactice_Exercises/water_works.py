first_tier_rate = 5.41
second_tier_rate_low = 7.77
second_tier_rate_high = 9.79


def tier_rate():
    # High Usage Season
    if month_num >= range(4, 11):   # Oct = 10, however add 1 w/ range
        hcf = final_reading - initial_reading
        high_first_rate = hcf * first_tier_rate
        if hcf >= 24:
            hcf_difference = hcf - 24
            high_second_rate = (hcf_difference * second_tier_rate_high) + high_first_rate
            return high_second_rate
        return high_first_rate


initial_reading = int(input("Initial meter reading: "))
final_reading = int((input("Final meter reading: ")))
customer_name = str(input("Customer name: "))
month_num = int(input("Month number (1=Jan, 2=Feb, etc.): "))

# print("---")
# print(f"The bill for {customer_name} is $bill")

print(tier_rate())
