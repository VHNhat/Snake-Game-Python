import pygame 
from time import sleep
from random import randint

pygame.init()
clock = pygame.time.Clock()
FPS = 60
WIDTH, HEIGHT = 601 , 601
screen = pygame.display.set_mode((WIDTH, HEIGHT))
icon_window = pygame.image.load("sprites/img/icon_window.png")
icon_window = pygame.transform.scale(icon_window, (32,32))
pygame.display.set_icon(icon_window)
pygame.display.set_caption('Snake Game')

# color
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0 ,0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
BROWN = (102, 51, 0)
PURPLE = (255, 0, 255)

mode = "0"
lvl = "0"

def level():
    lv_img = pygame.image.load("sprites/img/intro_bg.png")
    lv_img = pygame.transform.scale(lv_img, (WIDTH,HEIGHT))

    back_button_img = pygame.image.load("sprites/img/back_button.png")
    back_button_img = pygame.transform.scale(back_button_img, (25,25))

    font_level = pygame.font.SysFont('Times New Roman', 50)
    font_easy = pygame.font.SysFont('Times New Roman', 35)
    font_normal = pygame.font.SysFont('Times New Roman', 35)
    font_hard = pygame.font.SysFont('Times New Roman', 35)
    
    text_level = font_level.render("Level", True, RED)

    sound_click = pygame.mixer.Sound('sprites/sound/mouse_click.wav')
    sound_move = pygame.mixer.Sound('sprites/sound/mouse_move.wav')
    # sound_base = pygame.mixer.Sound('sprites/sound/base_music.wav')
    
    gamestart = False
    mouse = 0

    while not gamestart:
        screen.fill(BLACK)
        clock.tick(FPS)

        screen.blit(lv_img, (0,0))

        # back button
        screen.blit(back_button_img,(5,5))

        mouse_x, mouse_y = pygame.mouse.get_pos()

        # Draw level text
        screen.blit(text_level, (250, 30))

        # Draw option box
        # pygame.draw.rect(screen, BROWN, (200,280,200,50))
        # pygame.draw.rect(screen, BROWN, (200,350,200,50))
        # pygame.draw.rect(screen, BROWN, (200,420,200,50))

        # Draw option text
        if mouse == 0 or mouse == 4:
            text_easy = font_easy.render("EASY", True, GREEN)
            text_normal = font_normal.render("NORMAL", True, YELLOW)
            text_hard = font_hard.render("HARD", True, PURPLE)
            screen.blit(text_easy, (260,290))
            screen.blit(text_normal, (230,360))
            screen.blit(text_hard, (255,430))
        elif mouse == 1:
            text_easy = font_easy.render("EASY", True, RED)
            text_normal = font_normal.render("NORMAL", True, YELLOW)
            text_hard = font_hard.render("HARD", True, PURPLE)
            screen.blit(text_easy, (260,290))
            screen.blit(text_normal, (230,360))
            screen.blit(text_hard, (255,430))
        elif mouse == 2:
            text_easy = font_easy.render("EASY", True, GREEN)
            text_normal = font_normal.render("NORMAL", True, RED)
            text_hard = font_hard.render("HARD", True, PURPLE)
            screen.blit(text_easy, (260,290))
            screen.blit(text_normal, (230,360))
            screen.blit(text_hard, (255,430))
        elif mouse == 3:
            text_easy = font_easy.render("EASY", True, GREEN)
            text_normal = font_normal.render("NORMAL", True, YELLOW)
            text_hard = font_hard.render("HARD", True, RED)
            screen.blit(text_easy, (260,290))
            screen.blit(text_normal, (230,360))
            screen.blit(text_hard, (255,430))

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if (200 < mouse_x < 400) and (280 < mouse_y < 330):
                        pygame.mixer.Sound.play(sound_click)
                        return "easy"
                    elif (200 < mouse_x < 400) and (350 < mouse_y < 400):
                        pygame.mixer.Sound.play(sound_click)
                        return "normal"
                    elif (200 < mouse_x < 400) and (420 < mouse_y < 470):
                        pygame.mixer.Sound.play(sound_click)
                        return "hard"
                    elif (0 < mouse_x < 30) and (0 < mouse_y < 30):
                        pygame.mixer.Sound.play(sound_click)
                        sleep(0.5)
                        main()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    main()
            if event.type == pygame.MOUSEMOTION:
                if (200 < mouse_x < 400) and (280 < mouse_y < 330):
                    if mouse == 0:
                        mouse = 1
                        pygame.mixer.Sound.play(sound_move)
                elif (200 < mouse_x < 400) and (350 < mouse_y < 400):
                    if mouse == 0:
                        mouse = 2
                        pygame.mixer.Sound.play(sound_move)
                elif (200 < mouse_x < 400) and (420 < mouse_y < 470):
                    if mouse == 0:
                        mouse = 3
                        pygame.mixer.Sound.play(sound_move)
                elif (0 < mouse_x < 30) and (0 < mouse_y < 30):
                    if mouse == 0:
                        mouse = 4
                        pygame.mixer.Sound.play(sound_move)
                else:
                    mouse = 0



        pygame.display.flip()

def gamepause():
    pausing_img = pygame.image.load("sprites/img/intro_bg.png")
    pausing_img = pygame.transform.scale(pausing_img, (WIDTH,HEIGHT))

    font_pausing = pygame.font.SysFont('Times New Roman', 50)
    font_resume = pygame.font.SysFont('Times New Roman', 35)
    font_mainmenu = pygame.font.SysFont('Times New Roman', 30)

    text_pausing = font_pausing.render('PAUSING...', True, RED)

    sound_click = pygame.mixer.Sound('sprites/sound/mouse_click.wav')
    sound_move = pygame.mixer.Sound('sprites/sound/mouse_move.wav')

    pygame.mixer.unpause()
    
    gamestart = False
    mouse = 0

    while not gamestart:
        screen.fill(BLACK)
        clock.tick(FPS)
        screen.blit(pausing_img, (0,0))
        mouse_x, mouse_y = pygame.mouse.get_pos()
        
        # Draw Pausing text
        screen.blit(text_pausing, (180, 30))

        # Draw option box
        # pygame.draw.rect(screen, BROWN, (200,300,200,80))
        # pygame.draw.rect(screen, BROWN, (200,400,200,80))

        # Draw option text
        if mouse == 0:
            text_resume = font_resume.render('RESUME', True, YELLOW)
            text_mainmenu = font_mainmenu.render('MAIN MENU', True, GREEN)
            screen.blit(text_resume, (230,320))
            screen.blit(text_mainmenu, (210,420))
        elif mouse == 1:
            text_resume = font_resume.render('RESUME', True, RED)
            text_mainmenu = font_mainmenu.render('MAIN MENU', True, GREEN)
            screen.blit(text_resume, (230,320))
            screen.blit(text_mainmenu, (210,420))
        elif mouse == 2:
            text_resume = font_resume.render('RESUME', True, YELLOW)
            text_mainmenu = font_mainmenu.render('MAIN MENU', True, RED)
            screen.blit(text_resume, (230,320))
            screen.blit(text_mainmenu, (210,420))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if (200 < mouse_x < 400) and (300 < mouse_y < 380):
                        pygame.mixer.Sound.play(sound_click)
                        return "resume"
                    elif (200 < mouse_x < 400) and (400 < mouse_y < 480):
                        pygame.mixer.Sound.play(sound_click)
                        return "main menu"
            if event.type == pygame.MOUSEMOTION:
                if (200 < mouse_x < 400) and (300 < mouse_y < 380): 
                    if mouse == 0:
                        mouse = 1
                        pygame.mixer.Sound.play(sound_move)
                elif (200 < mouse_x < 400) and (400 < mouse_y < 480):
                    if mouse == 0:
                        mouse = 2
                        pygame.mixer.Sound.play(sound_move)
                else:
                    mouse = 0
                
        
        pygame.display.flip()

def introscreen():

    pygame.mixer.stop()

    intro_img = pygame.image.load("sprites/img/intro_bg.png")
    intro_img = pygame.transform.scale(intro_img, (WIDTH,HEIGHT))
    sound_on_img = pygame.image.load("sprites/img/sound_on.png")
    sound_on_img = pygame.transform.scale(sound_on_img, (25,25))
    sound_off_img = pygame.image.load("sprites/img/sound_off.png")
    sound_off_img = pygame.transform.scale(sound_off_img, (25,25))

    font_intro = pygame.font.SysFont('Times New Roman', 50)
    font_classic = pygame.font.SysFont('Times New Roman', 35)
    font_special = pygame.font.SysFont('Times New Roman', 35)
    font_challenge = pygame.font.SysFont('Times New Roman', 30)
    font_unlimited = pygame.font.SysFont('Times New Roman', 35)

    text_intro = font_intro.render("Snake Game", True, RED)

    sound_click = pygame.mixer.Sound('sprites/sound/mouse_click.wav')
    sound_base = pygame.mixer.Sound('sprites/sound/base_music.wav')
    sound_move = pygame.mixer.Sound('sprites/sound/mouse_move.wav')
    pygame.mixer.Sound.play(sound_base)
    pygame.mixer.Sound.set_volume(sound_base, 0.3)

    gamestart = False
    sound_on = True
    mouse = 0

    while not gamestart:
        screen.fill(BLACK)
        clock.tick(FPS)
        # background
        screen.blit(intro_img, (0,0))
        # sound
        if sound_on:
            screen.blit(sound_on_img,(570,5))
        else:
            screen.blit(sound_off_img,(570,5))

        mouse_x, mouse_y = pygame.mouse.get_pos()

        # Draw intro text
        screen.blit(text_intro, (180,30))

        # Draw option box
        # pygame.draw.rect(screen, BROWN, (200,200,200,80))
        # pygame.draw.rect(screen, BROWN, (200,300,200,80))
        # pygame.draw.rect(screen, BROWN, (200,400,200,80))
        # pygame.draw.rect(screen, BROWN, (200,500,200,80))

        # Draw mode text
        if mouse == 0 or mouse == 5:
            text_classic = font_classic.render("CLASSIC", True, YELLOW)
            text_special = font_special.render("SPECIAL", True, BLUE)
            text_challenge = font_challenge.render("CHALLENGE", True, PURPLE)
            text_unlimited =  font_unlimited.render("UNLIMITED", True, GREEN)
            screen.blit(text_classic, (230,320))
            screen.blit(text_special, (230,420))
            screen.blit(text_challenge, (215,525))
            screen.blit(text_unlimited, (205,220))
        elif mouse == 1:
            text_classic = font_classic.render("CLASSIC", True, YELLOW)
            text_special = font_special.render("SPECIAL", True, BLUE)
            text_challenge = font_challenge.render("CHALLENGE", True, PURPLE)
            text_unlimited =  font_unlimited.render("UNLIMITED", True, RED)
            screen.blit(text_classic, (230,320))
            screen.blit(text_special, (230,420))
            screen.blit(text_challenge, (215,525))
            screen.blit(text_unlimited, (205,220))
        elif mouse == 2:
            text_classic = font_classic.render("CLASSIC", True, RED)
            text_special = font_special.render("SPECIAL", True, BLUE)
            text_challenge = font_challenge.render("CHALLENGE", True, PURPLE)
            text_unlimited =  font_unlimited.render("UNLIMITED", True, GREEN)
            screen.blit(text_classic, (230,320))
            screen.blit(text_special, (230,420))
            screen.blit(text_challenge, (215,525))
            screen.blit(text_unlimited, (205,220))
        elif mouse == 3:
            text_classic = font_classic.render("CLASSIC", True, YELLOW)
            text_special = font_special.render("SPECIAL", True, RED)
            text_challenge = font_challenge.render("CHALLENGE", True, PURPLE)
            text_unlimited =  font_unlimited.render("UNLIMITED", True, GREEN)
            screen.blit(text_classic, (230,320))
            screen.blit(text_special, (230,420))
            screen.blit(text_challenge, (215,525))
            screen.blit(text_unlimited, (205,220))
        elif mouse == 4:
            text_classic = font_classic.render("CLASSIC", True, YELLOW)
            text_special = font_special.render("SPECIAL", True, BLUE)
            text_challenge = font_challenge.render("CHALLENGE", True, RED)
            text_unlimited =  font_unlimited.render("UNLIMITED", True, GREEN)
            screen.blit(text_classic, (230,320))
            screen.blit(text_special, (230,420))
            screen.blit(text_challenge, (215,525))
            screen.blit(text_unlimited, (205,220))



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if (200 < mouse_x < 400) and (200 < mouse_y < 280):
                        pygame.mixer.Sound.play(sound_click)
                        return "unlimited"
                    elif (200 < mouse_x < 400) and (300 < mouse_y < 380):
                        pygame.mixer.Sound.play(sound_click)
                        return "classic"
                    elif (200 < mouse_x < 400) and (400 < mouse_y < 480):
                        pygame.mixer.Sound.play(sound_click)
                        return "special"
                    elif (200 < mouse_x < 400) and (500 < mouse_y < 580):
                        pygame.mixer.Sound.play(sound_click)
                        return "challenge"
                    elif (570 < mouse_x < 600) and (0 < mouse_y < 30):
                        if sound_on:
                            sound_on = False
                            pygame.mixer.Sound.set_volume(sound_base, 0)
                        else:
                            sound_on = True
                            pygame.mixer.Sound.set_volume(sound_base, 0.3)
            if event.type == pygame.MOUSEMOTION:
                if (200 < mouse_x < 400) and (200 < mouse_y < 280):
                    if mouse == 0:
                        mouse = 1
                        pygame.mixer.Sound.play(sound_move)
                elif (200 < mouse_x < 400) and (300 < mouse_y < 380):
                    if mouse == 0:
                        mouse = 2
                        pygame.mixer.Sound.play(sound_move)
                elif (200 < mouse_x < 400) and (400 < mouse_y < 480):
                    if mouse == 0:
                        mouse = 3
                        pygame.mixer.Sound.play(sound_move)
                elif (200 < mouse_x < 400) and (500 < mouse_y < 580):
                    if mouse == 0:
                        mouse = 4
                        pygame.mixer.Sound.play(sound_move)
                elif (570 < mouse_x < 600) and (0 < mouse_y < 30):
                    if mouse == 0:
                        mouse = 5
                        pygame.mixer.Sound.play(sound_move)
                else: 
                    mouse = 0
                    

        pygame.display.flip()

# check the place to spawn snake
def check(obss, temp):
    for i in range(len(obss)):
        if temp == obss[i]:
            return False
    return True

def gameplay(mode, lvl):

    pygame.mixer.stop()

    if mode == "challenge":
        obss = [[0,0],[0,1],[0,2],[0,3],[1,0],[2,0],[3,0],[16,0],[17,0],[18,0],[19,0],[19,1],[19,2],
                [19,3],[16,19],[17,19],[18,19],[19,19],[19,16],[19,17],[19,18],[0,16],[0,17],[0,18],
                [0,19],[1,19],[2,19],[3,19],[5,5],[5,6],[5,7],[5,8],[5,9],[5,10],[5,11],[5,12],[5,13],[5,14],[5,15],
                [14,5],[14,6],[14,7],[14,8],[14,9],[14,10],[14,11],[14,12],[14,13],[14,14],[14,15]]

    # initiallize snakes
    snakes = [[]]
    if mode == "challenge":
        while True:
            temp_snakes = [randint(0,19),randint(0,19)]
            if check(obss, temp_snakes):
                snakes = [temp_snakes]
                break
    else:
        snakes = [[randint(0,19),randint(0,19)]]


    # initiallize food
    while True:
        if mode == "challenge":
            temp_food = [randint(1,18), randint(1,18)]
            if temp_food not in snakes and temp_food not in obss:
                food = temp_food
                break
        else:
            temp_food = [randint(1,18), randint(1,18)]
            if temp_food not in snakes:
                food = temp_food
                break
    
    special_food = [-1,-1]
    time, temp = -1, -1

    run = True
    pausing = False
    score = 0
    direction = "0"
    die = False

    if mode == "unlimited":
        hit = False

    if lvl == "easy":
        difficulty = 0.13
    elif lvl == "normal":
        difficulty = 0.1
    elif lvl == "hard":
        difficulty = 0.08


    # obs1 = [[0,0],[0,1],[0,2],[0,3]]
    # obs2 = [[0,0],[1,0],[2,0],[3,0]]
    # obs3 = [[16,0],[17,0],[18,0],[19,0]]
    # obs4 = [[19,0],[19,1],[19,2],[19,3]]
    # obs5 = [[16,19],[17,19],[18,19],[19,19]]
    # obs6 = [[19,16],[19,17],[19,18],[19,19]]
    # obs7 = [[0,16],[0,17],[0,18],[0,19]]
    # obs8 = [[0,19],[1,19],[2,19],[3,19]]
    # obs9 = [[5,5],[5,6],[5,7],[5,8],[5,9],[5,10],[5,11],[5,12],[5,13],[5,14],[5,15]]
    # obs10 = [[14,5],[14,6],[14,7],[14,8],[14,9],[14,10],[14,11],[14,12],[14,13],[14,14],[14,15]]
    

    font_score = pygame.font.SysFont('time new roman', 20)
    font_gameover = pygame.font.SysFont('sans', 50)
    font_replay = pygame.font.SysFont('sans', 50)
    font_pause = pygame.font.SysFont('sans', 50)
    font_esc = pygame.font.SysFont('sans', 15)
    
    food_img = pygame.image.load("sprites/img/shiny-apple.png")
    food_img = pygame.transform.scale(food_img, (30,30))
    special_food_img = pygame.image.load("sprites/img/special-apple.png")
    special_food_img = pygame.transform.scale(special_food_img, (30,30))
    head_right_img = pygame.image.load("sprites/img/head_right.png")
    head_right_img = pygame.transform.scale(head_right_img, (30,30))
    head_left_img = pygame.image.load("sprites/img/head_left.png")
    head_left_img = pygame.transform.scale(head_left_img, (30,30))
    head_up_img = pygame.image.load("sprites/img/head_up.png")
    head_up_img = pygame.transform.scale(head_up_img, (30,30))
    head_down_img = pygame.image.load("sprites/img/head_down.png")
    head_down_img = pygame.transform.scale(head_down_img, (30,30))
    body_img = pygame.image.load("sprites/img/body.png")
    body_img = pygame.transform.scale(body_img, (30,30))
    obstacles1_img = pygame.image.load("sprites/img/obstacles1.png")
    obstacles1_img = pygame.transform.scale(obstacles1_img, (120,30))
    obstacles2_img = pygame.image.load("sprites/img/obstacles2.png")
    obstacles2_img = pygame.transform.scale(obstacles2_img, (30,120))
    obstacles3_img = pygame.image.load("sprites/img/obstacles2.png")
    obstacles3_img = pygame.transform.scale(obstacles3_img, (30,300))

    sound_point = pygame.mixer.Sound('sprites/sound/point.wav')
    sound_die = pygame.mixer.Sound('sprites/sound/die.wav')

    while run:
        screen.fill(BLACK)
        clock.tick(FPS)

        mouse_x, mouse_y = pygame.mouse.get_pos()

        tail_x = snakes[0][0]
        tail_y = snakes[0][1]

        # Draw edge
        if mode == "classic":
            pygame.draw.line(screen, RED, (0,0), (0,600))
            pygame.draw.line(screen, RED, (0,600), (600,600))
            pygame.draw.line(screen, RED, (0,0), (600,0))
            pygame.draw.line(screen, RED, (0,1), (600,1))
            pygame.draw.line(screen, RED, (600,0), (600,600))

        if mode == "challenge":
            # obstacles1 = pygame.draw.rect(screen, BROWN, (0,0,120,30))
            # obstacles2 = pygame.draw.rect(screen, BROWN, (0,0,30,120))
            # obstacles3 = pygame.draw.rect(screen, BROWN, (480,0,120,30))
            # obstacles4 = pygame.draw.rect(screen, BROWN, (570,0,30,120))
            # obstacles5 = pygame.draw.rect(screen, BROWN, (0,480,30,120))
            # obstacles6 = pygame.draw.rect(screen, BROWN, (0,570,120,30))
            # obstacles7 = pygame.draw.rect(screen, BROWN, (480,570,120,30))
            # obstacles8 = pygame.draw.rect(screen, BROWN, (570,480,30,120))
            # obstacles9 = pygame.draw.rect(screen, BROWN, (150,150,30,300))
            # obstacles10 = pygame.draw.rect(screen, BROWN, (420,150,30,300))

            obstacles1 = screen.blit(obstacles1_img,(0,0))
            obstacles2 = screen.blit(obstacles2_img,(0,0))
            obstacles3 = screen.blit(obstacles1_img,(480,0))
            obstacles4 = screen.blit(obstacles2_img,(570,0))
            obstacles5 = screen.blit(obstacles1_img,(0,570))
            obstacles6 = screen.blit(obstacles2_img,(0,480))
            obstacles7 = screen.blit(obstacles1_img,(480,570))
            obstacles8 = screen.blit(obstacles2_img,(570,480))
            obstacles9 = screen.blit(obstacles3_img,(150,150))
            obstacles10 = screen.blit(obstacles3_img,(420,150))
 
        #   Draw Grid
        # for i in range(21):
        #     pygame.draw.line(screen, WHITE, (i * 30, 0), (i * 30, 600))
        #     pygame.draw.line(screen, WHITE, (0, i * 30), (600, i*30))

        # Draw snake
        for snake in snakes[:-1]:
            #pygame.draw.rect(screen, GREEN, (snake[0] * 30, snake[1] * 30, 30, 30))
            screen.blit(body_img, (snake[0] * 30, snake[1] * 30))

        # Draw snake head    
        if direction == "right" or direction == "0":
            snake_head = screen.blit(head_right_img, (snakes[-1][0] * 30, snakes[-1][1] * 30))
        elif direction == "left" or direction == "0":
            snake_head = screen.blit(head_left_img, (snakes[-1][0] * 30, snakes[-1][1] * 30))
        elif direction == "up" or direction == "0":
            snake_head = screen.blit(head_up_img, (snakes[-1][0] * 30, snakes[-1][1] * 30))
        elif direction == "down" or direction == "0":
            snake_head = screen.blit(head_down_img, (snakes[-1][0] * 30, snakes[-1][1] * 30))

        # Draw food
        #pygame.draw.rect(screen, RED, (food[0] * 30, food[1] * 30, 30, 30))
        screen.blit(food_img, (food[0] * 30, food[1] * 30))
        if score % 10 == 0 and score != 0 and time > 0:
            screen.blit(special_food_img, (special_food[0] * 30, special_food[1] * 30))
            pygame.draw.rect(screen, RED,(special_food[0] * 30,special_food[1] * 30 - 5, int(30 * time/temp), 3))
            if direction != "0":
                time -= 1
        elif time == 0:
            time = -1
            special_food = [-1,-1]
            while True:
                temp_food = [randint(1,18),randint(1,18)]
                if temp_food not in snakes:
                    food = temp_food
                    break
            
        # Special point
        if snakes[-1][0] == special_food[0] and snakes[-1][1] == special_food[1]:
            pygame.mixer.Sound.play(sound_point)
            snakes.insert(0, [tail_x, tail_y])
            special_food = [-1,-1]
            score += 4
            if difficulty > 0.01:
                difficulty -= 0.005
            while True:
                temp_food = [randint(1,18),randint(1,18)]
                if temp_food not in snakes:
                    food = temp_food
                    break

        # Point
        if snakes[-1][0] == food[0] and snakes[-1][1] == food[1]:
            pygame.mixer.Sound.play(sound_point)
            snakes.insert(0, [tail_x, tail_y])
            score += 1
            if score % 2 == 0:
                if difficulty > 0.01:
                    difficulty -= 0.005
            while True:
                if score % 10 == 0:
                    food = [-1,-1]
                    if mode == "challenge":
                        temp_special_food = [randint(1,18),randint(1,18)]
                        if temp_special_food not in snakes and temp_food not in obss:
                            special_food = temp_special_food
                            time = 100
                            temp = time
                            break
                    
                    else:
                        temp_special_food = [randint(1,18),randint(1,18)]
                        if temp_special_food not in snakes:
                            special_food = temp_special_food
                            time = 100
                            temp = time
                            break
                else:
                    if mode == "challenge":
                        temp_food = [randint(1,18),randint(1,18)]
                        if temp_food not in snakes and temp_food not in obss:
                            food = temp_food                            
                            break
                    else:
                        temp_food = [randint(1,18),randint(1,18)]
                        if temp_food not in snakes:
                            food = temp_food
                            break	

        # HIT the Wall (end game) (Classic mode)
        if mode == "classic":
            if snakes[-1][0] > 19 or snakes[-1][0] < 0 or snakes[-1][1] > 19 or snakes[-1][1] < 0:
                pausing = True
        # Go through the wall (Special mode)
        elif mode == "special" or mode == "challenge" or mode == "unlimited":
            if snakes[-1][0] < 0:
                snakes[-1][0] = 19
            elif snakes[-1][0] > 19:
                snakes[-1][0] = 0
            elif snakes[-1][1] < 0:
                snakes[-1][1] = 19
            elif snakes[-1][1] > 19:
                snakes[-1][1] = 0

        if mode == "challenge":
            for obs in [obstacles1,obstacles2,obstacles3,obstacles4,obstacles5,obstacles6,obstacles7,obstacles8,obstacles9,obstacles10]:
                if snake_head.colliderect(obs):
                    pausing = True

        # Draw score text
        if mode == "challenge":
            text_score = font_score.render("Score: " + str(score), True, BLUE)
            screen.blit(text_score, (280 , 5))
        else:
            text_score = font_score.render("Score: " + str(score), True, BLUE)
            screen.blit(text_score, (5 , 5))

        # Draw escape text
        text_escape = font_esc.render("ESC", True, RED)
        screen.blit(text_escape, (570 , 10))

        # Draw Game Over scene
        if pausing:
            text_gameover = font_gameover.render("GAME OVER, Score: " + str(score), True, YELLOW)
            screen.blit(text_gameover, (90, 200))
            text_replay = font_replay.render("Press SPACE to CONTINUE", True, YELLOW)
            screen.blit(text_replay, (30, 300))
            text_pause = font_pause.render("Press ESCAPE to PAUSE", True, YELLOW)
            screen.blit(text_pause, (55, 400))
        
        # Snake movement
        if pausing == False:
            if direction == "up":
                snakes.append([snakes[-1][0],snakes[-1][1] - 1])
                snakes.pop(0)
            if direction == "down":
                snakes.append([snakes[-1][0],snakes[-1][1] + 1])
                snakes.pop(0)
            if direction == "right":
                snakes.append([snakes[-1][0] + 1,snakes[-1][1]])
                snakes.pop(0)
            if direction == "left":
                snakes.append([snakes[-1][0] - 1,snakes[-1][1]])
                snakes.pop(0)    

        # Hit the body
        if mode == "unlimited":
            for i in range((len(snakes) - 1)):
                if snakes[-1][0] == snakes[i][0] and snakes[-1][1] == snakes[i][1]:
                    for j in range(int(len(snakes) / 2)):
                        snakes.pop(0)
                        hit = True
                    break
            
            if hit == True:
                hit = False  
                score = int(score/2)
                difficulty += 0.005 * int(score / 2)
                if lvl == "easy":
                    if difficulty > 0.13:
                        difficulty = 0.13
                elif lvl == "normal":
                    if difficulty > 0.1:
                        difficulty = 0.1
                elif lvl == "hard":
                    if difficulty > 0.08:
                        difficulty = 0.08
            
                 
        else:
            for i in range((len(snakes) - 1)):
                if snakes[-1][0] == snakes[i][0] and snakes[-1][1] == snakes[i][1]:
                    pausing = True

        if pausing:
            if die == False:
                die = True
                pygame.mixer.Sound.play(sound_die)

        sleep(difficulty)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if (570 < mouse_x < 600) and (0 < mouse_y < 30):
                        direction = "0"
                        isGamepause = gamepause()
                        if isGamepause == "main menu":
                            isMainmenu = main()
                        elif isGamepause == "resume":
                            pass

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != "down":
                    #snakes[-1][1] -= 1
                    direction = "up"
                if event.key == pygame.K_DOWN and direction != "up":
                    #snakes[-1][1] += 1
                    direction = "down"
                if event.key == pygame.K_LEFT and direction != "right":
                    #snakes[-1][0] -= 1
                    direction = "left"
                if event.key == pygame.K_RIGHT and direction != "left":
                    #snakes[-1][0] += 1
                    direction = "right"
                if event.key == pygame.K_SPACE and pausing == True:
                    pausing = False
                    # snakes = [[randint(0,19),randint(0,19)]]
                    # food = [randint(0,19), randint(0,19)]
                    if mode == "challenge":
                        while True:
                            temp_snakes = [randint(0,19),randint(0,19)]
                            if check(obss, temp_snakes):
                                snakes = [temp_snakes]
                                break
                    else:
                        snakes = [[randint(0,19),randint(0,19)]]
                    ###############################################
                    while True:
                        if mode == "challenge":
                            temp_food = [randint(1,18), randint(1,18)]
                            if temp_food not in snakes and temp_food not in obss:
                                food = temp_food
                                break
                        else:
                            temp_food = [randint(1,18), randint(1,18)]
                            if temp_food not in snakes:
                                food = temp_food
                                break

                    direction = "0"
                    score = 0
                    die = False
                    if lvl == "easy":
                        difficulty = 0.13
                    elif lvl == "normal":
                        difficulty = 0.1
                    elif lvl == "hard":
                        difficulty = 0.08

                if event.key == pygame.K_ESCAPE and pausing == False:
                    direction = "0"
                    isGamepause = gamepause()
                    if isGamepause == "main menu":
                        isMainmenu = main()
                    elif isGamepause == "resume":
                        pass
                
                if event.key == pygame.K_ESCAPE and pausing == True:
                    isGamepause = gamepause()
                    if isGamepause == "main menu":
                        isMainmenu = main()
                    elif isGamepause == "resume":
                        pass  
                
        pygame.display.flip()

    pygame.quit()
    exit()

def main():
    isGameintro = introscreen()
    if isGameintro == "classic":
        mode = "classic"
        chooselevel = level()
        if chooselevel == "easy":
            lvl = "easy"
            gameplay(mode, lvl)
        elif chooselevel == "normal":
            lvl = "normal"
            gameplay(mode, lvl)
        elif chooselevel == "hard":
            lvl = "hard"
            gameplay(mode, lvl)
    elif isGameintro == "special":
        mode = "special"
        chooselevel = level()
        if chooselevel == "easy":
            lvl = "easy"
            gameplay(mode, lvl)
        elif chooselevel == "normal":
            lvl = "normal"
            gameplay(mode, lvl)
        elif chooselevel == "hard":
            lvl = "hard"
            gameplay(mode, lvl)
    elif isGameintro == "challenge":
        mode = "challenge"
        chooselevel = level()
        if chooselevel == "easy":
            lvl = "easy"
            gameplay(mode, lvl)
        elif chooselevel == "normal":
            lvl = "normal"
            gameplay(mode, lvl)
        elif chooselevel == "hard":
            lvl = "hard"
            gameplay(mode, lvl)
    elif isGameintro == "unlimited":
        mode = "unlimited"
        chooselevel = level()
        if chooselevel == "easy":
            lvl = "easy"
            gameplay(mode, lvl)
        elif chooselevel == "normal":
            lvl = "normal"
            gameplay(mode, lvl)
        elif chooselevel == "hard":
            lvl = "hard"
            gameplay(mode, lvl)

if __name__ == "__main__":
    main()