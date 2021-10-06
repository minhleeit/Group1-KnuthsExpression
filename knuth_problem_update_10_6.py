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
        try:
            if current_value >= 720 and actions[index] == "fact":
  #              print("TOO LARGE")
                return 99999999
            current_value = perform_action(current_value,actions[index])
        except Exception as e:
   #         print("ERROR OCCURED")
            current_value = 99999999

 #   print("RESULT IS " + str(current_value))
    return current_value


def check_if_goal_reached(state, target): 
 #   print("CHECKING ", state)
    return_result = False
    result = evaulate_expression(state)
    if (target == result):
        print("TARGET FOUND")
        print(state)
        return_result = True
    #Any value that goes towards 1 when the target is greater than 3 we dont care about
    elif target != 1 and result < 2:
    #    print("Target is not less than 1 and the current result is < 2")
        pass
    elif target == 1 and result < 2:
   #     print("target is 1 and the result is less than 2")
        state_list.append(str(state) + " floor")
    else:
        if str(result) in seen_states :
  #          print("SEEN", result)
            pass

        else:
         #   print("not a seen state")
            seen_states[str(result)] = state
            add_successors(state, result) 
   #         print("UPDATED STATE LIST: ", state_list)
  
    return return_result

def add_successors(state, result):
    
    #Simple way to check if an absurdly large number is an int
    r=result
    list_result = str(r).split('.')
 #   print("ADDING SUCCESSOR, ", r, state)
    if len(list_result) == 2: ## there is a decimal so it is not an int
       
        state_list.append(str(state) + " floor")
        state_list.append(str(state) + " sqrt")
    else: 
        state_list.append(str(state) + " sqrt")
        state_list.append(str(state) + " fact")
        state_list.append(str(state) + " floor")
        
    
    

def advance(target):
 
    while len(state_list) >0:
  #      print("STATE LIST: ", state_list)
        next_item = state_list.pop()
  #      print("NEXT: ", next_item)
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
            
            seen_states = {}
            state_list =["3"]

            print("Calculating.... please wait ...")
            advance(target)
        
        except Exception as e:
            print("Invalid input", e)