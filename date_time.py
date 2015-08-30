from datetime import date
now = date.today()
print(now)

# 
print(now.strftime("%m/%d/%y. %d %b %Y is %A"))

born = date(1984, 4, 10)
age = now - born

print(dir(age))
