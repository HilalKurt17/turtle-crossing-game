# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 17:25:25 2023

@author: Hilal
"""

from turtle import Turtle;
import random

obstacle_colors = ["medium aquamarine", "hot pink", "pale violet red", "gold", "light blue", "light steel blue", "powder blue", "light sky blue", "pale green"];


class cars(Turtle):
    def __init__(self):
        super().__init__();
        self.penup()
        self.color(random.choice(obstacle_colors));
        self.shape("square");
        self.shapesize(1,2)
        self.hideturtle();
        self.setposition(random.randint(300,2500), random.randint(-250,250))
        self.showturtle();
        self.setheading(180);

    def move_car(self, i):
        i.forward(10);


class Obstacles():
    def __init__(self):
        self.turtle = Turtle();
        self.turtle.penup();
        self.turtle.shape("turtle");
        self.turtle.shapesize(1);
        self.turtle.setheading(90);
        self.turtle.setpos(0,-290);
        self.turtle.color("dark green");
        
        self.turtle2 = Turtle();
        self.turtle2.hideturtle();
        self.turtle2.penup();
        self.turtle2.color("black");
        self.level = 1;
        self.speed = 0.1;
    
    def move_turtle_up(self):
        self.turtle.forward(10)
        
    def game_over(self):
        self.turtle2.setpos(-10,0);
        self.turtle2.write("GAME  OVER", align = "center",  font=('Arial', 20, 'bold'));
    
    def next_level(self):
        self.level += 1;
        self.speed -= 0.01;
        self.level_game();
        
    def level_game(self):
        self.turtle2.clear();
        self.turtle2.setpos(-260,270);
        self.turtle2.write("LEVEL: {0}".format(self.level), align = "center",  font=('Arial', 13, 'bold'));
    
    def new_level(self, Turtles):
        self.turtle.setpos(0,-290);
        for i in Turtles:
            i.setposition(random.randint(300,2500), random.randint(-250,250))

