import os


def strings_with_the_for(strings=[]):
    for i in range(1, 6):
        strings.append('str №' + str(i))
    return " \n".join(strings)


try_out = "String For Python Output"

outputs = strings_with_the_for()

# a = False

# def test():
#  global a
#  a = True
#  return a


