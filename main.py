# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 17:18:47 2023

@author: Hilal
"""

from turtle import Screen;
from obstacles import Obstacles, cars;

import time
Turtles = [];

class turtle_crossing_capstone_game():
    def __init__(self):
        self.screen = Screen();
        self.screen.tracer(0)
        self.screen.screensize(600,600);
        self.screen.setworldcoordinates(-300, -300, 300, 300);
        self.obstacles = Obstacles();
        self.screen.listen();
        # create cars with random coordinates
        for i in range(50):
            self.cars = cars();
            Turtles.append(self.cars);
            
        self.screen.onkeypress(fun= self.obstacles.move_turtle_up, key="Up");
        self.game_on(True);
    
    def game_on(self,condition):
        
        self.crash = False;
        self.obstacles.level_game();
        
        while condition:
            for i in Turtles:
                self.cars.move_car(i);
            
            for i in Turtles:
               
                if i.xcor() <= 15 and i.xcor() >= -15:
                    if i.distance(self.obstacles.turtle) <= 23:
                        self.crash = True;
                        break;
            if self.crash == True:
                self.obstacles.game_over();
                break;
            if self.obstacles.turtle.ycor() >= 300:
                self.obstacles.next_level();
                self.obstacles.new_level(Turtles);
                
            self.screen.update();
            time.sleep(self.obstacles.speed)
        self.screen.exitonclick();
    

    
turtle_crossing_capstone_game()