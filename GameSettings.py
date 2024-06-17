import pygame
import sys
import random

class GameSettings:
    def __init__(self, screen_width=600, screen_height=600):
        
        self.screen_width = screen_width
        self.screen_height = screen_height

        self.max_num_fruits = 4
        self.current_ammount_fruits = self.max_num_fruits

        pygame.init()
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Snake Game")
        icon = pygame.image.load('photos/icon.jpg')
        pygame.display.set_icon(icon)
        
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)
        self.fontTitle = pygame.font.Font(None, 60)

        self.images = {}
        self.food_images = {}
        self.load_sounds()
        self.load_images()

        #starting visuals:
        startingBack = self.images['background_image1']
        self.background_image= pygame.transform.scale(startingBack, (self.screen_width, self.screen_height))
        self.head_image=self.images['head_image1'] 
        self.segment_image=self.images['segment_image1'] 
        #used in changing visuals:
        self.chosen_number_back = 1
        self.chosen_number_seg = 1
        self.chosen_number_head = 1
               
        self.choose_game_type()


    def choose_game_type(self):
        self.screen.fill((0, 0, 0))
        while True:
            menu_title = self.fontTitle.render("Welcome to SNAKE Game!", True, (0, 255, 0))
            menu_choose = self.font.render("Choose game mode:", True, (255, 255, 255))
            menu_mode1 = self.font.render("1. Single Player - Easy", True, (255, 255, 255))
            menu_mode2 = self.font.render("2. Single Player - Medium", True, (255, 255, 255))
            menu_mode3 = self.font.render("3. Single Player - Hard", True, (255, 255, 255))
            menu_mode4 = self.font.render("4. Multiplayer", True, (255, 255, 255))
            menu_mode5 = self.font.render("5. Instructions",True, (255,255,255))
            menu_mode6 = self.font.render("6. Changing Visuals",True, (255,255,255))

            self.screen.blit(menu_title, (35, 100))
            self.screen.blit(menu_choose, (150, 170))
            self.screen.blit(menu_mode1, (150, 220))
            self.screen.blit(menu_mode2, (150, 270))
            self.screen.blit(menu_mode3, (150, 320))
            self.screen.blit(menu_mode4, (150, 370))
            self.screen.blit(menu_mode5, (150, 420))
            self.screen.blit(menu_mode6, (150, 470))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        self.game_type = 1
                        self.change_rules()
                        return
                    elif event.key == pygame.K_2:
                        self.game_type = 2
                        self.change_rules()
                        return
                    elif event.key == pygame.K_3:
                        self.game_type = 3
                        self.change_rules()
                        return
                    elif event.key == pygame.K_4:
                        self.game_type = 4
                        self.change_rules()
                        return
                    elif event.key == pygame.K_5:
                        self.game_type = 5
                        self.instructions()
                        return
                    elif event.key == pygame.K_6:
                        self.game_type = 6
                        self.changing_window()
                        self.choose_game_type()
                        return
    
    def instructions(self):
        self.screen.fill((0, 0, 0))
        instructions_image=pygame.image.load('photos/instr.jpg')
        while True:

            instructions_title = self.fontTitle.render("Instructions", True, (0, 255, 0))
            
            self.screen.blit(instructions_image, (0, 100))  # Rysowanie obrazu na współrzędnych (100, 100)
            self.screen.blit(instructions_title, (165, 50))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        self.choose_game_type()
                        return


    def change_rules(self):
        if self.game_type == 1:# Easy
            self.speed = 10
            
        elif self.game_type == 2:# Medium
            self.speed = 10
            
        elif self.game_type == 3:# Hard
            self.speed = 10
            
        elif self.game_type == 4:# Multiplayer
            self.speed = 10  

    def change_ammount_foods(self):
        self.current_ammount_fruits = random.randint(1,self.max_num_fruits)


    def load_sounds(self):
        try:
            self.sound_picking = pygame.mixer.Sound('picking.wav')
            self.sound_picking.set_volume(0.1)
            self.sound_picking.fadeout(1000)

            self.sound_background = pygame.mixer.Sound('music.mp3')
            self.sound_background.set_volume(0.15)

            self.sound_fail = pygame.mixer.Sound('fail.mp3')
            self.sound_fail.set_volume(0.2)
        except pygame.error as e:
            print(f"Error loading sound: {e}")
            self.sound_picking = None
            self.sound_background = None
            self.sound_fail = None

    def load_images(self):
        self.images['background_image1'] = pygame.image.load('photos/doge.jpg')
        self.images['background_image2'] = pygame.image.load('photos/sunset.jpg')
        self.images['background_image3'] = pygame.image.load('photos/back1.png')
        self.images['background_image4'] = pygame.image.load('photos/back2.png')
        self.images['background_image5'] = pygame.image.load('photos/milky-way.jpg')
        self.images['segment_image1'] = pygame.image.load('photos/snake_segment/segment2.png')
        self.images['segment_image2'] = pygame.image.load('photos/snake_segment/segment4.png')
        self.images['segment_image3'] = pygame.image.load('photos/snake_segment/segment3.png')
        self.images['segment_image_special1'] = pygame.image.load('photos/snake_segment/special1.png')
        self.images['segment_image_special2'] = pygame.image.load('photos/snake_segment/special2.png')
        self.images['head_image1'] = pygame.image.load('photos/snake_head/snake4.png')
        self.images['head_image2'] = pygame.image.load('photos/snake_head/snake5.png')
        self.images['head_image3'] = pygame.image.load('photos/snake_head/snake2.png')
        self.images['head_image4'] = pygame.image.load('photos/snake_head/snake3.png')
        self.images['head_image5'] = pygame.image.load('photos/snake_head/snake1.png')
        self.images['highlight'] = pygame.image.load('photos/highlight.jpg')

        # Ładowanie obrazów owoców
        self.fruit_images = {
            1: pygame.image.load('photos/foods/hot_dog.png'),
            2: pygame.image.load('photos/foods/potion.png'),
            3: pygame.image.load('photos/foods/pizza.png'),
            4: pygame.image.load('photos/foods/brzoskwinka.png')
        }

        return self.images
    

    #main window for changing visuals:
    def changing_window(self):
        self.screen.fill((0, 0, 0))

        background_image1= pygame.transform.scale(self.images['background_image1'], (50,50))
        background_image2= pygame.transform.scale(self.images['background_image2'], (50,50))
        background_image3= pygame.transform.scale(self.images['background_image3'], (50,50))
        background_image4= pygame.transform.scale(self.images['background_image4'], (50,50))
        background_image5= pygame.transform.scale(self.images['background_image5'], (50,50))

        segment_image1= pygame.transform.scale(self.images['segment_image1'], (50,50))
        segment_image2= pygame.transform.scale(self.images['segment_image2'], (50,50))
        segment_image3= pygame.transform.scale(self.images['segment_image3'], (50,50))
        segment_image_special1= pygame.transform.scale(self.images['segment_image_special1'], (50,50))
        segment_image_special2= pygame.transform.scale(self.images['segment_image_special2'], (50,50))

        head_image1= pygame.transform.scale(self.images['head_image1'], (50,50))
        head_image2= pygame.transform.scale(self.images['head_image2'], (50,50))
        head_image3= pygame.transform.scale(self.images['head_image3'], (50,50))
        head_image4= pygame.transform.scale(self.images['head_image4'], (50,50))
        head_image5= pygame.transform.scale(self.images['head_image5'], (50,50))



        while True:

            ###printing choosen ones:
            #background:
            if self.chosen_number_back == 1:
                highBack = (75, 145)
            elif self.chosen_number_back == 2:
                highBack = (175, 145)
            elif self.chosen_number_back == 3:
                highBack = (275, 145)
            elif self.chosen_number_back == 4:
                highBack = (375, 145)
            elif self.chosen_number_back == 5:
                highBack = (475, 145)

            #seg:
            if self.chosen_number_seg == 1:
                highSeg = (75, 345)
            elif self.chosen_number_seg == 2:
                highSeg = (175, 345)
            elif self.chosen_number_seg == 3:
                highSeg = (275, 345)
            elif self.chosen_number_seg == 4:
                highSeg = (375, 345)
            elif self.chosen_number_seg == 5:
                highSeg = (475, 345)

            #head:
            if self.chosen_number_head == 1:
                highHead = (75, 495)
            elif self.chosen_number_head == 2:
                highHead = (175, 495)
            elif self.chosen_number_head == 3:
                highHead = (275, 495)
            elif self.chosen_number_head == 4:
                highHead = (375, 495)
            elif self.chosen_number_head == 5:
                highHead = (475, 495)

            #printing highlighter
            self.screen.blit(self.images['highlight'], highBack)
            self.screen.blit(self.images['highlight'], highSeg)
            self.screen.blit(self.images['highlight'], highHead)
            
            changing_title = self.fontTitle.render("Changing visuals", True, (0, 255, 0))
            
            #backgrounds:
            changing_mode1 = self.font.render("Change background:", True, (0, 255, 0))
            changing_back1 = self.font.render("1.", True, (0, 255, 0))
            changing_back2 = self.font.render("2.", True, (0, 255, 0))
            changing_back3 = self.font.render("3.", True, (0, 255, 0))
            changing_back4 = self.font.render("4.", True, (0, 255, 0))
            changing_back5 = self.font.render("5.", True, (0, 255, 0))

            self.screen.blit(changing_title, (135, 30))
            self.screen.blit(changing_mode1, (60, 80))
            self.screen.blit(changing_back1, (100, 110))
            self.screen.blit(changing_back2, (200, 110))
            self.screen.blit(changing_back3, (300, 110))
            self.screen.blit(changing_back4, (400, 110))
            self.screen.blit(changing_back5, (500, 110))
            
            self.screen.blit(background_image1, (80, 150))
            self.screen.blit(background_image2, (180, 150))
            self.screen.blit(background_image3, (280, 150))
            self.screen.blit(background_image4, (380, 150))
            self.screen.blit(background_image5, (480, 150))

            back1_rect = background_image1.get_rect()
            back1_rect.topleft = (80, 150)  
            back2_rect = background_image2.get_rect()
            back2_rect.topleft = (180, 150)
            back3_rect = background_image3.get_rect()
            back3_rect.topleft = (280, 150)  
            back4_rect = background_image4.get_rect()
            back4_rect.topleft = (380, 150)
            back5_rect = background_image5.get_rect()
            back5_rect.topleft = (480, 150)


            #segments:
            changing_mode2 = self.font.render("Change segments:", True, (0, 255, 0))

            self.screen.blit(changing_mode2, (60, 270))
            self.screen.blit(changing_back1, (100, 300))
            self.screen.blit(changing_back2, (200, 300))
            self.screen.blit(changing_back3, (300, 300))
            self.screen.blit(changing_back4, (400, 300))
            self.screen.blit(changing_back5, (500, 300))

            self.screen.blit(segment_image1, (80, 350))
            self.screen.blit(segment_image2, (180, 350))
            self.screen.blit(segment_image3, (280, 350))
            self.screen.blit(segment_image_special1, (380, 350))
            self.screen.blit(segment_image_special2, (480, 350))

            seg1_rect = segment_image1.get_rect()
            seg1_rect.topleft = (80, 350)  
            seg2_rect = segment_image2.get_rect()
            seg2_rect.topleft = (180, 350)
            seg3_rect = segment_image3.get_rect()
            seg3_rect.topleft = (280, 350)  
            seg4_rect = segment_image_special1.get_rect()
            seg4_rect.topleft = (380, 350)
            seg5_rect = segment_image_special2.get_rect()
            seg5_rect.topleft = (480, 350)

            #heads:
            changing_mode3 = self.font.render("Change Head:", True, (0, 255, 0))

            self.screen.blit(changing_mode3, (60, 420))
            self.screen.blit(changing_back1, (100, 450))
            self.screen.blit(changing_back2, (200, 450))
            self.screen.blit(changing_back3, (300, 450))
            self.screen.blit(changing_back4, (400, 450))
            self.screen.blit(changing_back5, (500, 450))

            self.screen.blit(head_image1, (80, 500))
            self.screen.blit(head_image2, (180, 500))
            self.screen.blit(head_image3, (280, 500))
            self.screen.blit(head_image4, (380, 500))
            self.screen.blit(head_image5, (480, 500))

            head1_rect = head_image1.get_rect()
            head1_rect.topleft = (80, 500)  
            head2_rect = head_image2.get_rect()
            head2_rect.topleft = (180, 500)
            head3_rect = head_image3.get_rect()
            head3_rect.topleft = (280, 500)  
            head4_rect = head_image4.get_rect()
            head4_rect.topleft = (380, 500)
            head5_rect = head_image5.get_rect()
            head5_rect.topleft = (480, 500)


            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        self.choose_game_type()
                        return
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    
                    #klikniecia background
                    if back1_rect.collidepoint(event.pos):
                        self.set_background_image(self.images['background_image1'])
                        self.chosen_number_back = 1
                        return
                    elif back2_rect.collidepoint(event.pos):
                        self.set_background_image(self.images['background_image2'])
                        self.chosen_number_back = 2
                        return
                    elif back3_rect.collidepoint(event.pos):
                        self.set_background_image(self.images['background_image3'])
                        self.chosen_number_back = 3
                        return
                    elif back4_rect.collidepoint(event.pos):
                        self.set_background_image(self.images['background_image4'])
                        self.chosen_number_back = 4
                        return
                    elif back5_rect.collidepoint(event.pos):
                        self.set_background_image(self.images['background_image5'])
                        self.chosen_number_back = 5
                        return

                    #klikniecia seg
                    elif seg1_rect.collidepoint(event.pos):
                        self.choose_seg(self.images['segment_image1'])
                        self.chosen_number_seg = 1
                        return
                    elif seg2_rect.collidepoint(event.pos):
                        self.choose_seg(self.images['segment_image2'])
                        self.chosen_number_seg = 2
                        return
                    elif seg3_rect.collidepoint(event.pos):
                        self.choose_seg(self.images['segment_image3'])
                        self.chosen_number_seg = 3
                        return    
                    elif seg4_rect.collidepoint(event.pos):
                        self.choose_seg(self.images['segment_image_special1'])
                        self.chosen_number_seg = 4
                        return
                    elif seg5_rect.collidepoint(event.pos):
                        self.choose_seg(self.images['segment_image_special2'])
                        self.chosen_number_seg = 5
                        return
                    
                    #klikniecia head
                    elif head1_rect.collidepoint(event.pos):
                        self.choose_head(self.images['head_image1'])
                        self.chosen_number_head = 1
                        return
                    elif head2_rect.collidepoint(event.pos):
                        self.choose_head(self.images['head_image2'])
                        self.chosen_number_head = 2
                        return
                    elif head3_rect.collidepoint(event.pos):
                        self.choose_head(self.images['head_image3'])
                        self.chosen_number_head = 3
                        return
                    elif head4_rect.collidepoint(event.pos):
                        self.choose_head(self.images['head_image4'])
                        self.chosen_number_head = 4
                        return
                    elif head5_rect.collidepoint(event.pos):
                        self.choose_head(self.images['head_image5'])
                        self.chosen_number_head = 5
                        return
                    
    def set_background_image(self, image):
        try:
            self.background_image = pygame.transform.scale(image, (self.screen_width, self.screen_height))
        except pygame.error as e:
            print(f"Error loading background image: {e}")
            self.background = None

    def choose_seg(self, image):
        try:
            self.segment_image = pygame.transform.scale(image, (20,20))
        except pygame.error as e:
            print(f"Error loading seg image: {e}")
            self.segment_image = None

    def choose_head(self, image):
        try:
            self.head_image = pygame.transform.scale(image, (20,20))
        except pygame.error as e:
            print(f"Error loading head image: {e}")
            self.head_image = None

