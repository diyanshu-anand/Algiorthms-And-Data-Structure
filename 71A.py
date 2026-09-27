s = input()

string = list(s)

if(len(string)>10):
    list1 = [string[0],len(string)-2,string[-1]]
    print("".join(map(str,list1)))
else:
    print("".join(map(str,string)))