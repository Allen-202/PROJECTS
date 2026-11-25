import math

first_name = "Gloria"
height = 60.2
very_beautiful = True
age = 20

print(f"My girl is called {first_name}")
print(f" She is {height} cm tall")
print(f"She is {age} years old")

if very_beautiful:
    print("My girl is very beautiful!")

else:
    print("My girl is NOT very beautiful")


 #CIRCUMFRENCE OF A CIRCLE

radius = float(input("Enter the radius of the circle"))

cicumference = 2 * math.pi *radius

print(f"The circumference of the circle is {round(cicumference, 2)}")
