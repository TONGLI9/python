# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 09:08:54 2018

@author: gy18tl
"""

import random

class Agent(object): 
    def __init__(self,environment,agents):
        self.environment = environment
        self.store = 0
        self.x = random.randint(0,299)
        self.y = random.randint(0,299)
        self.agents = agents
        
    # move agent randomly
    def move(self):
        if random.random() < 0.5:
            self.x = (self.x + 1) % 300
        else:
            self.x = (self.x - 1) % 300

        if random.random() < 0.5:
            self.y = (self.y + 1) % 300
        else:
            self.y = (self.y - 1) % 300 
            
    # agent eats environemt
    def eat(self): 
       if  self.environment[self.y][self.x] > 20:
           self.environment[self.y][self.x] -= 20
           self.store += 20
     
    #agent will search for close neighbours, and share resources with them
    def share_with_neighbours(self,neighbourhood):
        for agent in self.agents:
            dist = self.distance_between(agent) 
            if dist <= neighbourhood:
                     sum = self.store + agent.store
                     ave = sum /2
                     self.store = ave
                     agent.store = ave
                     #print("sharing " + str(dist) + " " + str(ave))
   
    #Calculate and return the distance between self and agent.
    def distance_between(self, agent):
        return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5
  
      
    
           