def get_user_input(): 
    print("get_user_input")
    user_input = input("Enter temperature values: ").split(",")
    floatLst = []
    for x in user_input:
        floatNumber = float(x)
        floatLst.append(floatNumber)

    print(floatLst)
    return floatLst

blah = get_user_input()