import math

def perform_action(current_value, action):
    if current_value == 0 and action != "3":
        print("Statement must start with a 3")
        exit()

    elif action == "3" and current_value ==0 :
        return 3

    elif action == "sqrt":
        return math.sqrt(current_value)
    
    elif action == "fact":
        return math.factorial(current_value)
    
    elif action == "floor": 
        return math.floor(current_value)

    else:
        print("Invalid action found: " + str(action))
        exit()
    

def evaulate_expression(evalute_expression):
    index = 0
    current_value = 0
    actions =[]
    actions = evalute_expression.split()
    for index in range(0,len(actions)):
        current_value = perform_action(current_value,actions[index])
    print("RESULT IS " + str(current_value))

evaulate_expression("3 fact sqrt floor")

evaulate_expression("3 floor")

evaulate_expression("3 fact fact")

evaulate_expression("3 fact fact sqrt")

evaulate_expression("3 fact fact sqrt sqrt")

evaulate_expression("3 fact fact sqrt sqrt floor")

evaulate_expression("3 fact fact sqrt sqrt floor fact")

evaulate_expression("3 fact fact sqrt sqrt floor fact sqrt")

evaulate_expression("3 fact fact sqrt sqrt floor fact sqrt floor fact")

evaulate_expression("3 fact fact sqrt sqrt floor fact sqrt floor fact sqrt")


evaulate_expression("3 fact fact sqrt sqrt floor fact sqrt floor fact sqrt sqrt")

evaulate_expression("3 fact fact sqrt sqrt floor fact sqrt floor fact sqrt sqrt floor fact")

evaulate_expression("3 fact fact sqrt sqrt floor fact sqrt floor fact sqrt sqrt floor fact sqrt")
evaulate_expression("3 fact fact sqrt sqrt floor fact sqrt floor fact sqrt sqrt floor fact sqrt sqrt")
evaulate_expression("3 fact fact sqrt sqrt floor fact sqrt floor fact sqrt sqrt floor fact sqrt sqrt sqrt")
evaulate_expression("3 fact fact sqrt sqrt floor fact sqrt floor fact sqrt sqrt floor fact sqrt sqrt sqrt sqrt")
evaulate_expression("3 fact fact sqrt sqrt floor fact sqrt floor fact sqrt sqrt floor fact sqrt sqrt sqrt sqrt sqrt")
evaulate_expression("3 fact fact sqrt sqrt floor fact sqrt floor fact sqrt sqrt floor fact sqrt sqrt sqrt sqrt sqrt sqrt")
evaulate_expression("3 fact fact sqrt sqrt floor fact sqrt floor fact sqrt sqrt floor fact sqrt sqrt sqrt sqrt sqrt sqrt floor fact")

evaulate_expression("3 fact fact sqrt sqrt floor fact sqrt floor fact sqrt sqrt floor fact sqrt sqrt sqrt sqrt sqrt sqrt floor fact sqrt")
evaulate_expression("3 fact fact sqrt sqrt floor fact sqrt floor fact sqrt sqrt floor fact sqrt sqrt sqrt sqrt sqrt sqrt floor fact sqrt floor sqrt")