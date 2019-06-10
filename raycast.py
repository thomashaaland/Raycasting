import math
import pygame
import tkinter as tk
from tkinter import messagebox
import numpy as np

class wall(object):
    def __init__(self, color, pos1, pos2):
        self.color = color
        self.pos1 = pos1
        self.pos2 = pos2
        
    def pos(self):
        return self.pos1, self.pos2
    
    def draw(self, surface):
        pygame.draw.line(surface, self.color, self.pos1, self.pos2)

class ray(object):
    def __init__(self, color):
        self.color = color
    def draw(self, surface, walls):
        n_rays = 360
        phi = np.linspace(0,2*np.pi-2*np.pi/n_rays,n_rays)
        rays = [2*np.cos(phi), 2*np.sin(phi)]
        
        for i in range(0, len(rays[0])):
            x_1 = self.pos[0]
            y_1 = self.pos[1]
            x_2 = self.pos[0] + 2*rays[0][i]
            y_2 = self.pos[1] + 2*rays[1][i]
            dist_closest = [math.inf, math.inf]
            pygame.draw.line(surface, self.color, self.pos, (x_2, y_2))
            ray_x = 0
            ray_y = 0
            for wall in walls:
                x_3 = wall.pos()[0][0]
                y_3 = wall.pos()[0][1]
                x_4 = wall.pos()[1][0]
                y_4 = wall.pos()[1][1]
                num = (x_4-x_3)*(y_2-y_1)-(x_2-x_1)*(y_4-y_3)
                if num:
                    u = ((x_2-x_1)*(y_3-y_1)-(x_3-x_1)*(y_2-y_1))/num
                    t = -((x_3-x_1)*(y_4-y_3)-(x_4-x_3)*(y_3-y_1))/num
                    if (0 < u < 1) & (t > 0):
                        dist = [t*(x_2-x_1), t*(y_2-y_1)]
                        L_1 = [x_1 + dist[0], y_1 + dist[1]] 
                        if (np.dot(dist,dist) < np.dot(dist_closest,dist_closest)):
                            dist_closest = dist
                            ray_x = L_1[0]
                            ray_y = L_1[1]
            if ray_x**2 + ray_y**2:
                pygame.draw.line(surface, (150,150,150), self.pos, (ray_x, ray_y))

    def getmouse_pos(self, pos):
        self.pos = pos
            

def redrawWindow(surface, ray, walls):
    surface.fill((0,0,0))
    for wall in walls:
        wall.draw(surface)
    mouse_pos = pygame.mouse.get_pos()
    ray.getmouse_pos(mouse_pos)
    ray.draw(surface, walls)
    pygame.display.update()

def main():
    width = 680
    height = 476
    flag = True
    pygame.init()
    # walls:
    walls = [wall((255,255,255), (500,50), (300,350)),
             wall((255,255,255), (100,50), (300,350)),
             wall((255,255,255), (50,450), (600,450)),
             wall((255,255,255), (650,50), (650,450)),
             wall((255,255,255), (50,50), (60,100)),
             wall((255,255,255), (60,100), (0,100)),
             wall((255,255,255), (550,70), (250,100)),
             wall((255,255,255), (550,140), (250,100)),
             wall((255,255,255), (0,0), (width,0)),
             wall((255,255,255), (width,0), (width,height)),
             wall((255,255,255), (width,height), (0,height)),
             wall((255,255,255), (0,height), (0,0))]
    lsource = ray((255,255,255))
    win = pygame.display.set_mode((width,height))
    
    while flag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                flag = False
        redrawWindow(win, lsource, walls)

    
main()
