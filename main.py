myNumbers = [1, 2, 3, 4, 5, 11]
for num in myNumbers:
    print((lambda x: x*2)(num))

students = [['Bob', 70],
            ['Jane', 90],
            ['Bohdan', 50]]
print(students)
sortedStud = sorted(students, key=lambda x:x[1], reverse=True)
print(sortedStud)



curs = 41.31
discount = 0.2

pricoDol = lambda x: x/curs* (1 - discount)

amount = float(input("Введіть сумму: "))
print(f"price: {pricoDol(amount):.2f} $")

studBirth = [2000, 2010, 2009, 2011]
studAge = []
for year in studBirth:
    studAge.append(2024-year)

print(studAge)