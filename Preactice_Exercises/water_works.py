# https://web.archive.org/web/20220429062001/http://web.cs.ucla.edu/classes/spring22/cs31/
first_tier_rate = 5.41
second_tier_rate_low = 7.77
second_tier_rate_high = 9.79


def tier_rate(month_num, initial_reading, final_reading):
    """Returns HCF rates based on low and high usage seasons."""
    hcf = final_reading - initial_reading
    first_rate = hcf * first_tier_rate

    # --- High Usage Season ---
    # if 4 <= month_num <= 10:
    if month_num in range(4, 11):
        if hcf > 23:
            hcf_high_difference = hcf - 23
            high_second_rate = (hcf_high_difference * second_tier_rate_high) + (23 * first_tier_rate)
            return round(high_second_rate, 3)
        return round(first_rate, 3)

    # --- Low Usage Season ---
    if month_num in (1, 2, 3, 11, 12):
        if hcf > 15:
            hcf_low_difference = hcf - 15
            low_second_rate = (hcf_low_difference * second_tier_rate_low) + (15 * first_tier_rate)
            return round(low_second_rate, 3)
        return round(first_rate, 3)


if __name__ == "__main__":
    initial_reading = int(input("Initial meter reading: "))
    if initial_reading < 0:
        print("The initial meter reading must not be negative.")
    final_reading = int((input("Final meter reading: ")))
    if final_reading < initial_reading:
        print("The final meter reading must be at least as large as the initial reading.")
    customer_name = str(input("Customer name: "))
    if customer_name == "":
        print("You must enter a customer name.")
    month_num = int(input("Month number (1=Jan, 2=Feb, etc.): "))
    if month_num <= 0 or month_num > 12:
        print("The month number must be in the range 1 through 12.")

    print("\n---")
    print(f"The bill for {customer_name} is ${float(round(tier_rate(month_num, initial_reading, final_reading), 3))}")


# ----- Program improvement using loops to iterate until valid input are made -----
# should_continue = False
# while not should_continue:
#     initial_reading = int(input("Initial meter reading: "))
#     if initial_reading < 0:
#         print("The initial meter reading must not be negative.")
#     else:
#         should_continue = True
#
# should_continue = False
# while not should_continue:
#     final_reading = int((input("Final meter reading: ")))
#     if final_reading < initial_reading:
#         print("The final meter reading must be at least as large as the initial reading.")
#     else:
#         should_continue = True
#
# should_continue = False
# while not should_continue:
#     customer_name = str(input("Customer name: "))
#     if customer_name == "":
#         print("You must enter a customer name.")
#     else:
#         should_continue = True
#
# should_continue = False
# while not should_continue:
#     month_num = int(input("Month number (1=Jan, 2=Feb, etc.): "))
#     if month_num <= 0 or month_num > 12:
#         print("The month number must be in the range 1 through 12.")
#     else:
#         should_continue = True
#
#
# print("\n---")
# print(f"The bill for {customer_name} is ${float(round(tier_rate(), 3))}")
