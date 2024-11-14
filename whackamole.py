import pygame
import random


def main():
    try:
        pygame.init()
            ### field creation ###
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()

            ### mole initial position ###
        mole_x = 1
        mole_y = 1
        mole_rect = mole_image.get_rect(topleft=(mole_x, mole_y))
        running = True
        while running:
            for event in pygame.event.get():
                    ### not running ###
                if event.type == pygame.QUIT:
                    running = False
                    ## click reaction ###
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if mole_rect.collidepoint(event.pos):
                        mole_x = random.randrange(0, 20) * 32  # 20 columns
                        mole_y = random.randrange(0, 16) * 32  # 16 rows
                        mole_rect.topleft = (mole_x, mole_y)

                ### field grid ###
            screen.fill("aquamarine")
            for i in range(1, 16):
                pygame.draw.line(screen, 'teal', (0, 32 * i), (640, 32 * i))
            for i in range(1, 20):
                pygame.draw.line(screen, 'teal', (32 * i, 0), (32 * i, 512))
            screen.blit(mole_image, mole_rect)
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
