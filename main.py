import pygame
import time
import random
pygame.font.init()

WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Dodge")
icon = pygame.image.load('C:\\Python\\SpaceDodge\\rocket.png')
pygame.display.set_icon(icon)


PLAYER_WIDTH = 40
PLAYER_HEIGHT = 60
PLAYER_IMG = pygame.image.load('C:\\Python\\SpaceDodge\\space-ship.png')
PLAYER_IMG = pygame.transform.scale(PLAYER_IMG, (PLAYER_WIDTH, PLAYER_HEIGHT))
PLAYER_VEL = 5

STAR_WIDTH = 30
STAR_HEIGHT = 40
STAR_IMG = pygame.image.load('C:\\Python\\SpaceDodge\\asteroid.png')
STAR_IMG = pygame.transform.scale(STAR_IMG, (STAR_WIDTH, STAR_HEIGHT))
STAR_VEL = 3

FONT = pygame.font.SysFont("Space Mono", 30)

def draw(player, elapsed_time, stars):

    WIN.fill((0, 0, 0))

    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, "white")
    WIN.blit(time_text, (10, 10))

    WIN.blit(PLAYER_IMG, (player.x, player.y))

    for star in stars:
        WIN.blit(STAR_IMG, (star.x, star.y))

    pygame.display.update()

def main():
    run = True

    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT, 
                         PLAYER_WIDTH, PLAYER_HEIGHT)
    clock = pygame.time.Clock()
    start_time = time.time()
    elapsed_time = 0

    star_add_increment = 2000
    star_count = 0

    stars = []
    hit = False

    while run:
        star_count += clock.tick(60)
        elapsed_time = time.time() - start_time

        if star_count > star_add_increment:
            for _ in range(3):
                star_x = random.randint(0, WIDTH - STAR_WIDTH)
                star = pygame.Rect(star_x, -STAR_HEIGHT, STAR_WIDTH, STAR_HEIGHT)
                stars.append(star)
            
            star_add_increment = max(200, star_add_increment - 50)
            star_count = 0


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a] and player.x - PLAYER_VEL >= 0:
            player.x -= PLAYER_VEL
        if keys[pygame.K_RIGHT] or keys[pygame.K_d] and player.x + PLAYER_VEL + PLAYER_WIDTH <= WIDTH:
            player.x += PLAYER_VEL

        for star in stars[:]:
            star.y += STAR_VEL
            if star.y > HEIGHT:
                stars.remove(star)
            elif star.y + star.height >= player.y and star.colliderect(player):
                stars.remove(star)
                hit = True
                break
        
        if hit :
            lost_text = FONT.render("You Lost!", 1, "white")
            WIN.blit(lost_text, (WIDTH / 2 - lost_text.get_width() / 2, HEIGHT / 2 - lost_text.get_height() / 2))
            pygame.display.update()
            pygame.time.delay(4000)
            break
        
        draw(player, elapsed_time, stars)

    pygame.quit()

if __name__ == "__main__":
    main()