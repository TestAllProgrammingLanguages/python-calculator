def myDivision(a,b):
    return a/b

def myMultipication(a,b):
    return a*b

def myMinus(a,b):
    return a-b

def myPlus(a,b):
    return a+b




def myTakeInputs(s):
    try:
        x = float(input("Please enter "+s+" number:"))
        return x;
    except ValueError:
        myTakeInputs(s)
    except:
        print("ops, something is wrong! please pay attention about your inputs (the error code is 1)")


def myTakeAction():
    try:
        ac = str(input("Please enter action (for example + or - or / or *):"))
        if ac == "+":
            return ac
        if ac == "-":
            return ac
        if ac == "/":
            return ac
        if ac == "*":
            return ac
        else:
            myTakeAction()
    except ValueError:
        myTakeAction()
    except:
        print("ops, something is wrong! please pay attention about your inputs (the error code is 2)")


def myUseWhatFunction(first_num,actionn,second_num):
    try:
        if actionn == "+":
            return myPlus(first_num,second_num)
        if actionn == "-":
            return myMinus(first_num,second_num)
        if actionn == "/":
            return myDivision(first_num,second_num)
        if actionn == "*":
            return myMultipication(first_num,second_num)
    except:
        print("ops, something is wrong! (the error code is 3)")


try:
    first_number = myTakeInputs("first")
    action_cal = myTakeAction()
    second_number = myTakeInputs("second")
    result = myUseWhatFunction(first_number,action_cal,second_number)
    print(str(first_number)+" "+ action_cal + " " + str(second_number) + " = "+ str(result))
except:
    print("ops, something is wrong! (the error code is 4)")
