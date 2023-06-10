import pygame
import time

pygame.init()


class Enemy:
    def __init__(self, x, y, w, h, filename, speed):
        self.rect = pygame.Rect(x, y, w, h)
        self.image = pygame.image.load(filename)
        self.speed = speed

    def draw(self, window):
        # pygame.draw.rect(window, (0, 0, 0), self.rect)
        window.blit(self.image, [self.rect.x, self.rect.y])

    def update(self):
        self.rect.y += self.speed


class Bullet:
    def __init__(self, x, y, w, h, filename, speed):
        self.rect = pygame.Rect(x, y, w, h)
        self.image = pygame.image.load(filename)
        self.speed = speed

    def draw(self, window):
        pygame.draw.rect(window, (0, 0, 0), self.rect)
        window.blit(self.image, [self.rect.x, self.rect.y])

    def update(self):
        self.rect.y -= self.speed


class Platform:
    def __init__(self, x, y, w, h, filename, speed):
        self.rect = pygame.Rect(x, y, w, h)
        self.image = pygame.image.load(filename)
        self.speed = speed
        self.bullets = []

    def draw(self, window):
        pygame.draw.rect(window, (0, 0, 0), self.rect)
        window.blit(self.image, [self.rect.x, self.rect.y])

    def draw(self, window):
        pygame.draw.rect(window, (0, 0, 0), self.rect)
        window.blit(self.image, [self.rect.x, self.rect.y])
        for i in range(len(self.bullets)):
            self.bullets[i].draw(window)


screen = pygame.display.set_mode((500, 500))
fps = pygame.time.Clock()

pixils = []
x = 50
for i in range(4):
    pixils.append(Enemy(x, 50, 50, 50, "pixil-frame-0 (14).png", 1))
    x += 110

player = Platform(0, 350, 0, 20, "pixil-frame-0 (16).png", 0)
background = pygame.image.load("pixil-frame-0 (13).png")

n = 0
startTime = time.time()
timer = int(time.time() - startTime)
timeText = pygame.font.Font(None, 56).render("Час:" + str(timer), True, (0, 0, 0))

level = 1
leveltext = pygame.font.Font(None, 56).render("Левел:" + str(level), True, (0, 0, 0))
losetext = pygame.font.Font(None, 56).render("Ти програв:", True, (0, 0, 0))
Wintext = pygame.font.Font(None, 56).render("Ти виграв :", True, (0, 0, 0))

game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                player.speed = -5
            if event.key == pygame.K_d:
                player.speed = 5
            if event.key == pygame.K_f:
                player.bullets.append(Bullet(player.rect.x + 20, player.rect.y, 0, 20, "pixil-frame-0 (19).png", 3))
        if event.type == pygame.KEYUP:
            player.speed = 0
    # обробки подій

    # оновлення об'єктів
    player.rect.x += player.speed
    for i in range(len(player.bullets)):
        player.bullets[i].update()

    for i in range(len(pixils)):
        pixils[i].update()

    for i in range(len(player.bullets)):
        flag = False
        for j in range(len(pixils)):
            if pixils[j].rect.colliderect(player.bullets[i].rect):
                pixils.pop(j)
                player.bullets.pop(i)
                flag = True
                break
        if flag:
            break

    if len(pixils) == 0:
        level += 1
        leveltext = pygame.font.Font(None, 56).render("Левел:" + str(level), True, (0, 0, 0))

        x = 50
        for i in range(4):
            y = 50
            for j in range(level):
                pixils.append(Enemy(x, y, 50, 50, "pixil-frame-0 (14).png", 1))
                y -= 100
            x += 110

    timer = int(time.time() - startTime)
    timeText = pygame.font.Font(None, 56).render("Час:" + str(timer), True, (0, 0, 0))

    # відмалювання

    # заповніть екран кольором
    screen.blit(background, [0, 0])
    for i in range(len(pixils)):
        pixils[i].draw(screen)
    screen.blit(timeText, [0, 0])

    screen.blit(leveltext, [150, 0])

    player.draw(screen)

    for i in range(len(pixils)):
        if pixils[i].rect.y > 500:
            screen.fill((255, 0, 0))
            screen.blit(losetext, [100, 100])
        if timer > 60:
            screen.fill((0, 255, 0))
            screen.blit(Wintext, [100, 100])
            game = False
    pygame.display.flip()
    fps.tick(60)




