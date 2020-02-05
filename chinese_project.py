import re
var = {}
C_number = {"零":0,"一":1,"二":2,"三":3,"四":4,"五":5,"六":6,"七":7,"八":8,"九":9,"十":10}
def define(name,value):
    global var
    var[name] = value

def println(name):
    global var
    rule = r'“(.*?)”'
    try:
        print("\n")
        print(var[name])
    except:
        print("\n")
        print(re.find(rule))

def add(name,num):
    global var,C_number
    result = C_number[var[name]] +C_number[num]
    var[name] =  chinese(result)

def subtract(name,num):
    global var, C_number
    result = C_number[var[name]] - C_number[num]
    var[name] =  chinese(result)

def ifelse(get_input):
    global var,C_number
    num = C_number[get_input[3]]
    rule = r'“(.*?)”'
    list = re.findall(rule,str(get_input))
    if get_input[2] == "大于":
        if C_number[var[get_input[1]]] > num:
            print(list[0])
        else :
            print(list[1])
    elif get_input[2] == "小于":
        if C_number[var[get_input[1]]] < num:
            print(list[0])
        else :
            print(list[1])
    elif get_input[2] == "等于":
        if C_number[var[get_input[1]]] == num:
            print(list[0])
        else :
            print(list[1])
    else:
        print("输入不符合规则")


def chinese(num):
    global C_number
    for x in C_number:
        if num == C_number[x]:
            return x

while True :
    get_input = input().split()
    try: rubbish = get_input[0]
    except:print("无输入")
    else:
        if get_input[0] == "整数":
            if get_input[2] != "等于":
                print("输入不符合规则")
            else :
                define(get_input[1],get_input[3])
        elif get_input[0] == "看看":
            println(get_input[1])
        elif get_input[0] == "如果":
            ifelse(get_input)
        else :
            if get_input[1] == "增加":
                add(get_input[0],get_input[2])
            elif get_input[1] == "减少":
                subtract(get_input[0],get_input[2])
            else :
                print("输入不符合规则")