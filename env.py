import math
import pygame

class buildEnvironment:
    def __init__(self,MapDimensions):
        pygame.init()
        self.pointCloud = []
        self.externalMap = pygame.image.load('1.png')
        self.maph, self.mapw = MapDimensions
        self.mapWindowName = 'RRT path planning'
        pygame.display.set_caption(self.mapWindowName)
        self.map = pygame.display.set_mode((self.mapw, self.maph))
        self.map.blit(self.externalMap,(0,0))
        #Colors
        self.black = (0,0,0)
        self.grey = (70,70,70)
        self.blue = (0,0,189)
        self.Green = (0,198,0)
        self.red = (199, 0,0)
        self.white = (250,250,250)


    #helper functions

    #converts the sensor raw angel distance data to 
    #catesian coordinates
    def AD2pos(self, distance, angle, robotPosition):
        x = distance * math.cos(angle) + robotPosition[0]
        y = -distance * math.sin(angle) +robotPosition[1]
        return (int(x), int(y))



    #this method will take the raw data and use the add to pose to convert them into cartessian coordinates
    def dataStorage(self,data):
        print(len(self.pointCloud))
        print("the data ", data)
        if data != False:
            for element in data:
                point = self.AD2pos(element[0], element[1], element[2])
                #storing in pointcloud after checking the duplicates
                if point not in self.pointCloud:
                    self.pointCloud.append(point)

    def show_sensorData(self):
        self.infomap = self.map.copy()
        for point in self.pointCloud:
            self.infomap.set_at((int(point[0]), int(point[1])),(255,0,0))
            #will be drown in this map , by coloring the coresponding pixel to color red
