import pygame
import random
import GameSettings
import time



class Food(pygame.sprite.Sprite):
    def __init__(self, walls, scoreboard, game_settings, n=1):
        super().__init__()
        self.screen_width = game_settings.screen_width
        self.screen_height = game_settings.screen_height
        self.walls = walls
        self.type = 0


        self.init_time = time.time()
        #randomowa dlugosc zycia kazdego owocu
        self.lengthOfLife = random.randrange(5,10,1)
        #self.lengthOfLife = 5
        #na sztywno - jedno z dwoch^
        

        # Ustawienie obrazów owoców do odpowiednich rozmiarów
        for key in game_settings.fruit_images:
            game_settings.fruit_images[key] = pygame.transform.scale(game_settings.fruit_images[key], (20, 20))
        
        self.image = pygame.Surface((20, 20))
        self.rect = self.image.get_rect()
        self.spawn_food(scoreboard, game_settings)

    def spawn_food(self, scoreboard, game_settings):
        
        
        #correct position - not spawning in the position of wall
        while True:
            self.rect.x = random.randrange(0, self.screen_width - self.rect.width, 20)
            self.rect.y = random.randrange(0, self.screen_height - self.rect.height, 20)

            collision = any(wall.rect.colliderect(self.rect) for wall in self.walls)
            if not collision:
                break

        self.generate_fruit_type(scoreboard, game_settings)

        """    def spawn_food(self, scoreboard, game_settings):
            num_fruits = random.randint(1, 3)
            for _ in range(num_fruits):
        while True:
            self.rect.x = random.randrange(0, self.screen_width - self.rect.width, 20)
            self.rect.y = random.randrange(0, self.screen_height - self.rect.height, 20)

            collision = any(wall.rect.colliderect(self.rect) for wall in self.walls)
            if not collision:
                break

        self.generate_fruit_type(scoreboard, game_settings)
        """

    


    def generate_fruit_type(self, scoreboard, game_settings):
        score = scoreboard.score
        if score == 0:
            los = random.randint(1, 65)
        elif score == 1:
            los = random.randint(1, 85)
        else:
            los = random.randint(1, 100)

        # Wybór typu owocu na podstawie losowej liczby
        if los <= 50:
            self.type = 1  # hot dog +1 size
        elif 50 < los < 66:
            self.type = 2  # potion +2 size
        elif 65 < los < 86:
            self.type = 3  # pizza -1 size
        elif 85 < los <= 100:
            self.type = 4  #brzoskwinka -2 size

        # Ustawienie obrazu na podstawie typu owocu
        self.image = game_settings.fruit_images[self.type]
    
    def check_time(self):
        current_time=time.time()
        roznicaCalosc=current_time-self.init_time

        if roznicaCalosc >= self.lengthOfLife:
            self.init_time = time.time()
            return True
        else:
            return False
        

    def draw(self, screen):
        screen.blit(self.image, self.rect)
