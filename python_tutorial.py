
#
# Python: 3.9.6
#
# Author: Stephen A. PArks Jr
#
# Purpose: The Tech Academy - Python Course, Creating our first program together.
#          Demonstrating how to pass variable from function to function
#          while producing a functional game.
#
#          Rememeber, function_name(variable) _means that we pass in the variable.
#          return variable _means that we are returning the variable to
#          back to the calling finction.






def start():
    f_name = "Sarah"
    l_name = "Connor"
    age = 28
    gender = "female"
    get_name(f_name, l_name,age,gender)


def get_name(f_name,l_name,age,gender):
    print("My name is {} {}. I am {} yearold {}.".format(f_name,l_name,age,gender))




    

if __name__ == "__main__":
    start()
