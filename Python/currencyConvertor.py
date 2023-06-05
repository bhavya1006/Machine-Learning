print("Bhavya Madan\n0901AM221026")

def convert_currency(base_currency,amount,target_currency):
    currency_exchange_rates = {"rs":{'usd':0.012,'sol':0.045,'lira':0.25},
                               "usd":{'rs':82.40,'sol':3.70,'lira':20.96},
                               "sol":{'rs':22.29,'usd':0.27,'lira':5.67},
                               "lira":{'rs':3.93,'usd':0.048,'sol':0.048}}
    cc = currency_exchange_rates[base_currency]
    exchange_currency = cc[target_currency]
    converted_amount = amount * exchange_currency
    return converted_amount


print("Welcome to the Currency Converter!")
print("Available currency exchange possible: RS,USD,LIRA,SOL")
base_currency = input("Enter the base currency: ").lower()
target_currency = input("Enter the target currency: ").lower()
amount = float(input("Enter the amount to convert: "))
converted_amount = convert_currency(base_currency,amount,target_currency)


print(f"{amount} {base_currency} is equal to {round(converted_amount,10)} {target_currency}.")
