with open("./top-1m.csv", "r") as file:
    counter = 0
    string = ""
    for line in file:
        string += line 
        counter += 1

        if counter > 500:
            break

    f = open("./top500.csv", "w")
    f.write(string)
