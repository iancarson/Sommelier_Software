#Balanced parenthesis expression
list1 = ["[","{","("]
list2 = ["]","}",")"]

def balance(checkStr):
    #Stack to store the element of the strings
    stack = []
    for index in checkStr:
        #Check index in the list
        if index in list1:
            #Use one stack to add the index
            stack.append(index)
        #Using the same index, get the position.
        elif index in list2:
            position = list2.index(index)
            #If we empty list then it means that the string is balanced.
            if ((len(stack) > 0) and (list1[position] == stack[len(stack) -1])):
                stack.pop()
                #Otherwise the string is not balanced
            else:
                return "Not balanced"

    if len(stack) == 0:
        return "balanced."
    else:
        return "Not balanced."


if __name__ == '__main__':
    #Test this string.
    string = "[{}{})(]"
    print(balance(string))