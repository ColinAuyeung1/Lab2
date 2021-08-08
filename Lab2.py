def data_owned(package):
    cost = 0
    data_add = 0
    if package == "green":
        cost = 49.99
        data_add = int(input("enter the additional data"))
        if data_add < 0:
            print("invalid data entered")
            return
        cost = cost + data_add * 14.99
    elif package == "orange":
        cost = 69.99
        data_add = int(input("enter the additional data:"))
        if data_add < 0:
            print("invalid data entered")
            return
        cost = cost + data_add * 9.99
    elif package == "purple":
        cost = 99.99
    else:
        print("Invalid package name")
        return
    print("You owe (round(cost,2))$ to the mobile phone provider")

    package = input("enter:")
    package = package.strip().lower()
    data_owned(package)