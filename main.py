import pygame
from pygame.locals import  QUIT
import service
from Components.Pelota import Pelota
from Components.Raqueta import Raqueta

def main():
    # Initializing Pygame
    pygame.init()
    # Window Initialization
    screen = pygame.display.set_mode((service.HORIZONTAL_WINDOW, service.VERTICAL_WINDOW))
    pygame.display.set_caption("Pong")
    font = pygame.font.Font(None, 60)

    #Ball creation
    pingBall =  Pelota('ball.png')

    raqueta1 = Raqueta()
    raqueta1.x = 60

    raqueta2 = Raqueta()
    raqueta2.x = service.HORIZONTAL_WINDOW - 60 - raqueta2.width

    playing = True
    while playing:
        pingBall.mov()
        pingBall.bounce()
        raqueta1.mov()
        raqueta1.beatTheBall(pingBall)
        raqueta2.movAI(pingBall)
        raqueta2.beatTheBallAI(pingBall)

        # Initializing the drawing surface
        screen.fill(service.WHITE)

        #Drawing the object in the window
        screen.blit(pingBall.img, (pingBall.x, pingBall.y))
        screen.blit(raqueta1.img, (raqueta1.x, raqueta1.y))
        screen.blit(raqueta2.img, (raqueta2.x, raqueta2.y))

        score = f"{pingBall.puntuation}: {pingBall.puntuationIA}"
        leaderboard = font.render(score, False, service.BLACK)
        screen.blit(leaderboard, (service.HORIZONTAL_WINDOW / 2 - font.size(score)[0] / 2, 50))

        for event in pygame.event.get():
            if event.type == QUIT:
                playing = False
            #Checks if a key has been pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    raqueta1.dir_y = -5
                if event.key == pygame.K_s:
                    raqueta1.dir_y = 5
            #Checks if the key has been released
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    raqueta1.dir_y = 0
                if event.key == pygame.K_s:
                    raqueta1.dir_y = 0
        # Updates the content of the entire screen
        pygame.display.flip()
        pygame.time.Clock().tick(service.FPS)

    pygame.quit()

if __name__ == "__main__":
    main()