class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"my name is {self.name} and my age is {self.age}"
    def  is_adult(self):
       if self.age>=18:
          print("You have too much responsibilities")
       else:
           print("Lucky you")
first_person = person("omar",20)
print(first_person.age)
print(first_person.name)          
print(first_person)
first_person.is_adult()
