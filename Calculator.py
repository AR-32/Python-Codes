a = (input("Enter first Number"))
b = (input("Enter second Number"))
print("Which operator you want to perform !!!")
print(" 1. Arithmetic Operator\n","2. Bitwise Operator\n","3. Relational Operator\n","4. Logical Operator\n")
operator = input("Type the starting '3' letters of the operator you want to perform")
def calculator(operator):
    if operator == ("ari" or "ARI" or "Ari" or "aRI"):
        arithmetic_operator = input("Enter the operator to be performed")
        def cal_1(arithmetic_operator):
            if arithmetic_operator == "add":
                return "Addition of two numbers", int(a)+int(b)
            elif arithmetic_operator == "subtract":
                print("If you want",int(a),"-",int(b),"type 'first'\nIf you want",int(b),"-",int(a),"type 'second'")
                c = input("what do you want ?")
                if c == "first":
                    return "Subtraction of",int(a),"-",int(b),"is",int(a)-int(b)
                if c == "second":
                    return "Subtraction of",int(b),"-",int(a),"is",int(b)-int(a)
            elif arithmetic_operator == "multiply":
                return "Multiplication of two numbers", int(a)*int(b)
            elif arithmetic_operator == "divide":
                print("If you want",int(a),"/",int(b),"type 'first'\nIf you want",int(b),"/",int(a),"type 'second'")
                d = input("what do you want ?")
                if d == "first":
                    return "Division of",int(a),"/",int(b),"is",int(a)/int(b)
                if d == "second":
                    return "Division of",int(b),"/",int(a),"is",int(b)/int(a)
            elif arithmetic_operator == "remainder":
                print("If you want",int(a),"%",int(b),"type 'first'\nIf you want",int(b),"%",int(a),"type 'second'")
                e = input("what do you want ?")
                if e == "first":
                    return "Remainder of",int(a),"%",int(b),"is",int(a)%int(b)
                if e == "second":
                    return "Remainder of",int(b),"%",int(a),"is",int(b)%int(a)
            elif arithmetic_operator == "power":
                print("If you want",int(a),"**",int(b),"type 'first'\nIf you want",int(b),"**",int(a),"type 'second'")
                f = input("what do you want ?")
                if f == "first":
                    return "Power of",int(a),"**",int(b),"is",int(a)**int(b)
                if f == "second":
                    return "Power of",int(b),"**",int(a),"is",int(b)**int(a)
            else:
                return "Invalid Operator"
        return cal_1(arithmetic_operator)   
    elif operator == ("bit" or "BIT" or "Bit" or "bIT"):
        bitwise_operator = input("Enter the operator to be performed")
        def cal_2(bitwise_operator):
            if bitwise_operator == "AND":
                return "Bitwise AND of two numbers", int(a)&int(b)
            elif bitwise_operator == "OR":
                return "Bitwise OR of two numbers", int(a)|int(b)
            elif bitwise_operator == "NOT":
                return "Bitwise NOT of both number", ~int(a), ~int(b)
            elif bitwise_operator == "XOR":
                return "Bitwise XOR of two numbers", int(a)^int(b)
            elif bitwise_operator == "RIGHT":
                return "Bitwise RIGHT SHIFT of both numbers by 2", int(a)>>2, int(b)>>2
            elif bitwise_operator == "LEFT":
                return "Bitwise LEFT SHIFT of both numbers by 2", int(a)<<2, int(b)<<2
            else:
                return "Invalid Operator"
        return cal_2(bitwise_operator)
    elif operator == ("rel" or "REL" or "Rel" or "rEL"):
        print("Note:\nUse '_' instead of space and write in small letters only")
        relational_operator = input("Enter the operator to be performed")
        def cal_3(relational_operator):
            if relational_operator == "greater_than":
                if int(a) > int(b):
                    return int(a),"is greater than",int(b)
                else:
                    return int(b),"is greater than",int(a)
            elif relational_operator == "less_than":
                if int(a) < int(b):
                    return int(a),"is less than",int(b)
                else:
                    return int(b),"is less than",int(a)
            elif relational_operator == "equal_to":
                return int(a)==int(b)
            elif relational_operator == "not_equal":
                return int(a)!=int(b)
            elif relational_operator == "greater_than_equal_to":
                return int(a)>=int(b)
            elif relational_operator == "less_than_equal_to":
                return int(a)<=int(b)
            else:
                return "Invalid Operator"
        return cal_3(relational_operator)
    elif operator == ("log" or "LOG" or "Log" or "lOG"):
        logical_operator = input("Enter the operator to be performed")
        def cal_4(logical_operator):
            if logical_operator == "and":
                return "Bitwise AND of two numbers", int(a) and int(b)
            elif logical_operator == "or":
                return "Bitwise OR of two numbers", int(a) or int(b)
            elif logical_operator == "not":
                return "Bitwise NOT of both numbers", not int(a), not int(b)
            else:
                return "Invalid Operator"
        return cal_4(logical_operator)
    else:
        return "invalid"  
print(calculator(operator))