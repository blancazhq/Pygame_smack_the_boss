import pygame
import random

play_again = True
level_counter = 1


def overlap(c1, c2):
    if (c2.x in xrange(c1.x,c1.x + c1.dimensions[2]) and c2.y in xrange(c1.y, c1.y + c1.dimensions[3])) or (c2.x + c2.dimensions[2] in xrange(c1.x,c1.x + c1.dimensions[2]) and c2.y + c2.dimensions[3] in xrange(c1.y, c1.y + c1.dimensions[3])) or (c1.x in xrange(c2.x,c2.x + c1.dimensions[2]) and c1.y in xrange(c2.y, c2.y + c1.dimensions[3])) or (c1.x + c1.dimensions[2] in xrange(c2.x,c2.x + c2.dimensions[2]) and c1.y + c1.dimensions[3] in xrange(c2.y, c2.y + c2.dimensions[3])):
        return True
    else:
        return False

class Boss(object):
    def __init__(self,image,screen,others,tools):
        self.image = image
        self.dimensions = image.get_rect()
        self.bounds = screen.get_rect()
        self.set_location(others,tools)
        self.direction_speed = 1

    def set_location(self,others,tools):
        self.x = random.randint(self.bounds[0],self.bounds[2] - self.dimensions[2])
        self.y = random.randint(self.bounds[1],self.bounds[3] - self.dimensions[3])
        resetFlag = False
        for i in others:
            for j in tools:
                if overlap(i, self) or overlap(j, self):
                    resetFlag = True
        if resetFlag:
            self.set_location(others, tools)

    def get_location(self):
        return (self.x,self.y)


class Boss1(Boss):
    def __init__(self,image,screen,others,tools):
        self.image = image
        self.dimensions = image.get_rect()
        self.bounds = screen.get_rect()
        self.set_location(others,tools)
        self.direction_speed = 1
        self.click_needed = 1

class Boss2(Boss):
    def __init__(self,image,screen,others,tools):
        self.image = image
        self.dimensions = image.get_rect()
        self.bounds = screen.get_rect()
        self.set_location(others,tools)
        self.direction_speed = 1
        self.click_needed = 2

class Boss3(Boss):
    def __init__(self,image,screen,others,tools):
        self.image = image
        self.dimensions = image.get_rect()
        self.bounds = screen.get_rect()
        self.set_location(others,tools)
        self.direction_speed = 1
        self.click_needed = 3

class Boss4(Boss):
    def __init__(self,image,screen,others,tools):
        self.image = image
        self.dimensions = image.get_rect()
        self.bounds = screen.get_rect()
        self.set_location(others,tools)
        self.direction_speed = 1
        self.click_needed = 4

class Tool(object):
    def get_location(self):
        return (self.x,self.y)

class Timer(Tool):
    def __init__(self,image,screen):
        self.image = image
        self.dimensions = image.get_rect()
        self.x = 25
        self.y = 50

class Exit(Tool):
    def __init__(self,image,screen):
        self.image = image
        self.dimensions = image.get_rect()
        self.x = 405
        self.y = 25

class Level_text(Tool):
    def __init__(self,screen, level_counter):
        self.font = pygame.font.Font(None, 30)
        self.dimensions = [0, 0, 0, 0]
        self.dimensions[2] = self.font.size("Level1")[0]
        self.dimensions[3] = self.font.size("Level1")[1]
        self.x = 32
        self.y = 32
        self.text = self.font.render('Level %d' % level_counter, True, (0, 0, 0), (255,255,255))

def main():
    global play_again, level_counter
    play_again = False
    end_condition = ""

    background_image = pygame.image.load('images/background.png')
    x,y,width,height = background_image.get_rect()

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Smack the boss')
    clock = pygame.time.Clock()

    game_music = pygame.mixer.Sound('sounds/music.wav')

    mallet1_image = pygame.image.load('images/mallet1.png').convert_alpha()
    mallet2_image = pygame.image.load('images/mallet2.png').convert_alpha()
    start_banner_image = pygame.image.load('images/start_banner.png').convert_alpha()
    start_button_image = pygame.image.load('images/start_button.png').convert_alpha()
    level_complete_banner_image = pygame.image.load('images/level_complete_banner.png').convert_alpha()
    start_again_banner_image = pygame.image.load('images/start_again_banner.png').convert_alpha()
    exit_image = pygame.image.load('images/exit.png').convert_alpha()
    timer1_image = pygame.image.load('images/timer1.png').convert_alpha()
    timer2_image = pygame.image.load('images/timer2.png').convert_alpha()
    timer3_image = pygame.image.load('images/timer3.png').convert_alpha()
    timer4_image = pygame.image.load('images/timer4.png').convert_alpha()
    timer5_image = pygame.image.load('images/timer5.png').convert_alpha()
    timer6_image = pygame.image.load('images/timer6.png').convert_alpha()
    timer7_image = pygame.image.load('images/timer7.png').convert_alpha()
    timer8_image = pygame.image.load('images/timer8.png').convert_alpha()
    timer9_image = pygame.image.load('images/timer9.png').convert_alpha()

    quit_game = False
    start = False
    next_level = False

    smack_ticks = []
    smack_locations = []

    tools = []
    exit = Exit(exit_image, screen)
    tools.append(exit)
    level_text = Level_text(screen, level_counter)
    tools.append(level_text)
    timer = Timer(timer1_image, screen)
    tools.append(timer)
    game_music.play(-1)

    while quit_game == False:

        while start == False and quit_game == False:
            tick = pygame.time.get_ticks()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    stop_game = True
                    quit_game = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.pos[0] in range(350, 450) and event.pos[1] in range(285, 400):
                        start = True
                    if event.pos[0] in range(405, 475) and event.pos[1] in range(25, 50):
                        quit_game = True
            screen.blit(background_image, (0,0))
            exit = Exit(exit_image, screen)
            screen.blit(exit.image, exit.get_location())
            screen.blit(start_banner_image, (0, 235))
            if tick/200 % 2 == 0:
                screen.blit(start_button_image, (350, 260))
            else:
                screen.blit(start_button_image, (350, 270))
            pygame.display.update()
            game_music.stop()

        characters = []

        num_boss1 = 1 + level_counter - 1
        boss1s = []
        boss1_image = pygame.image.load('images/boss1.png').convert_alpha()
        for i in xrange(num_boss1):
            boss1 = Boss1(boss1_image,screen,characters,tools)
            characters.append(boss1)
            boss1s.append(boss1)


        num_boss2 = 1 + level_counter - 1
        boss2s = []
        boss2_image = pygame.image.load('images/boss2.png').convert_alpha()
        for i in xrange(num_boss2):
            boss2 = Boss2(boss2_image,screen,characters,tools)
            characters.append(boss2)
            boss2s.append(boss2)

        num_boss3 = 1 + level_counter - 1
        boss3s = []
        boss3_image = pygame.image.load('images/boss3.png').convert_alpha()
        for i in xrange(num_boss3):
            boss3 = Boss3(boss3_image,screen,characters,tools)
            characters.append(boss3)
            boss3s.append(boss3)

        num_boss4 = 1 + level_counter - 1
        boss4s = []
        boss4_image = pygame.image.load('images/boss4.png').convert_alpha()
        for i in xrange(num_boss4):
            boss4 = Boss4(boss4_image,screen,characters,tools)
            characters.append(boss4)
            boss4s.append(boss4)

        leveltick_start = pygame.time.get_ticks()
        game_music.play(-1)
        while start == True and quit_game == False:

            next_level = False
            tick = pygame.time.get_ticks()
            leveltick = pygame.time.get_ticks()
            mouse_pos = list(pygame.mouse.get_pos())
            mallet1_pos = [0, 0]
            mallet1_pos[0] = mouse_pos[0] -15
            mallet1_pos[1] = mouse_pos[1] -30
            smack_location = (-100, -100)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    stop_game = True
                    quit_game = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for i in range(len(boss1s)):
                        if event.pos[0] in range(boss1s[i].get_location()[0], boss1s[i].get_location()[0]+boss1s[i].dimensions[2]) and event.pos[1] in range(boss1s[i].get_location()[1], boss1s[i].get_location()[1]+boss1.dimensions[3]):
                            num_boss1 -= 1
                            sound = pygame.mixer.Sound('sounds/smack.wav')
                            sound.play()
                            smack_tick = pygame.time.get_ticks()
                            smack_ticks.append(smack_tick)
                            smack_location = boss1s[i].get_location()
                            smack_locations.append(smack_location)
                            characters.remove(boss1s[i])
                            boss1s.remove(boss1s[i])
                            break
                    for i in range(len(boss2s)):
                        if event.pos[0] in range(boss2s[i].get_location()[0], boss2s[i].get_location()[0]+boss2s[i].dimensions[2]) and event.pos[1] in range(boss2s[i].get_location()[1], boss2s[i].get_location()[1]+boss2s[i].dimensions[3]):
                            boss2s[i].click_needed -= 1
                            if boss2s[i].click_needed == 0:
                                num_boss2 -= 1
                                sound = pygame.mixer.Sound('sounds/smack.wav')
                                sound.play()
                                smack_tick = pygame.time.get_ticks()
                                smack_ticks.append(smack_tick)
                                smack_location = boss2s[i].get_location()
                                smack_locations.append(smack_location)
                                characters.remove(boss2s[i])
                                boss2s.remove(boss2s[i])
                            break
                    for i in range(len(boss3s)):
                        if event.pos[0] in range(boss3s[i].get_location()[0], boss3s[i].get_location()[0]+boss3s[i].dimensions[2]) and event.pos[1] in range(boss3s[i].get_location()[1], boss3s[i].get_location()[1]+boss3s[i].dimensions[3]):
                            boss3s[i].click_needed -= 1
                            if boss3s[i].click_needed == 0:
                                num_boss3 -= 1
                                sound = pygame.mixer.Sound('sounds/smack.wav')
                                sound.play()
                                smack_tick = pygame.time.get_ticks()
                                smack_ticks.append(smack_tick)
                                smack_location = boss3s[i].get_location()
                                smack_locations.append(smack_location)
                                characters.remove(boss3s[i])
                                boss3s.remove(boss3s[i])
                            break
                    for i in range(len(boss4s)):
                        if event.pos[0] in range(boss4s[i].get_location()[0], boss4s[i].get_location()[0]+boss4s[i].dimensions[2]) and event.pos[1] in range(boss4s[i].get_location()[1], boss4s[i].get_location()[1]+boss4s[i].dimensions[3]):
                            boss4s[i].click_needed -= 1
                            if boss4s[i].click_needed == 0:
                                num_boss4 -= 1
                                sound = pygame.mixer.Sound('sounds/smack.wav')
                                sound.play()
                                smack_tick = pygame.time.get_ticks()
                                smack_ticks.append(smack_tick)
                                smack_location = boss4s[i].get_location()
                                smack_locations.append(smack_location)
                                characters.remove(boss4s[i])
                                boss4s.remove(boss4s[i])
                            break
                    if event.pos[0] in range(405, 475) and event.pos[1] in range(25, 50):
                        quit_game = True


            screen.blit(background_image, (0,0))
            screen.blit(exit.image, exit.get_location())
            level_text = Level_text(screen, level_counter)
            screen.blit(level_text.text,level_text.get_location())

            if leveltick > leveltick_start and leveltick < leveltick_start + 1875:
                timer1 = Timer(timer1_image, screen)
                screen.blit(timer1_image, timer1.get_location())
            elif leveltick >= leveltick_start + 1875 and leveltick < leveltick_start + 3750:
                timer2 = Timer(timer2_image, screen)
                screen.blit(timer2_image, timer2.get_location())
            elif leveltick >= leveltick_start + 3750 and leveltick < leveltick_start + 5625:
                timer3 = Timer(timer3_image, screen)
                screen.blit(timer3_image, timer3.get_location())
            elif leveltick >= leveltick_start + 5625 and leveltick < leveltick_start + 7500:
                timer4 = Timer(timer4_image, screen)
                screen.blit(timer4_image, timer4.get_location())
            elif leveltick >= leveltick_start + 7500 and leveltick < leveltick_start + 9375:
                timer5 = Timer(timer5_image, screen)
                screen.blit(timer5_image, timer5.get_location())
            elif leveltick >= leveltick_start + 9375 and leveltick < leveltick_start + 11250:
                timer6 = Timer(timer6_image, screen)
                screen.blit(timer6_image, timer6.get_location())
            elif leveltick >= leveltick_start + 11250 and leveltick < leveltick_start + 13125:
                timer7 = Timer(timer7_image, screen)
                screen.blit(timer7_image, timer7.get_location())
            elif leveltick >= leveltick_start + 13125 and leveltick < leveltick_start + 15000:
                timer8 = Timer(timer8_image, screen)
                screen.blit(timer8_image, timer8.get_location())
            elif leveltick >= leveltick_start + 15000:
                timer9 = Timer(timer9_image, screen)
                screen.blit(timer9_image, timer9.get_location())
                sound = pygame.mixer.Sound('sounds/lose.flac')
                sound.play()
                end_condition = 'lose'
                level_counter = 1
                break

            for i in characters:
                screen.blit(i.image, i.get_location())

            if smack_location == (-100, -100):
                screen.blit(mallet1_image, mallet1_pos)

            if smack_ticks != []:
                if leveltick <= smack_ticks[-1] + 500:
                    screen.blit(mallet2_image, smack_locations[-1])
                    smack_tick = 0

            pygame.display.update()

            if num_boss1 <= 0 and num_boss2 <= 0 and num_boss3 <= 0 and num_boss4 <= 0:
                sound = pygame.mixer.Sound('sounds/level_complete.wav')
                sound.play()
                end_condition = 'win'
                level_counter += 1
                break

        game_music.stop()

        while start == True and end_condition == 'win' and quit_game == False:
            tick = pygame.time.get_ticks()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit_game = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.pos[0] in range(350, 450) and event.pos[1] in range(285, 400):
                        next_level = True
                        break
                    if event.pos[0] in range(405, 475) and event.pos[1] in range(25, 50):
                        quit_game = True
            if next_level == True:
                break

            screen.blit(background_image, (0,0))
            screen.blit(exit.image, exit.get_location())
            screen.blit(level_complete_banner_image, (0, 235))
            if tick/200 % 2 == 0:
                screen.blit(start_button_image, (350, 300))
            else:
                screen.blit(start_button_image, (350, 290))
            pygame.display.update()

        while start == True and end_condition == 'lose' and quit_game == False:
            tick = pygame.time.get_ticks()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit_game = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.pos[0] in range(350, 450) and event.pos[1] in range(285, 400):
                        next_level = True
                        break
                    if event.pos[0] in range(405, 475) and event.pos[1] in range(25, 50):
                        quit_game = True
            if next_level == True:
                break

            screen.blit(background_image, (0,0))
            screen.blit(exit.image, exit.get_location())
            screen.blit(start_again_banner_image, (0, 235))
            if tick/200 % 2 == 0:
                screen.blit(start_button_image, (350, 260))
            else:
                screen.blit(start_button_image, (350, 270))
            pygame.display.update()


pygame.quit()

if __name__ == '__main__':
    while play_again:
        main()
