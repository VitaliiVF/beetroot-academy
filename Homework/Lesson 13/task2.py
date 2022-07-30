def deposit(amount):
    def add(percent):
        def year(year):
            return amount * (percent / 100) * year
        return year 
    return add

sum_deposit = int(input("Enter deposit amount: "))
percent = int(input("Enter deposit percentage: "))
year = int(input("Length of deposit in years: "))

func = deposit(sum_deposit)
func1 = func(percent)

print(f"If you put {sum_deposit} UAH on a deposit for {year} years at {percent}%, you can get {sum_deposit + int(func1(year))} UAH")