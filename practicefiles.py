with open("practice.txt","w") as d:
    d.write("Hi everyone")
    d.write("\nwe are learning file I\O")
    d.write("\nusing java")
    d.write("\ni like programing in java")
    d.write("\ninsha kutti hai")
    # print(d.read())
    # data.replace("java","python")

with open("practice.txt","r") as d:
    data = d.read()
    new_data = data.replace("java", "python")

with open("practice.txt","w") as d:
    d.write(new_data)

with open("practice.txt", "r") as f:
    data = f.read()
    if (new_data.find("inshaa") != -1):
        print("yes it exist")
    else:
       print("not exist")

    

