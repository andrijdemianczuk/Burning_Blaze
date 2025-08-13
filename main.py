# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from entities.User import User as User


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f"Hi, {name}. We're going to build some nice modules together.")  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi("Andrij")
    user = User(name="Andrij", email="andrij.demianczuk@gmail.com", password="123456")
    print(user.name)
    print(user.email)
    print(user.password)
