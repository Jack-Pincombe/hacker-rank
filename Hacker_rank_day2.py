x = float(input())
tipPercent = int(input())
taxPercent = int(input())

tip = x * (tipPercent/100)

tax = x * (taxPercent / 100)

total = x + tip + tax 
total = round(total)

print("The total meal cost is", total, "dollars.")