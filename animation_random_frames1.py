# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 01:26:24 2018

@author: dhl
"""
import agentframework
import random
#import operator

import matplotlib
matplotlib.use('TkAgg')

import matplotlib.pyplot
import matplotlib.animation 
import csv
import tkinter
import matplotlib.backends.backend_tkagg


def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a.x - agents_row_b.x)**2) + 
    ((agents_row_a.y - agents_row_b.y)**2))**0.5
            

num_of_agents = 10
num_of_iterations = 100
agents = []
neighbourhood = 20

###create environment 

environment = []
f = open('in.txt')
reader = csv. reader(f,quoting=csv.QUOTE_NONNUMERIC)
for row in f:
    parsed_line = str.split(row,",")
    rowlist = []
    for value in parsed_line:
        rowlist.append(int(value))
        
    environment.append(rowlist)
    
f.close()

fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])



#ax.set_autoscale_on(False)

# Make the agents.
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment,agents))
carry_on = True	


    
# Move the agents.
#for j in range(num_of_iterations):
    #for i in range(num_of_agents):
        #agents[i].move()
        #agents[i].eat()
#for i in range(num_of_agents):
#    agents[i].move()
#    agents[i].eat()
#    agents[i].share_with_neighbours(neighbourhood)
    
    



for agents_row_a in agents:
    for agents_row_b in agents:
        distance = distance_between(agents_row_a, agents_row_b)
   

    
#for i in range(num_of_agents):
#        matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
#        #print(agents[i][0],agents[i][1])

# uodate the frame before next step and move the agents
def update(frame_number):
    
    fig.clear()   
    global carry_on
    matplotlib.pyplot.xlim(0, 99)
    matplotlib.pyplot.ylim(0, 99)
    matplotlib.pyplot.imshow(environment)
    
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].x, agents[i].y)
        #print("frame",frame_number)

    # to stop the agents when it satisfy the condition    
    if random.random() < 0.1:
        carry_on = False
        print("stopping condition")
  
		
def gen_function(b = [0]):
    a = 0
    global carry_on #Not actually needed as we're not assigning, but clearer
    while (a < 10) & (carry_on == True):
        yield a			# Returns control and waits next call.
        a = a + 1


#animation = matplotlib.animation.FuncAnimation(fig, update, interval=1, repeat=False, frames=10)
#animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)

#def run():
#    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
#    canvas.draw()
 
animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)    
#animation = matplotlib.animation.FuncAnimation(fig, update, frames=20, repeat=False)    
#root = tkinter.Tk() 
#root.wm_title("Model")
#canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
#canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
#
#
#    
#tkinter.mainloop()