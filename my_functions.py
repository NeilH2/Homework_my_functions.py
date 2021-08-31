# def greet():
#     print("Hey"
    
# greet()

# def greet():
#     return "Hey"

# greeting = greet()
# print(greeting)

# def greet():
#     print("Hey")

# greeting = greet()
# print(greeting)

# def greet(name):
#     return "Hey" + name

# greeting = greet("bob")
# print(greeting)

# def greet(name, time_of_day):
#     return "Good " + time_of_day + ", " + name

# greeting = greet('Bob', 'morning')
# print(greeting)

# def greet(name, time_of_day):
#     return "Good " + time_of_day + ", "  + name

# name_1 = "Bob"
# time_of_day = "morning"

# greeting = greet(name_1, time_of_day) 
# print(greeting)  

# name_2 = "Ada"
# time_of_day_2 = "afternoon"

# greeting = greet(name_2, time_of_day_2)
# print(greeting)

chickens = [
  { "name": "Margaret", "age": 2, "eggs": 0 },
  { "name": "Hetty", "age": 1, "eggs": 2 },
  { "name": "Henrietta", "age": 3, "eggs": 1 },
  { "name": "Audrey", "age": 2, "eggs": 0 },
  { "name": "Mabel", "age": 5, "eggs": 1 },
]

def count_eggs( list ):
    total_eggs = 0

    for bird in list:
        total_eggs += bird["eggs"]
        bird["eggs"] = 0 

    return f"{total_eggs} eggs collected"

print(count_eggs(chickens))      
    
    