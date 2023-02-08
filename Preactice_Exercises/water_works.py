first_tier_rate = 5.41
second_tier_rate_low = 7.77
second_tier_rate_high = 9.79


def tier_rate():
    """Returns HCF rates based on low and high usage seasons."""
    hcf = final_reading - initial_reading
    first_rate = hcf * first_tier_rate

    # --- High Usage Season ---
    if 4 <= month_num <= 10:
        if hcf > 23:
            hcf_high_difference = hcf - 23
            high_second_rate = (hcf_high_difference * second_tier_rate_high) + (23 * first_tier_rate)
            return high_second_rate
        return first_rate
    # --- Low Usage Season ---
    if month_num == 11 or 12 or 1 or 2 or 3:
        if hcf > 15:
            hcf_low_difference = hcf - 15
            low_second_rate = (hcf_low_difference * second_tier_rate_low) + (15 * first_tier_rate)
            return low_second_rate
        return first_rate


should_continue = True
while should_continue:

    initial_reading = int(input("Initial meter reading: "))
    if initial_reading < 0:
        should_continue = False
        print("The initial meter reading must not be negative.")

    final_reading = int((input("Final meter reading: ")))
    if initial_reading > final_reading:
        should_continue = False
        print("The final meter reading must be at least as large as the initial reading.")

    customer_name = str(input("Customer name: "))
    if customer_name == "":
        should_continue = False
        print("You must enter a customer name.")

    month_num = int(input("Month number (1=Jan, 2=Feb, etc.): "))
    if month_num != 1 <= month_num <= 12:
        should_continue = False
        print("The month number must be in the range 1 through 12.")

    print("\n---")
    print(f"The bill for {customer_name} is ${round(tier_rate(), 2)}")

