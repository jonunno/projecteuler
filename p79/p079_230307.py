print("hello!")


f = open("p079\p079_keylog.txt", "r")

init_str = ""

for i in f: 
    
    init_str += str(i[0:3])
    print(i[0])
    print(init_str)
    for j in init_str:
        print(j)    


