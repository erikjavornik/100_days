import turtle, pandas

## Get the Coordinates from the Map image. Not needed for final code 
# def get_mouse_click_coor(x, y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

#Set up Screen and set "Background" as blank map
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

#Create list of all State name
state_name_data = pandas.read_csv("50_states.csv")
state_names = state_name_data.state.to_list()

#Empty list for while loop and store user guesses
user_states = []

#Loop through input prompt and check guess until all 50 states are guessed
while len(user_states) != 50:
    num_correct = len(user_states) 
    #Get and store user input. Standarize the spelling to all lower case for input
    answer_state = screen.textinput(title=f"{num_correct}/50 Guessed", prompt="Enter a state's name: ").lower()
    
    if answer_state == "exit":
        break
    
    for name in state_names:
        #Check in User input matches any state names
        if answer_state == name.lower():
            #Retrieve data row of input answer
            state_row = state_name_data[state_name_data.state == name]
            #Retreieve X and Y coordinates of state
            x_cor = int(state_row.x)
            y_cor = int(state_row.y)
            
            #Turtle object to write state name on the state image
            name_label = turtle.Turtle()
            name_label.penup()
            name_label.hideturtle()
            name_label.goto(x=x_cor, y=y_cor)
            name_label.write(name)
            
            #Add user guess to list of user entered states
            user_states.append(name)       

#Creates a list of missed states and Creates a new csv of states not entered
not_guessed = []

for name in state_names:
    if name not in user_states:
        not_guessed.append(name)
        
state_series = pandas.Series(not_guessed)
state_series.to_csv("Missed_States.csv")

screen.exitonclick()