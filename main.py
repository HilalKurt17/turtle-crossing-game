# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 17:18:47 2023

@author: Hilal
"""

from turtle import Screen;
import turtle
from obstacles import Obstacles, cars;

import time


class turtle_crossing_capstone_game():
    def __init__(self):
        
        self.screen = Screen();
        self.screen.bgcolor("papaya whip")
        self.screen.tracer(0)
        self.screen.screensize(600,600);
        self.screen.setworldcoordinates(-300, -300, 300, 300);
        self.obstacles = Obstacles();
        self.screen.listen();
        turtle.title("Turtle Crossing Game")
    # create cars with random coordinates
        self.cars = cars();
        self.Turtles = self.cars.Turtles; # create cars on the screen at the beginning
            
        self.screen.onkeypress(fun= self.obstacles.move_turtle_up, key="Up");
        self.game_on(True);
    
    def game_on(self,condition):
        self.new_car_counter = 0; # counter for adding new cars to the game
        self.turtle_heart = 3;
        self.crash = False;
        self.obstacles.level_game(); # write current level on the screen
        
        while condition:
            for i in self.Turtles: # move cars forward
                self.cars.move_car(i);

            for i in self.Turtles:
                # check whether car crash with the turtle or not
                if i.xcor() <= 15 and i.xcor() >= -15:
                    if i.distance(self.obstacles.turtle) <= 20:
                        self.crash = True;
                        break;

            if self.crash == True: # if there is a crash, decrease the turtle heart. If turtle heart is zero, finish the game
                self.turtle_heart -= 1;
                
                self.obstacles.turtle_hearts(self.turtle_heart); # decrease the turtle heart on the screen
                
                if self.turtle_heart < 0: # if heart of turtle is finished, finish the game  
                    self.obstacles.game_over();
                    break
                else:
                    self.crash = False; 
      
            # if turtle reaches the upper wall increase the level
            if self.obstacles.turtle.ycor() >= 300:
                self.obstacles.next_level(); # increase speed of the cars and level
   
            
            if self.new_car_counter % 3 == 0: # create new cars with new positions 
                self.cars.new_cars();   
            self.new_car_counter += 1;
            
            
            
            self.screen.update(); # update screen
            time.sleep(self.obstacles.speed) 
            self.Turtles = self.cars.delete_car(self.Turtles);
        self.screen.exitonclick();
    

    
turtle_crossing_capstone_game()