def invest(amount, rate, years):
    for i in range(1, int(years + 1)):
        print(f'year {i}: ${round(amount * (1 + rate)**i, 2)}')

amount_user, rate_user, years_user = map(float, input('Enter an initial amount, an annual percentage rate, and a number of years with space: ').split())
invest(amount_user, rate_user, years_user)