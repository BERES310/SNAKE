import pygame
import sys
from os import system
import random
import math

from snake import Snake
from food import Food
from scoreboard import Scoreboard
from wall import Wall
from GameSettings import GameSettings
from timer import Timer
from wall import create_wall

system("cls")
pygame.mixer.init()

# obiekty gry
game_settings = GameSettings()

snake = Snake(game_settings.screen_width, 
              game_settings.screen_height,
              game_settings.speed, 
              game_settings)  

if game_settings.game_type == 4:
    snake2 = Snake(game_settings.screen_width, 
                   game_settings.screen_height,
                   game_settings.speed,
                   game_settings,  
                   400, 400)  

walls = create_wall(game_settings.screen_width, 
                    game_settings.screen_height,
                    game_settings.game_type,
                    snake)

if game_settings.game_type != 4:
    scoreboard = Scoreboard(game_settings.screen)
else:
    scoreboard = Scoreboard(game_settings.screen, 2)

timer = Timer(game_settings.screen)


#poczatkowe owoce
food = [0] * random.randint(1, game_settings.max_num_fruits) 
for i in range(len(food)):
    food[i] = Food(walls, scoreboard,game_settings)

#sprawdzenie = []


# ta funkcja musi zostać w głównej części programu, aby nie definiować zmiennych, takich jak ekran, itp., jeszcze raz
def ask_to_continue():
    global snake, food, scoreboard, walls, game_settings
    try:
        global snake2
    except:
        pass  

    while True:
        game_settings.screen.fill((0, 0, 0))
        GAME_OVER_text = game_settings.font.render("GAME OVER", True, (255, 0, 0))
        continue_text = game_settings.font.render("Czy chcesz kontynuować? (t/n)", True, (255, 255, 255))
        game_settings.screen.blit(GAME_OVER_text, (150, 200))
        game_settings.screen.blit(continue_text, (150, 250))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                #print("Key pressed:", event.key, event.unicode)  
                if event.key == pygame.K_t:
                    del snake, food, scoreboard, walls
                    if game_settings.game_type == 4:
                        del snake2
                    
                    #nowy wybor trybu gry:
                    game_settings.sound_fail.stop()
                    game_settings.choose_game_type()
                    snake = Snake(game_settings.screen_width, 
                                game_settings.screen_height,
                                game_settings.speed,
                                game_settings)  

                    if game_settings.game_type == 4:
                        snake2 = Snake(game_settings.screen_width, 
                                    game_settings.screen_height,
                                    game_settings.speed,
                                    game_settings,  
                                    400, 400) 
                        
                    if game_settings.game_type != 4:
                        scoreboard = Scoreboard(game_settings.screen)
                    else:
                        scoreboard = Scoreboard(game_settings.screen, 2)

                    walls = create_wall(game_settings.screen_width, 
                                        game_settings.screen_height,
                                        game_settings.game_type,
                                        snake)
                    
                    food = [0] * random.randint(1, game_settings.max_num_fruits) 
                    for i in range(len(food)):
                        food[i] = Food(walls, scoreboard, game_settings)
                        
                    game_settings.sound_background.play(-1)
                    return True
                    
                elif event.key == pygame.K_n:
                    return False
            elif event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

#muzyka tlo
game_settings.sound_background.play(-1)

#################### main petla
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                snake.left()
            elif event.key == pygame.K_d:
                snake.right()
            elif event.key == pygame.K_w:
                snake.up()
            elif event.key == pygame.K_s:
                snake.down()
        #wariant multiplayer
            elif event.key == pygame.K_LEFT and game_settings.game_type==4:
                snake2.left()
            elif event.key == pygame.K_RIGHT and game_settings.game_type==4:
                snake2.right()
            elif event.key == pygame.K_UP and game_settings.game_type==4:
                snake2.up()
            elif event.key == pygame.K_DOWN and game_settings.game_type==4:
                snake2.down()
                
    # Wyczyść ekran
    game_settings.screen.fill((0, 0, 0))

    # Przesuń węża
    snake.move()
    try:
        snake2.move()
    except:
        pass

    # Sprawdź kolizje z jedzeniem - snake1
    
    for fruit in food:
        if snake.head.colliderect(fruit.rect):
            game_settings.sound_picking.play()
            if fruit.type == 1:
                if game_settings.game_type == 3:
                    scoreboard.increase_score_n(1)
                    del walls
                    walls = create_wall(game_settings.screen_width, 
                                        game_settings.screen_height,
                                        game_settings.game_type,
                                        snake)
                    snake.extend()
                else:
                    scoreboard.increase_score_n(1) 
                    snake.extend()
            if fruit.type == 2:
                scoreboard.increase_score_n(2) 
                snake.extend_n(2)
            if fruit.type == 3:
                scoreboard.increase_score_n(-1) 
                snake.delete()
            if fruit.type == 4:
                scoreboard.increase_score_n(-2)
                snake.delete_n(2)

            #usuwanie starego owoca
            food.remove(fruit)
            del fruit
            game_settings.change_ammount_foods()
            #tworzenie nowego owoca i dodanie go do food 
            #--> jeżeli jest mniej owoców niż current_ammount_fruits
            if len(food) < game_settings.current_ammount_fruits:
                diff = game_settings.current_ammount_fruits - len(food)
                for i in range(diff):
                    newFruit = Food(walls, scoreboard, game_settings)
                    food.append(newFruit)

    """ czesc Huberta
    saaprawdzenie.append(timer.licznik)
    if timer.licznik % 5 == 0:         
        if timer.licznik !=0:             
            pozycja=len(sprawdzenie)             
            if sprawdzenie[pozycja-1] != sprawdzenie[pozycja-2]:     
                if isinstance(food, list):  
                    for i in range(len(food)):          
                        food[i].spawn_food(scoreboard, game_settings)  
    
    """ 
             

    # Sprawdź kolizje z jedzeniem - snake2
    for fruit in food:
        if game_settings.game_type == 4:
            if snake2.head.colliderect(fruit.rect):
                game_settings.sound_picking.play()
                if fruit.type == 1:
                    # test - w wariancie 3-cim kiedy zje się czerwony owoc to pojawiaja sie nowe losowe mapy
                    #konieczne - uniemozliwic tworzenie sie scian na snakeu!
                    if game_settings.game_type == 3:
                        scoreboard.increase_score_n(1)
                        del walls
                        walls = create_wall(game_settings.screen_width, 
                                                game_settings.screen_height,
                                                game_settings.game_type,
                                                snake)
                        snake.extend()
                    else:
                        scoreboard.increase_score_n(1,2) 
                        snake2.extend()
                if fruit.type == 2:
                    scoreboard.increase_score_n(2,2) 
                    snake2.extend_n(2)
                if fruit.type == 3:
                    scoreboard.increase_score_n(-1,2) 
                    snake2.delete()
                if fruit.type == 4:
                    scoreboard.increase_score_n(-2,2)
                    snake2.delete_n(2)
                
                #usuwanie starego owoca
                food.remove(fruit)
                del fruit
                game_settings.change_ammount_foods()
                #tworzenie nowego owoca i dodanie go do food 
                #--> jeżeli jest mniej owoców niż current_ammount_fruits
                if len(food) < game_settings.current_ammount_fruits:
                    diff = game_settings.current_ammount_fruits - len(food)
                    for i in range(diff):
                        newFruit = Food(walls, scoreboard, game_settings)
                        food.append(newFruit)
                    
    # Sprawdź kolizje ze ścianami - snake1
    for wall in walls:
        if snake.head.colliderect(wall):
            game_settings.sound_background.stop()
            game_settings.sound_fail.play()
            if scoreboard.score > scoreboard.get_highestScore:
                with open("score.txt", "w") as file:
                    file.write(str(scoreboard.score))
            elif game_settings.game_type == 4 and scoreboard.score2 > scoreboard.get_highestScore:
                with open("score.txt", "w") as file:
                    file.write(str(scoreboard.score2))
            
            if not ask_to_continue():
                pygame.quit()
                sys.exit()
            else:
                timer.reset()

    # Sprawdź kolizje ze ścianami - snake2
    if game_settings.game_type == 4:
        for wall in walls:
            if snake2.head.colliderect(wall):
                game_settings.sound_background.stop()
                game_settings.sound_fail.play()
                if scoreboard.score > scoreboard.get_highestScore:
                    with open("score.txt", "w") as file:
                        file.write(str(scoreboard.score))
                elif game_settings.game_type == 4 and scoreboard.score2 > scoreboard.get_highestScore:
                    with open("score.txt", "w") as file:
                        file.write(str(scoreboard.score2))
                
                if not ask_to_continue():
                    pygame.quit()
                    sys.exit()
                else:
                    timer.reset()

    #sprawdzenie kolizji z samym soba - snake1
    for segment in snake.segments[3:]:
        if snake.head.colliderect(segment) and segment.x != snake.head.x and segment.y != snake.head.y:
            game_settings.sound_background.stop()
            game_settings.sound_fail.play()
            if scoreboard.score > scoreboard.get_highestScore:
                with open("score.txt", "w") as file:
                    file.write(str(scoreboard.score))
            elif game_settings.game_type == 4 and scoreboard.score2 > scoreboard.get_highestScore:
                with open("score.txt", "w") as file:
                    file.write(str(scoreboard.score2))
            
            if not ask_to_continue():
                pygame.quit()
                sys.exit()
            else:
                timer.reset()
    
    #sprawdzenie kolizji z samym soba - snake2
    if game_settings.game_type == 4:
        for segment in snake2.segments[3:]:
            if snake2.head.colliderect(segment) and segment.x != snake.head.x and segment.y != snake.head.y:
                game_settings.sound_background.stop()
                game_settings.sound_fail.play()
                if scoreboard.score > scoreboard.get_highestScore:
                    with open("score.txt", "w") as file:
                        file.write(str(scoreboard.score))
                elif game_settings.game_type == 4 and scoreboard.score2 > scoreboard.get_highestScore:
                    with open("score.txt", "w") as file:
                        file.write(str(scoreboard.score2))
            
                if not ask_to_continue():
                    pygame.quit()
                    sys.exit()
                else:
                    timer.reset()

    #sprawdzenie kolizji snake1 i snake2
    if game_settings.game_type == 4:
        for segmentSnake1 in snake.segments:
            if snake2.head.colliderect(segmentSnake1):
                game_settings.sound_background.stop()
                game_settings.sound_fail.play()
                if scoreboard.score > scoreboard.get_highestScore:
                    with open("score.txt", "w") as file:
                        file.write(str(scoreboard.score))
                elif game_settings.game_type == 4 and scoreboard.score2 > scoreboard.get_highestScore:
                    with open("score.txt", "w") as file:
                        file.write(str(scoreboard.score2))
                
                if not ask_to_continue():
                    pygame.quit()
                    sys.exit()
                else:
                    timer.reset()
               
        for segmentSnake2 in snake2.segments:
            if snake.head.colliderect(segmentSnake2):
                game_settings.sound_background.stop()
                game_settings.sound_fail.play()
                if scoreboard.score > scoreboard.get_highestScore:
                    with open("score.txt", "w") as file:
                        file.write(str(scoreboard.score))
                elif game_settings.game_type == 4 and scoreboard.score2 > scoreboard.get_highestScore:
                    with open("score.txt", "w") as file:
                        file.write(str(scoreboard.score2))
                
                if not ask_to_continue():
                    pygame.quit()
                    sys.exit()
                else:
                    timer.reset()
    
    #kontrola czy lenthOfTime owoca nie minął
    for fruit in food:
        if fruit.check_time() == True:
            food.remove(fruit)
            del fruit
            newFruit = Food(walls,scoreboard,game_settings)
            newFruit.spawn_food(scoreboard, game_settings)
            food.append(newFruit)
        else:
            pass

    # Wyświetl wszystkie obiekty gry
    if game_settings.background_image:
        game_settings.screen.blit(game_settings.background_image, (0, 0))
    
    if isinstance(food, list):
        for fruit in food:
            fruit.draw(game_settings.screen)
            
    for wall in walls:
        wall.draw(game_settings.screen)
    
    snake.draw(game_settings.screen)
    if game_settings.game_type == 4:
        snake2.draw(game_settings.screen)
   
    scoreboard.draw(game_settings.screen, game_settings.game_type)
    timer.draw()

    # Aktualizuj ekran
    pygame.display.flip()

    # Ustaw maksymalną liczbę klatek na sekundę
    game_settings.clock.tick(game_settings.speed)