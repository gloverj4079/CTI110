def days_in_feb(user_year):
    if (user_year % 4 == 0 and user_year % 100 != 0) or (user_year % 400 == 0):
        return 29
    else:
        return 28

if __name__ == '__main__':
    input_year = int(input(""))
    result = days_in_feb(input_year)
    print(f"{input_year} has {result} days in February.")
    