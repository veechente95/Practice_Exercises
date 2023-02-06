first_tier_rate = 5.41
second_tier_rate_low = 7.77
second_tier_rate_high = 9.79


def tier_rate():
    """Returns HCF rates based on low or high usage seasons."""
    # Low Usage Season
    hcf = final_reading - initial_reading
    high_first_rate = hcf * first_tier_rate

    if 4 <= month_num <= 10:   # Oct = 10, however add 1 w/ range
        return high_first_rate
    elif hcf >= 24:
        hcf_high_difference = hcf - 23
        high_second_rate = (hcf_high_difference * second_tier_rate_high) + high_first_rate
        return high_second_rate
    # High Usage Season
    elif month_num == 11 or 12 or 1 or 2 or 3:
        low_first_rate = hcf * first_tier_rate




initial_reading = int(input("Initial meter reading: "))
final_reading = int((input("Final meter reading: ")))
customer_name = str(input("Customer name: "))
month_num = int(input("Month number (1=Jan, 2=Feb, etc.): "))
print("---")
print(f"The bill for {customer_name} is ${round(tier_rate(), 2)}")

