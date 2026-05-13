#f-strings in python
letter = "hello i am {1} and i am from {0}"
country = "india"
name = "kuldeep"
print(letter.format(country,name))
print(f"hello i am {name} and i am from {country}")

price = 49.0999

txt = f"for only {price:.2f} dollars!"
print(txt.format(price = 49.0999)) 