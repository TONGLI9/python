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
import tkinter

num_of_agents = 10
num_of_iterations = 100
neighbourhood = 20
agents = []

###create environment 
environment = []
f = open('in.txt')
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
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)

#matplotlib.pyplot.xlim(0, 99)
#matplotlib.pyplot.ylim(0, 99)
#matplotlib.pyplot.imshow(environment)
	

for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x, agents[i].y)
#matplotlib.pyplot.show()

#caculate distance
for agents_row_a in agents:
    for agents_row_b in agents:
        distance = distance_between(agents_row_a, agents_row_b)
        

def update(frame_number):
    
    fig.clear()
    
    global carry_on
    
    matplotlib.pyplot.xlim(0, 99)
    matplotlib.pyplot.ylim(0, 99)
    matplotlib.pyplot.imshow(environment)
    
    for i in range(num_of_agents):
        agents[i].move()
        
  # stop the agents according to the conditions
    if random.random() < 0.1:
        carry_on = False
        print("stopping condition")
    
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
        print(agents[i][0],agents[i][1])
        

		
def gen_function(b = [0]):
    a = 0
    global carry_on #Not actually needed as we're not assigning, but clearer
    while (a < 10) & (carry_on) :
        yield a			# Returns control and waits next call.
        a = a + 1


#animation = matplotlib.animation.FuncAnimation(fig, update, interval=1, repeat=False, frames=10)
animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)

root = tkinter.Tk() 
root.wm_title("Model")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

def run():
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
    canvas.show()
    
tkinter.mainloop()