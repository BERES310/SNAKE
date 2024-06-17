import pygame
from wall import Wall
import GameSettings



class Snake(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height, speed, game_settings, startPosX=300, startPosY=300):
        super().__init__()
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.direction = (1, 0)  # Initial direction: right
        self.segments = []  # List to store snake segments
        

        # Load head and segment images
        self.head_image = pygame.transform.scale(game_settings.head_image, (20, 20))
        self.segment_image = pygame.transform.scale(game_settings.segment_image, (20, 20))

        self.head = pygame.Rect(startPosX, startPosY, 20, 20)
        self.create_snake()
        self.move_left = False
        self.move_right = True  # Initially moving right
        self.move_up = False
        self.move_down = False
        self.speed = speed

    def create_snake(self):
        # Create initial snake segments
        for x in range(3):
            segment_rect = pygame.Rect(20 * x + self.head.x, self.head.y, 20, 20)
            self.segments.append(segment_rect)

    def move(self):
        if self.move_left:
            self.direction = (-1, 0)
        elif self.move_right:
            self.direction = (1, 0)
        elif self.move_up:
            self.direction = (0, -1)
        elif self.move_down:
            self.direction = (0, 1)

        # Move the snake
        for i in range(len(self.segments) - 1, 0, -1):
            self.segments[i].x = self.segments[i - 1].x
            self.segments[i].y = self.segments[i - 1].y

        # Move the head
        self.segments[0].x += self.direction[0] * self.speed
        self.segments[0].y += self.direction[1] * self.speed
        self.head.x += self.direction[0] * self.speed
        self.head.y += self.direction[1] * self.speed

    def up(self):
        if not self.move_down:
            self.move_up = True
            self.move_down = False
            self.move_left = False
            self.move_right = False

    def down(self):
        if not self.move_up:
            self.move_up = False
            self.move_down = True
            self.move_left = False
            self.move_right = False

    def left(self):
        if not self.move_right:
            self.move_up = False
            self.move_down = False
            self.move_left = True
            self.move_right = False

    def right(self):
        if not self.move_left:
            self.move_up = False
            self.move_down = False
            self.move_left = False
            self.move_right = True

    def draw(self, screen):
        # Draw the head
        screen.blit(self.head_image, self.segments[0])

        # Draw the rest of the snake
        for segment in self.segments[1:]:
            screen.blit(self.segment_image, segment)

    def extend(self):
        # Add a new segment to the snake
        new_segment_rect = pygame.Rect(self.segments[-1].x, self.segments[-1].y, 20, 20)
        self.segments.append(new_segment_rect)

    def delete(self):
        self.segments.pop()

    def delete_n(self, n):
        for _ in range(n):
            self.segments.pop()

    def extend_n(self, n):
        # Add new segments to the snake
        for _ in range(n):
            new_segment_rect = pygame.Rect(self.segments[-1].x, self.segments[-1].y, 20, 20)
            self.segments.append(new_segment_rect)

    def reset(self):
        self.head.x = 0
        self.head.y = 0
        self.direction = (1, 0)  # Initial direction: right

