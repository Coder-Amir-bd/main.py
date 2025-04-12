name = "Amir Hamza"
age = 22
is_student = True

print(type(name))
print(type(age))
print(type(is_student))


age = 22

print("Multiplication:", age * 2)
print("Addition:", age + 5)
print("Subtraction:", age - 3)
print("Division:", age / 2)


print("Is age greater than 18?", age > 18)
print("Is age equal to 22?", age == 22)
print("Is age not equal to 30?", age != 30)
print("Is age less than 25?", age < 25)


has_id_card = True
knows_python = False

print("Has both ID card and knows Python?", has_id_card and knows_python)
print("Has either ID card or knows Python?", has_id_card or knows_python)
print("Does not know Python?", not knows_python)


marks = 50

marks += 10
print("After += :", marks)

marks -= 5
print("After -= :", marks)

marks *= 2
print("After *= :", marks)

marks /= 4
print("After /= :", marks)


a = 10
b = 20

print("Is a same as b?", a is b)
print("Is a not same as b?", a is not b)


fruits = ["apple", "banana", "mango"]

print("Is 'mango' in the list?", "mango" in fruits)
print("Is 'orange' not in the list?", "orange" not in fruits)
