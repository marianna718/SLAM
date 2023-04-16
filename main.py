import env, sensors
import pygame
import pygame.event
import pygame.mouse
 
environment = env.buildEnvironment((600,1200))
environment.externalMap = environment.map.copy()
laser = sensors.LaserSensor(200, environment.externalMap, uncertainty=(0.5, 0.01))
environment.map.fill((0,0,0))
environment.infomap = environment.map.copy()

runing = True
while runing:
    sensorON = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runing = False
        if pygame.mouse.get_focused():
            sensorON = True
        elif not pygame.mouse.get_focused():
            sensorON = False

    if sensorON:
        #get the position 
        position = pygame.mouse.get_pos()
        #assign this pos to current pos
        laser.position = position
        sensor_data = laser.sense_obstacles()
        environment.dataStorage(sensor_data)
        environment.show_sensorData()
    environment.map.blit(environment.infomap,(0,0))
    pygame.display.update()
pygame.quit()




# version 1
# import env,sensors
# import pygame
# import math 

# environment = env.buildEnvironment((600,1200))
# running = True

# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running =False

#     pygame.display.update()
# pygame.quit()