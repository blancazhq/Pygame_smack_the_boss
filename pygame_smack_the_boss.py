import pygame
import random

play_again = True
level_counter = 1

def overlap(c1, c2):
    if (c2.x in xrange(c1.x,c1.x + c1.dimensions[2]) and c2.y in xrange(c1.y, c1.y + c1.dimensions[3])) or (c2.x + c2.dimensions[2] in xrange(c1.x,c1.x + c1.dimensions[2]) and c2.y + c2.dimensions[3] in xrange(c1.y, c1.y + c1.dimensions[3])):
        return True
    else:
        return False

class Boss(object):
    def __init__(self,image,screen,others):
        self.image = image
        self.dimensions = image.get_rect()
        self.bounds = screen.get_rect()
        self.set_location(others)
        self.direction_speed = 1
        self.change_direction()

    def change_direction(self):
        self.x_speed = random.randint(-1,1)
        self.y_speed = random.randint(-1,1)
        self.x_speed *= self.direction_speed
        self.y_speed *= self.direction_speed

    def set_location(self,others):
        self.x = random.randint(self.bounds[0],self.bounds[2] - self.dimensions[2])
        self.y = random.randint(self.bounds[1],self.bounds[3] - self.dimensions[3])
        resetFlag = False
        for i in others:
            if overlap(i,self):
                resetFlag = True
        if resetFlag:
            self.set_location(others)

    def get_location(self):
        return (self.x,self.y)

    def move(self):
        if self.x <= self.bounds[2] and self.y <= self.bounds[3] and self.x >= self.bounds[0] - self.dimensions[2] and self.y >= self.bounds[1] - self.dimensions[3]:
            self.x += self.x_speed
            self.y += self.y_speed
        elif self.x > self.bounds[2]:
            self.x = self.bounds[0] - self.dimensions[2]
        elif self.y > self.bounds[3]:
            self.y = self.bounds[1] - self.dimensions[3]
        elif self.x < self.bounds[0] - self.dimensions[2]:
            self.x = self.bounds[2]
        elif self.y < self.bounds[3] - self.dimensions[3]:
            self.y = self.bounds[3]

class Boss1(Boss):
    def __init__(self,image,screen,others):
        self.image = image
        self.dimensions = image.get_rect()
        self.bounds = screen.get_rect()
        self.set_location(others)
        self.direction_speed = 1
        self.change_direction()
        self.click_needed = 1

class Boss2(Boss):
    def __init__(self,image,screen,others):
        self.image = image
        self.dimensions = image.get_rect()
        self.bounds = screen.get_rect()
        self.set_location(others)
        self.direction_speed = 1
        self.change_direction()
        self.click_needed = 2

class Boss3(Boss):
    def __init__(self,image,screen,others):
        self.image = image
        self.dimensions = image.get_rect()
        self.bounds = screen.get_rect()
        self.set_location(others)
        self.direction_speed = 1
        self.change_direction()
        self.click_needed = 3

class Boss4(Boss):
    def __init__(self,image,screen,others):
        self.image = image
        self.dimensions = image.get_rect()
        self.bounds = screen.get_rect()
        self.set_location(others)
        self.direction_speed = 1
        self.change_direction()
        self.click_needed = 4

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

    start_banner_image = pygame.image.load('images/start_banner.png').convert_alpha()
    start_button_image = pygame.image.load('images/start_button.png').convert_alpha()
    level_complete_banner_image = pygame.image.load('images/level_complete_banner.png').convert_alpha()
    exit_image = pygame.image.load('images/exit.png').convert_alpha()

    quit_game = False
    start = False
    next_level = False
    game_music.play(-1)
    font = pygame.font.Font(None, 30)


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
            screen.blit(exit_image, (405, 25))
            screen.blit(start_banner_image, (0, 235))
            if tick/200 % 2 == 0:
                screen.blit(start_button_image, (350, 260))
            else:
                screen.blit(start_button_image, (350, 285))
            pygame.display.update()

        characters = []

        num_boss1 = 1 + level_counter - 1
        boss1s = []
        boss1_image = pygame.image.load('images/boss1.png').convert_alpha()
        for i in xrange(num_boss1):
            boss1 = Boss1(boss1_image,screen,characters)
            characters.append(boss1)
            boss1s.append(boss1)


        num_boss2 = 1 + level_counter - 1
        boss2s = []
        boss2_image = pygame.image.load('images/boss2.png').convert_alpha()
        for i in xrange(num_boss2):
            boss2 = Boss2(boss2_image,screen,characters)
            characters.append(boss2)
            boss2s.append(boss2)

        num_boss3 = 1 + level_counter - 1
        boss3s = []
        boss3_image = pygame.image.load('images/boss3.png').convert_alpha()
        for i in xrange(num_boss3):
            boss3 = Boss3(boss3_image,screen,characters)
            characters.append(boss3)
            boss3s.append(boss3)

        num_boss4 = 1 + level_counter - 1
        boss4s = []
        boss4_image = pygame.image.load('images/boss4.png').convert_alpha()
        for i in xrange(num_boss4):
            boss4 = Boss4(boss4_image,screen,characters)
            characters.append(boss4)
            boss4s.append(boss4)

        while start == True and quit_game == False:
            next_level = False
            tick = pygame.time.get_ticks()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    stop_game = True
                    quit_game = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for i in range(len(boss1s)):
                        if event.pos[0] in range(boss1s[i].get_location()[0], boss1s[i].get_location()[0]+boss1s[i].dimensions[2]) and event.pos[1] in range(boss1s[i].get_location()[1], boss1s[i].get_location()[1]+boss1.dimensions[3]):
                            num_boss1 -= 1
                            characters.remove(boss1s[i])
                            boss1s.remove(boss1s[i])
                            break
                    for i in range(len(boss2s)):
                        if event.pos[0] in range(boss2s[i].get_location()[0], boss2s[i].get_location()[0]+boss2s[i].dimensions[2]) and event.pos[1] in range(boss2s[i].get_location()[1], boss2s[i].get_location()[1]+boss2s[i].dimensions[3]):
                            boss2s[i].click_needed -= 1
                            if boss2s[i].click_needed == 0:
                                num_boss2 -= 1
                                characters.remove(boss2s[i])
                                boss2s.remove(boss2s[i])
                            break
                    for i in range(len(boss3s)):
                        if event.pos[0] in range(boss3s[i].get_location()[0], boss3s[i].get_location()[0]+boss3s[i].dimensions[2]) and event.pos[1] in range(boss3s[i].get_location()[1], boss3s[i].get_location()[1]+boss3s[i].dimensions[3]):
                            boss3s[i].click_needed -= 1
                            if boss3s[i].click_needed == 0:
                                num_boss3 -= 1
                                characters.remove(boss3s[i])
                                boss3s.remove(boss3s[i])
                            break
                    for i in range(len(boss4s)):
                        if event.pos[0] in range(boss4s[i].get_location()[0], boss4s[i].get_location()[0]+boss4s[i].dimensions[2]) and event.pos[1] in range(boss4s[i].get_location()[1], boss4s[i].get_location()[1]+boss4s[i].dimensions[3]):
                            boss4s[i].click_needed -= 1
                            if boss4s[i].click_needed == 0:
                                num_boss4 -= 1
                                characters.remove(boss4s[i])
                                boss4s.remove(boss4s[i])
                            break
                    if event.pos[0] in range(405, 475) and event.pos[1] in range(25, 50):
                        quit_game = True

            screen.blit(background_image, (0,0))
            screen.blit(exit_image, (405, 25))
            level_text = font.render('Level %d' % level_counter, True, (0, 0, 0), (255,255,255))
            screen.blit(level_text,(32,32))
            for i in characters:
                screen.blit(i.image, i.get_location())
            pygame.display.update()

            if num_boss1 <= 0 and num_boss2 <= 0 and num_boss3 <= 0 and num_boss4 <= 0:
                sound = pygame.mixer.Sound('sounds/win.wav')
                sound.play()
                end_condition = 'win'
                level_counter += 1
                break
            #else:
            #    sound = pygame.mixer.Sound('sounds/lose.wav')
            #    sound.play()
            #    end_condition = 'lose'
            #    level_counter = 1
            #    break

            game_music.stop()

        while start == True and end_condition == 'win' and quit_game == False:
            print "enter 3rd loop"
            print "next level: ", next_level
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
            screen.blit(exit_image, (405, 25))
            if end_condition == 'win':
                screen.blit(level_complete_banner_image, (0, 235))
                if tick/200 % 2 == 0:
                    screen.blit(start_button_image, (350, 300))
                else:
                    screen.blit(start_button_image, (350, 285))
                pygame.display.update()

"""
        if tick > 2000:
            monster.change_direction()
            for i in goblins:
                i.change_direction()
            tick = 0

        tick += clock.tick()
"""

pygame.quit()

if __name__ == '__main__':
    while play_again:
        main()
