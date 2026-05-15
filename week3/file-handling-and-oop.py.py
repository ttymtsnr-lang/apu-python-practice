filepath = "credential.txt"
users ={}
with open(filepath, mode="a") as f:
    username = input()
    age = input()
    pword = input()
    gender = input()
    f.write(f"{username}, {pword}, {age}, {gender}/n")
print(users)

users[username] = {
    "password": pword,
    "age": age,
    "gender": gender
}

multipliers = []
for i in range(2,5):
    multipliers.append(i)

class MyInt:
    def __init__(self,value):
        self.value = value

    def __add__(self,rhand):
        if isinstance(rhand, MyInt):
            return MyInt(self.value + rhand.value)

    def __str__(self):
        return f"MyInt({self.value})"


number = MyInt(15)
print(number)
number = number + 20
print(number)
