# import statements
import pygame, sys
from pygame.locals import *

# initialize pygame
pygame.init()

# clock, frame rate
FPS = 60
clock = pygame.time.Clock()

# screen dimensions/aspect ratios
display_info = pygame.display.Info()
display_width = display_info.current_w
display_height = display_info.current_h
aspect_ratio = display_width / display_height # aspect ratio is width / height. If you have a 16:9 aspect ratio

# screen - the entire pygame window - resize the display to the size of this window
green_mode = (int(aspect_ratio * display_height / 2), int(display_height / 2))
green = pygame.display.set_mode(green_mode, pygame.RESIZABLE)
# internal game resolution: blue rectangle
blue_mode = (int(aspect_ratio * 250), 250)
blue = pygame.Surface(blue_mode) # display - the surface you render all game elements onto

# load images: red rectangle
pikachu_img = pygame.image.load("pikachu.png").convert_alpha()
pixel_grid = pygame.image.load("pixel_grid.png")

# game loop
while True:
    # exit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # color elements on pygame window
    green.fill((0,150,0)) # fill entire window green
    blue.fill((0, 100, 200))  # smaller blue rectangle

    # mouse position ratio
    window_width, window_height = pygame.display.get_window_size()
    screen_display_ratio_x = blue.get_width()/window_width
    screen_display_ratio_y = blue.get_height()/window_height
    
    mouse_screen_pos = pygame.mouse.get_pos()
    mouse_grid_coords = list(mouse_screen_pos) # (x,y) mouse position

    # would need to write these lines of code if you want mouse position on the blue display, since we resized it by a certain scale.
    '''mouse_grid_coords[0] *= screen_display_ratio_x
    mouse_grid_coords[1] *= screen_display_ratio_y'''

    # display the pikachu image, with a red background
    blue.blit(pikachu_img, (20,20))
    green.blit(pikachu_img, (200,200))
    green.blit(pikachu_img, (600,500))

    blue.blit(pixel_grid, (300,100))

    #pygame.draw.circle(blue, (255,0,0), mouse_display_coordmouse_grid_coords, 5)

    # SCALE and RENDER (blit) blit blue onto green
    #scaled = pygame.transform.scale(blue, green.get_size())
    scaled = pygame.transform.scale(blue, (mouse_grid_coords[0],mouse_grid_coords[1])) # might need to adjust mouse coordinates using display ratio if working with a smaller resolution
    green.blit(scaled, (0,0))

    # display all, ticks.
    pygame.display.update()
    clock.tick(FPS)