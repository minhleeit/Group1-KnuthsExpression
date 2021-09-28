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
        #Added a square root approximation if the value is greater than the amount the math.sqrt() function can handle
        if (current_value < (1<<100)):
            return Decimal(math.sqrt(current_value))
        else:
            approximation = 1 << ((int(current_value).bit_length() + 1) >> 1)
            while True:
                new_approx = (approximation + int(current_value) // approximation) >> 1
                if new_approx >= approximation:
                    return approximation
                approximation = new_approx
    
    elif action == "fact":
#        print("TYPE AT FACTORIAL: ", type(current_value))
#        print("CURRENT VALUE FOR CURRENT_VALUE", current_value)
        return Decimal(math.factorial(int(current_value)))
    
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
 #   print("RESULT IS " + str(current_value))
    return current_value


def check_if_goal_reached(state, target): 
    result = evaulate_expression(state)
    if (target == result):
        print("TARGET FOUND")
        print(state)
        return True
    #Any value that goes towards 1 when the target is greater than 3 we dont care about
    elif target != 1 and result < 2:
        pass
    elif target == 1 and result < 2:
        state_list.append(str(state) + " floor")
    else:
        if str(result) in seen_states :
  #          print("STATE SEEN", result)
            pass

        else:
  #          print("ADDING RESULT", result)
            seen_states[str(result)] = state
            add_successors(state, result)    
 #           print()
 #           print("CURRENT LIST: ", state_list)
#            print()
            return False

def add_successors(state, result):
    
    #Simple way to check if an absurdly large number is an int
    r=result
    list_result = str(r).split('.')
    if len(list_result) == 2: 
        state_list.append(str(state) + " floor")
        state_list.append(str(state) + " sqrt")
    else: 
        state_list.append(str(state) + " fact")
        state_list.append(str(state) + " sqrt")
        state_list.append(str(state) + " floor")

def advance(target):
 
    while len(state_list) >0:
        next_item = state_list.pop()
        if check_if_goal_reached(next_item,target):
            break

continue_prompt = True
while continue_prompt:        
    print()
    user_input = input("please enter a targer number as an integer or type end to exit >> ")
    if user_input == "end":
        print("Thank you for using the knuth expression program")
        exit()
    else:
        try:
            target = int(user_input)
            print("Calculating.... please wait ...")
            advance(target)
        
        except:
            print("Invalid input")