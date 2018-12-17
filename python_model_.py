# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 01:26:24 2018

@author: gy18tl

"""
import agentframework
import random


import matplotlib
matplotlib.use('TkAgg')

import matplotlib.pyplot
import matplotlib.animation 
import csv
import tkinter
import matplotlib.backends.backend_tkagg
       

# set the parameters
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

#set up the figure
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])


# Make the agents.
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment,agents))

carry_on = True	

# uodate the frame before next step and move the agents
def update(frame_number):
    
    fig.clear()   #clear fig
    global carry_on
    matplotlib.pyplot.xlim(0, 299)
    matplotlib.pyplot.ylim(0, 299)
    matplotlib.pyplot.imshow(environment)
    
  #  move, eat and share the agent
  
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)
        
       
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].x, agents[i].y)
        #print("frame",frame_number)
        
# to stop the agents when it satisfy the condition    
    if random.random() < 0.001:
       carry_on = False
       print("stopping condition")
  
# Animate acting agents	
def gen_function(b = [0]):
    a = 0
    global carry_on 
    while (a < 100) & (carry_on) :
        yield a			# Returns control and waits next call.
        a = a + 1
        
# Animate acting agents
def run():
    global animation
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
    canvas.draw()
    
# build the main window.    
root = tkinter.Tk() 
root.wm_title("Model")

canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

# build the menu bar 
menu_bar = tkinter.Menu(root)
root.config(menu = menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label='Model',menu=model_menu)
model_menu.add_command(label ='Run model',command = run)
    
tkinter.mainloop()