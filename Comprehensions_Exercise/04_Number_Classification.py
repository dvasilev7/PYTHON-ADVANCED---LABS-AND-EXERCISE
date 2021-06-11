numbers = [int(num) for num in input().split(", ")]

positive = [str(number) for number in numbers if number >= 0]
negative = [str(number) for number in numbers if number < 0]
even = [str(number) for number in numbers if number % 2 == 0]
odd = [str(number) for number in numbers if number % 2 == 1]

print("Positive:", ", ".join(positive))
print("Negative:", ", ".join(negative))
print("Even:", ", ".join(even))
print("Odd:", ", ".join(odd))