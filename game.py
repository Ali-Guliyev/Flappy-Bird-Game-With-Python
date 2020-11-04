import turtle
from turtle import *
import time
import random
import winsound
import pickle

# screen
wn = Screen()
wn.title("Flappy Bird by @ali.guliyevoo7")
wn.setup(500, 600) # (x and y coordinates)
wn.bgpic('background.gif')
wn.bgcolor("lightblue")
wn.tracer(0)

# register the shape
wn.register_shape("flappy-bird.gif")
wn.register_shape("flappy-bird-jump.gif")
# register shape
	
# player
player = Turtle() 
player.speed(0)
player.penup() 
player.color("blue")
player.shape('flappy-bird.gif')
player.goto(-200, 0)
player.dx = 0 
player.dy = 1

# pipes
# random y
y = random.randint(-300, -200)

pipe1_top = Turtle()
pipe1_top.speed(0)
pipe1_top.penup()
pipe1_top.color("green")
pipe1_top.shape("square")
pipe1_top.shapesize(18, 3)
pipe1_top.goto(500, y)

pipe1_top.value = 1
	 
y_2 = y + 440

pipe1_bottom = Turtle()
pipe1_bottom.speed(0)
pipe1_bottom.penup()
pipe1_bottom.color("green")
pipe1_bottom.shape("square")
pipe1_bottom.shapesize(18, 3)
pipe1_bottom.goto(500, y_2)

# pipe 2 bottom
y = random.randint(-300, -200)

pipe2_top = Turtle()
pipe2_top.speed(0)
pipe2_top.penup()
pipe2_top.color("green")
pipe2_top.shape("square")
pipe2_top.shapesize(18, 3)
pipe2_top.goto(900, y)

pipe2_top.value = 1

y_2 = y + 440

pipe2_bottom = Turtle()
pipe2_bottom.speed(0)
pipe2_bottom.penup()
pipe2_bottom.color("green")
pipe2_bottom.shape("square")
pipe2_bottom.shapesize(18, 3)
pipe2_bottom.goto(900, y_2)

# pipe speed
pipe_speed = -2

# game over, start again
lose_w = Turtle()
lose_w.speed(0)
lose_w.penup()
lose_w.color("green")
lose_w.hideturtle()
lose_w.goto(-200, 0)
lose_w.write("", font=("Arial", 50, "normal"))

# score
player.score = 0

score_w = Turtle()
score_w.speed(0)
score_w.penup()
score_w.color("white")
score_w.hideturtle()
score_w.goto(-20, 50)
score_w.write(f"{player.score}", font=("Arial", 60, "normal"))
	
# high score
player.high_score = player.score

high_score_w = Turtle()
high_score_w.speed(0)
high_score_w.penup()
high_score_w.color("yellow")
high_score_w.hideturtle()
high_score_w.goto(120, 250)
high_score_w.write(f"HI: {player.high_score}", font=("Arial", 30, "normal"))

def game():
	global pipe_speed
	global c
	

	# Gravity variable
	gravity = 0.2

	# Functions
	def go_up():
		player.dy -= 7

		winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
		
		player.shape("flappy-bird-jump.gif")

		
	def put_to_screen():
		global pipe_speed
		global gravity
	
		pipe1_top.showturtle()
		pipe1_bottom.showturtle()
		pipe2_top.showturtle()
		pipe2_bottom.showturtle()
		pipe_speed = -2
		player.showturtle()
		wn.onkeypress(go_up, "space")
		wn.onkeypress(go_up, "Up")
		player.sety(0)
		gravity = 0.4
		player.dy = 0

	# losing
	def lose():
		global gravity
		global score
		global pipe_speed
		
		# Reset the speed
		pipe_speed = -0.01

		# Game Over
		lose_w.goto(-120, -100)
		lose_w.color("white")
		lose_w.write("GAME OVER", font=("Arial", 30, "normal"))
		
		# update the game
		wn.update()
		time.sleep(1.3)
		
		# Reset The Score
		player.score = 0
		score_w.clear()
		score_w.write(f"{player.score}", font=("Arial", 60, "normal"))
		
		# Move pipes Back
		pipe1_top.setx(500)
		pipe1_bottom.setx(500)
		pipe2_top.setx(900)
		pipe2_bottom.setx(900)
		
		# Player
		player.sety(0)
		player.dy = 0
		gravity = 0.4
		
		# Speed of pipes
		pipe_speed = -2
		lose_w.clear()
		lose_w.write("", font=("Arial", 30, "normal"))
		
		# return the shape of the bird to the normal shape ( image, gif )
		player.shape("flappy-bird.gif")
		
		# delete everything
		pipe1_top.hideturtle()
		pipe1_bottom.hideturtle()
		pipe2_top.hideturtle()
		pipe2_bottom.hideturtle()
		player.hideturtle()
		pipe_speed = 0
		
		# start the game again if you click to "space" button
		wn.listen()
		wn.onkeypress(put_to_screen, "space")
		wn.onkeypress(put_to_screen, "Up")
		
	def high_score():
		# Check if player.score is more than player.high_score
		if player.score > player.high_score:
			player.high_score = player.score
			high_score_w.clear()
			high_score_w.write(f"HI: {player.high_score}", font=("Arial", 30, "normal"))
		
		

		
	# Keyboard binding
	wn.listen()
	wn.onkeypress(go_up, "space")
	wn.onkeypress(go_up, "Up")

	# Main game loop
	while True: 
		# Pause
		time.sleep(0.01)
		
		# update the screen
		wn.update()
		
		# Add gravity
		player.dy += gravity
		
		# Fall player ( Moving to the bottom )
		player.sety(player.ycor() - player.dy)
		
		# Move the pipes
		pipe1_top.setx(pipe1_top.xcor() + pipe_speed)
		pipe1_bottom.setx(pipe1_bottom.xcor() + pipe_speed)
		pipe2_top.setx(pipe2_top.xcor() + pipe_speed)
		pipe2_bottom.setx(pipe2_bottom.xcor() + pipe_speed)
		
		# Collisions between player and pipe
		# Pipe 1
		if pipe1_bottom.xcor() - 40 <= player.xcor() < pipe1_bottom.xcor() + 40 and player.ycor() > pipe1_bottom.ycor() - 190:
			lose()
			
		if pipe1_top.xcor() - 40 <= player.xcor() < pipe1_top.xcor() + 40 and player.ycor() < pipe1_top.ycor() + 190:
			lose()
			 
		if pipe2_bottom.xcor() - 40 <= player.xcor() < pipe2_bottom.xcor() + 40 and player.ycor() > pipe2_bottom.ycor() - 190:
			lose()
		
		if pipe2_top.xcor() - 40 <= player.xcor() < pipe2_top.xcor() + 40 and player.ycor() < pipe2_top.ycor() + 190:
			lose()
			
		# losing wall
		if player.ycor() <= -280:
			player.sety(-280)
			player.dy = 0

		
		# Collisions between player and wall
		if player.ycor() >= 290:
			player.sety(290)
			player.dy = 0


			
		# Return pipes to start
		y = random.randint(-300, -200)
		y_2 = y + 440
		
		if pipe1_top.xcor() < -300:
			pipe1_top.setx(500)
			pipe1_top.sety(y)
			
			pipe1_top.value = 1
			
		if pipe1_bottom.xcor() <= -300:
			pipe1_bottom.setx(500)
			pipe1_bottom.sety(y_2)
		
		y = random.randint(-300, -200)
		y_2 = y + 440
			
		if pipe2_top.xcor() < -300:
			pipe2_top.setx(500)
			pipe2_top.sety(y)
			
			pipe2_top.value = 1
			
		if pipe2_bottom.xcor() < -300:
			pipe2_bottom.setx(500)
			pipe2_bottom.sety(y_2)
		


		
		# increase the speed of pipes
		# scoring system
		if player.xcor() > pipe1_bottom.xcor():
			pipe_speed -= 0.01
			player.score += pipe1_top.value
			score_w.clear()
			score_w.write(f"{player.score}", font=("Arial", 60, "normal"))
			# print high score
			high_score()
				
			# update the score
			pipe1_top.value = 0

		if player.xcor() > pipe2_bottom.xcor():
			pipe_speed -= 0.01
			player.score += pipe2_top.value

			score_w.clear()
			score_w.write(f"{player.score}", font=("Arial", 60, "normal"))
			# print high score
			high_score()

			# update the score
			pipe2_top.value = 0

		# Change the animation of bird
		if player.dy > 0:
			player.shape("flappy-bird.gif")
			
		# if score = 10 animation...
		if player.score > 0 and player.score % 10 == 0:
			print(f"Congrats! You Got {player.score} points!")
			
		
		

# Start the game

def start_game():
	game()
	
wn.listen()
wn.onkeypress(start_game ,"space")
wn.onkeypress(start_game ,"Up")
	
		


wn.mainloop()