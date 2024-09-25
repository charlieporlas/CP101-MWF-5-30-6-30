# Part 1: Basic f-string Formatting
def f_string_formatting():
    name = "Alice"  # Example input
    age = 25        # Example input
    print(f"Hello, {name}! You are {age} years old.")
# Part 2: Using .format()
def format_method():
    items = ["Apple", "Banana", "Carrot"]
    prices = [1.50, 0.75, 0.90]
    print("{:<10} {:>10}".format("Item", "Price"))  # Align headers
    print("-" * 20)
    for item, price in zip(items, prices):
        print("{:<10} ${:>8.2f}".format(item, price))  # Align items and prices

# Part 3: Legacy % formatting
def legacy_percent_formatting():
    temperature = 23.4567  # Example input
    print("The current temperature is %.2f degrees Celsius." % temperature)

# Call the functions to display the results
f_string_formatting()
format_method()
legacy_percent_formatting()
