#code created by: Nicholas Brean
#Created on October 2017
#This code shows an animation of a guy walking


import ui

#!/usr/bin/python

import time

@ui.in_background

def run():
    #
    counter = 1
    while(counter <= 10):
        if counter == 1:
            view['image_animation_file'].image = ui.Image.named("./assets/sprites/walking_man_1.BMP")
        elif counter == 2:
            view['image_animation_file'].image = ui.Image.named("./assets/sprites/walking_man_2.BMP")
        elif counter == 3:
            view['image_animation_file'].image = ui.Image.named("./assets/sprites/walking_man_3.BMP")
        elif counter == 4:
            view['image_animation_file'].image = ui.Image.named("./assets/sprites/walking_man_4.BMP")
        elif counter == 5:
            view['image_animation_file'].image = ui.Image.named("./assets/sprites/walking_man_5.BMP")
        elif counter == 6:
            view['image_animation_file'].image = ui.Image.named("./assets/sprites/walking_man_6.BMP")
        elif counter == 7:
            view['image_animation_file'].image = ui.Image.named("./assets/sprites/walking_man_7.BMP")
        elif counter == 8:
            view['image_animation_file'].image = ui.Image.named("./assets/sprites/walking_man_8.BMP")
        elif counter == 9:
            view['image_animation_file'].image = ui.Image.named("./assets/sprites/walking_man_9.BMP")
        elif counter == 10:
            view['image_animation_file'].image = ui.Image.named("./assets/sprites/walking_man_10.BMP")
        
        counter = counter + 1
        time.sleep(0.1)
        
        view['image_animation_file'].x = view['image_animation_file'].x - 10
        if counter >= 10:
        	counter = 0
        	
        if view['image_animation_file'].x <= -200:
       	    view['image_animation_file'].x = 481

view = ui.load_view()
view.present('sheet')

run()
