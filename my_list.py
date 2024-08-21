numbers = []
numbers.append(10)
numbers.append(15)
numbers.append(20)
numbers.append(30)
numbers.append(40)
numbers_extend = [50, 60, 70]
numbers.extend(numbers_extend)
numbers.remove(70)
print(numbers[3])