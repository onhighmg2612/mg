def calculate_interest(principal, years, senior_citizen):
    if senior_citizen == 'y':
        rate = 12
    else:
        rate = 10
    interest = (principal * years * rate) / 100
    return interest

principal = int(input("Enter the principal amount: "))
years = int(input("Enter the no of years: "))
senior_citizen = input("Is customer senior citizen (y/n): ")

interest = calculate_interest(principal, years, senior_citizen)
print("Interest: ", interest)
