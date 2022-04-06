import turtle
import pandas as pd

FONT = '("Verdana",15, "normal")'

screen = turtle.Screen()
screen.setup(725, 491)
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

df = pd.read_csv("50_states.csv")

write_head = turtle.Turtle()
write_head.penup()
write_head.hideturtle()
write_head.color("black")

already_guessed = []
score = 0
while score < 50:
    answer = screen.textinput(f"{score} States found so far.", "Guess the name of a state.").title()
    if answer == "Exit":
        break
    result = df[df.state == answer]
    if len(result) > 0 and answer not in already_guessed:
        score += 1
        already_guessed.append(answer)
        write_head.goto(int(result.x), int(result.y))
        write_head.write(answer, FONT)


missed_states = df[~df.state.isin(already_guessed)]
missed_states.state.to_csv("missed_states")

