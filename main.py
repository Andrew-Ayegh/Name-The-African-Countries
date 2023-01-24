import pandas
import turtle
import random

blank_image = "Blank_Africa.gif"

screen = turtle.Screen()
screen.setup(width=800, height=750)
data = pandas.read_csv("African_Countries.csv")



screen.addshape(blank_image)
turtle.shape(blank_image)

# Getting the Data from the African countries.csv file
data1  = pandas.read_csv("African_Countries.csv") 
c_data = data1.Country.to_list()

# Getting the coordinates of the countries on the map from the location.csv file
data2 = pandas.read_csv("location.csv")
x = data2.x.to_list()
y = data2.y.to_list()

# list of gotten by the player
gotten_countries = [ ]
number_of_countries = len(data1.Country)

# Track user Score
score = 0

# RBG color coordinates for the country name
color = [(208, 154, 108),(197, 139, 153), (239, 210, 220), (157, 89, 58), (136, 169, 190), (146, 70, 87), (229, 198, 124), (142, 174, 155), (193, 99, 81), (186, 93, 107), (230, 167, 180), (236, 171, 158), (68, 126, 90), (86, 154, 114), (129, 34, 51), (81, 109, 132), (170, 205, 189), (133, 37, 25), (159, 204, 214), (78, 148, 166), (79, 29, 47), (86, 36, 17), (115, 122, 153), (16, 102, 57), (90, 77, 23)]

# Running the game as long as player hasn't gotten all the countries
while len(gotten_countries) < number_of_countries:
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    turtle.colormode(255)
    
    # changing turtle color to a random color from provided RBG coordinates for writing country name on map
    t.color(random.choice(color))
    
    # Getting user Input for the country name
    answer_country = screen.textinput(title="African Country Game", prompt=f"{score}/{number_of_countries} What's another Country?").title().strip()
    
    # Checking for Force EXIT Command
    if answer_country == "Exit":
        missing_countries = [country for country in c_data if country not in gotten_countries ]
        break
    
    if answer_country in c_data and answer_country not in gotten_countries:
        # Getting the index number of the country to match the location data
        index = c_data.index(answer_country)
        
        # Track user score
        score += 1
        
        # adding correct country names to the list of gotten countries        
        gotten_countries.append(answer_country)
        
        # Changing location of the turtle to country's position on the map
        t.goto(x[index], y[index])
        
        # reducing the font size if the name of the country is above 10 characters
        if len(answer_country) > 10:
            t.write(f"{answer_country}", False, "Center", ("Courier", 6, "normal"))
        else:
            t.write(f"{answer_country}", False, "Center", ("Courier", 10, "normal"))

# Creating new csv file of countries not mentioned
new_data = pandas.DataFrame(missing_countries)
new_data.to_csv("Countries_to_learn.csv")

#            #  OR

# with open("Countries_to_learn.csv", 'w') as new_data:
#     for country in missing_countries:
#         new_data.write(f'{country}\n')

turtle.mainloop()