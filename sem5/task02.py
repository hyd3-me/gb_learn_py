names = ["Alice", "Bob", "Charlie"]
salary = [5000, 6000, 7000]
bonus = ["10%", "5%", "15%"]

_tuple = zip(names, salary, bonus)

_d = {item[0]: item[1] * float(item[2][:-1])/100 for item in _tuple}
print(_d)