# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 17:25:25 2023

@author: Hilal
"""

from turtle import Turtle,Screen;

import random

obstacle_colors = ["firebrick", "deep pink", "dark green", "teal", "dark blue", "steel blue", "sea green", "maroon", "dark orchid"];


class cars(): # create cars with random coordinates
    def __init__(self):
        self.Turtles = [];
        for i in range(55): # create car at the beginning of the game
            self.Turtles.append(self.create_car(-300,700));
        
        
    def create_car(self,beginning_position,end_position): # create new car
        self.turtle = Turtle();
        self.turtle.penup()
        self.turtle.color(random.choice(obstacle_colors))
        self.turtle.shape("square")
        self.turtle.shapesize(1,2)
        self.turtle.hideturtle();
        self.turtle.setposition(random.randint(beginning_position,end_position), random.randint(-230,230))
        self.turtle.showturtle();
        self.turtle.setheading(180);
        return self.turtle
    
    def new_cars(self): # create car during the game
        self.Turtles.append(self.create_car(300,350));
            
    def total_cars(self): # return total cars
        return self.Turtles

    def move_car(self, i): # move cars forward
        i.forward(5);
    
    def delete_car(self,turtles): # delete cars which are out of game

        for i in turtles:
            x,y = i.position();
            if x<-300:
                i.hideturtle();
                turtles.remove(i);

        return turtles


class Obstacles():
    
    def __init__(self):
        
        image = "turtle_heart.gif";
        screen = Screen();
        screen.addshape(image);
        self.turtle = Turtle(); # create turtle object 
        self.turtle.penup();
        self.turtle.shape("turtle");
        self.turtle.shapesize(1);
        self.turtle.setheading(90);
        self.turtle.setpos(0,-290);
        self.turtle.color("dark green");
        
        # create writer turtle
        self.turtle2 = Turtle();
        self.turtle2.hideturtle();
        self.turtle2.penup();
        self.turtle2.color("black");
        self.level = 1;
        self.speed = 0.1;
       
        # turtle heart1
        self.turtle_h1 = Turtle(); # create turtle object 
        self.turtle_h1.penup();
        self.turtle_h1.shape(image);
        self.turtle_h1.setheading(90);
        self.turtle_h1.setpos(210,280);
        
        # turtle heart2
        self.turtle_h2 = Turtle(); # create turtle object 
        self.turtle_h2.penup();
        self.turtle_h2.shape(image);
        self.turtle_h2.setheading(90);
        self.turtle_h2.setpos(240,280);
        
        # turtle heart3
        self.turtle_h3 = Turtle(); # create turtle object 
        self.turtle_h3.penup();
        self.turtle_h3.shape(image);
        self.turtle_h3.setheading(90);
        self.turtle_h3.setpos(270,280);

    
    def move_turtle_up(self): # move forward
        self.turtle.forward(10)
        
    def game_over(self): # inform user when game is over.

        self.turtle2.setpos(-10,0);
        self.turtle2.write("GAME  OVER", align = "center",  font=('Arial', 20, 'bold'));
        return True
    
    def next_level(self): # increase level and increase the speed
        self.level += 1;
        self.speed -= 0.015;
        self.turtle.setpos(0,-290); # set turtle position at the beginning
        self.level_game();
        
    def level_game(self):   # write current level of the game
        self.turtle2.clear();
        self.turtle2.setpos(-260,270);
        self.turtle2.write("LEVEL: {0}".format(self.level), align = "center",  font=('Arial', 13, 'bold'));
    
    def turtle_hearts(self,turtle_heart): # decrease the turtle heart and check whether the game is finished or not.

        if turtle_heart == 1:
            self.turtle_h2.hideturtle();
            self.turtle.setpos(0,-290);

        
       
        elif turtle_heart == 2:
            self.turtle_h1.hideturtle();
            self.turtle.setpos(0,-290);

            
        else:
            self.turtle_h3.hideturtle();
           
            

   

            
      
       
        