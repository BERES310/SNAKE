import pygame
import random
import snake


class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, width=10, height=10):
        super().__init__()
        self.rect = pygame.Rect(x, y, width, height)
        self.color = (0, 255, 0)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)


    def create_random_wall(screen_width, screen_height, snake):
        while True:
            smallerSize = random.randint(20, 40)
            largerSize = random.randint(100,300)

            posX = random.randint(0, screen_width)
            posY = random.randint(0, screen_height)

            #decyzja czy horyzontalnie czy wertykalnie
            #0-horyzontalnie, 1-wertykalnie
            decisionDir = random.randint(0,1)
            if decisionDir == 0:
                wallToAppend = Wall(posX, posY, largerSize,smallerSize)
                
            elif decisionDir == 1:
                wallToAppend = Wall(posX, posY, smallerSize, largerSize)
            
            #warunek przestania generowania nowych scian - sprawdzenie:
            for segment in snake.segments:
                if segment.colliderect(wallToAppend):
                    break
            break
        return wallToAppend


def create_wall(screen_width, screen_height, game_type, snake):
    #ramka:
    size_wall_frame=5
    walls = [
        Wall(0, 0, screen_width, size_wall_frame),  # Górna granica
        Wall(0, screen_height - size_wall_frame, screen_width, size_wall_frame),  # Dolna granica
        Wall(0, 0, size_wall_frame, screen_height),  # Lewa granica
        Wall(screen_width - size_wall_frame, 0, size_wall_frame, screen_height)  # Prawa granica
    ]
    
    #dodatkowe sciany - zalezne od trybu gry
    if game_type == 1:
        pass
    elif game_type == 2:
        pass    
    elif game_type == 3:
        ammountWalls= 3
        for i in range(ammountWalls):
            walls.append(Wall.create_random_wall(screen_width,screen_height, snake))
        pass
    return walls


    
