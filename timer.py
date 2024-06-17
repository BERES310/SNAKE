import time
import pygame
import math

ALIGNMENT = "center"
WHITE = (255, 255, 255)
FONT = None 

class Timer:
    def __init__(self,screen):
        self.start_time = time.time()
        self.screen_rect = screen.get_rect()
        self.screen=screen
        self.licznik = 0

        pygame.font.init()
        self.font = pygame.font.SysFont("Arial", 16)

    def draw(self):
        current_time=time.time()
        #calosc czasu:
        roznicaCalosc=current_time-self.start_time
        
        min=int(roznicaCalosc//60)
        ms = roznicaCalosc % 1
        ms *= 10
        ms = int(ms)
        sek =  int((math.floor(roznicaCalosc)) - min*60)
    
        self.licznik = sek
        time_text = f"Time: {min}:{sek}:{ms}"
        self.render_text(time_text, (self.screen_rect.centerx, 70))
        # Add code to draw the scoreboard on the screen
        
    def render_text(self, text, pos):
        rendered_text = self.font.render(text, True, WHITE)
        text_rect = rendered_text.get_rect(center=pos)
        self.screen.blit(rendered_text, text_rect)

    def reset(self):
        self.start_time = time.time()
        
    