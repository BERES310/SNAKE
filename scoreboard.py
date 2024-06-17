import pygame.font

ALIGNMENT = "center"
WHITE = (255, 255, 255)
FONT = None  

class Scoreboard:
    def __init__(self, screen, ammountPlayers=1):
        self.score = 0
        if ammountPlayers != 1:
            self.score2 = 0
        self.get_score = 0
        self.screen = screen
        self.screen_rect = screen.get_rect()
        
        pygame.font.init()
        self.font = pygame.font.SysFont("Arial", 16)
        
        self.get_highestScore = self.read_high_score()
        

    def read_high_score(self):
        try:
            with open("score.txt", "r") as file:
                return int(file.read())
        except FileNotFoundError:
            return 0

    def increase_score(self, player=1):
        if player == 1:
            self.score += 1
        else:
            self.score2 += 1
    
    def increase_score_n(self,n, player=1):
        if player == 1:
            self.score += n
        else:
            self.score2 += n
                
    def reset(self):
        if self.score > self.get_score:
            self.get_score = self.score
        self.score = 0

    
    def render_text(self, text, pos):
        rendered_text = self.font.render(text, True, WHITE)
        text_rect = rendered_text.get_rect(center=pos)
        self.screen.blit(rendered_text, text_rect)

    def game_over(self):
        game_over_text = "GAME OVER!"
        self.render_text(game_over_text, self.screen_rect.center)
        


    def draw(self, screen, game_type):
        if game_type != 4:
            score_text = f"Score: {self.score}   High Score: {self.get_highestScore}"
            self.render_text(score_text, (self.screen_rect.centerx, 50))
            # Add code to draw the scoreboard on the screen
        
        #scoreboard for multiplayer
        else:
            score_text = f"Score P1: {self.score}   Score P2: {self.score2}"
            self.render_text(score_text, (self.screen_rect.centerx, 50))
            # Add code to draw the scoreboard on the screen
            