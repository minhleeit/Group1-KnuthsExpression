import math
from decimal import Decimal

seen_states = {}
state_list =["3"]

def perform_action(current_value, action):
    if current_value == 0 and action != "3":
        print("Statement must start with a 3")
        exit()

    elif action == "3" and current_value ==0 :
        return 3

    elif action == "sqrt":
        return Decimal(math.sqrt(current_value))
    
    elif action == "fact":
        return Decimal(math.factorial(current_value))
    
    elif action == "floor": 
        return math.floor(Decimal(current_value))

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
    return current_value


def check_if_goal_reached(state, target): 
    result = evaulate_expression(state)
    if ( target == result):
        print("TARGET FOUND")
        return True
    elif target > 2 and result < 2:
        pass
    else:
        if str(result) in seen_states :
            print("STATE SEEN", result)

        else:
            print("ADDING RESULT", result)
            seen_states[str(result)] = state
            add_successors(state, result)    
            print()
            print("CURRENT LIST: ", state_list)
            print()
            return False

def add_successors(state, result ):
    print("TYPE OF RESULT: ", type(result))
    if not isinstance(result, int):
        state_list.append(str(state) + " floor")
        state_list.append(str(state) + " sqrt")

    else: 
        state_list.append(str(state) + " sqrt")
        state_list.append(str(state) + " fact")
        state_list.append(str(state) + " floor")

def advance(target):
 
    while len(state_list) >0:
        next_item = state_list.pop()
        print("NEXT ITEM: ", next_item)
        if check_if_goal_reached(next_item,target):
            break
        

target = 5
advance(target)
# evaulate_expression("3 fact sqrt floor")

# evaulate_expression("3 floor")

# evaulate_expression("3 fact fact")

# evaulate_expression("3 fact fact sqrt")

# evaulate_expression("3 fact fact sqrt sqrt")
        
# evaulate_expression("3 fact fact sqrt sqrt floor")

# evaulate_expression("3 fact fact sqrt sqrt floor fact")

# evaulate_expression("3 fact fact sqrt sqrt floor fact sqrt")

# evaulate_expression("3 fact fact sqrt sqrt floor fact sqrt floor fact")

# evaulate_expression("3 fact fact sqrt sqrt floor fact sqrt floor fact sqrt")


# evaulate_expression("3 fact fact sqrt sqrt floor fact sqrt floor fact sqrt sqrt")

# evaulate_expression("3 fact fact sqrt sqrt floor fact sqrt floor fact sqrt sqrt floor fact")

# evaulate_expression("3 fact fact sqrt sqrt floor fact sqrt floor fact sqrt sqrt floor fact sqrt")
# evaulate_expression("3 fact fact sqrt sqrt floor fact sqrt floor fact sqrt sqrt floor fact sqrt sqrt")
# evaulate_expression("3 fact fact sqrt sqrt floor fact sqrt floor fact sqrt sqrt floor fact sqrt sqrt sqrt")
# evaulate_expression("3 fact fact sqrt sqrt floor fact sqrt floor fact sqrt sqrt floor fact sqrt sqrt sqrt sqrt")
# evaulate_expression("3 fact fact sqrt sqrt floor fact sqrt floor fact sqrt sqrt floor fact sqrt sqrt sqrt sqrt sqrt")
# evaulate_expression("3 fact fact sqrt sqrt floor fact sqrt floor fact sqrt sqrt floor fact sqrt sqrt sqrt sqrt sqrt sqrt")
# evaulate_expression("3 fact fact sqrt sqrt floor fact sqrt floor fact sqrt sqrt floor fact sqrt sqrt sqrt sqrt sqrt sqrt floor fact")

# evaulate_expression("3 fact fact sqrt sqrt floor fact sqrt floor fact sqrt sqrt floor fact sqrt sqrt sqrt sqrt sqrt sqrt floor fact sqrt")
# evaulate_expression("3 fact fact sqrt sqrt floor fact sqrt floor fact sqrt sqrt floor fact sqrt sqrt sqrt sqrt sqrt sqrt floor fact sqrt floor sqrt")