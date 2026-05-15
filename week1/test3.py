# import interaction as i
from interraction import ask, greet
def main():
    # ask user for name and age
    # say hello and mention their age
    name, age = ask()
    greet(name, age)

main()
