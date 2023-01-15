import pygame
import time
import random
import igroc
import Common
pygame.init()

igroc = igroc
Common = Common
dis = pygame.display.set_mode((igroc.dis_width, igroc.dis_height))


font_style = pygame.font.SysFont("bahnschrift", 45)
score_font = pygame.font.SysFont("comicsansms", 45)
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, Common.red, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [igroc.dis_width / 6, igroc.dis_height / 3])

def gameLoop():
    game_over = False
    game_close = False

    x1 = igroc.dis_width / 2
    y1 = igroc.dis_height / 2


    snake_List = []
    Length_of_snake = 1

    while not game_over:
        while game_close == True:
            dis.fill(Common.blue)
            message("You Lost!!!!!", Common.red)
            message("                     " + str(Length_of_snake - 1), Common.red)

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Common.game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    Common.x1_change = -igroc.snake_block
                    Common.y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    Common.x1_change = igroc.snake_block
                    Common.y1_change = 0
                elif event.key == pygame.K_UP:
                    Common.y1_change = -igroc.snake_block
                    Common.x1_change = 0
                elif event.key == pygame.K_DOWN:
                    Common.y1_change = igroc.snake_block
                    Common.x1_change = 0

        if x1 >= igroc.dis_width or x1 < 0 or y1 >= igroc.dis_height or y1 < 0:
            game_close = True
        x1 += Common.x1_change
        y1 += Common.y1_change
        dis.fill(Common.blue)
        f1 = pygame.font.Font(None, 36)
        text1 = f1.render("Score: " + str(Length_of_snake - 1), True,
                          (0, 20, 50))
        dis.blit(text1, (0, 0))
        pygame.draw.rect(dis, Common.green, [Common.foodx, Common.foody, igroc.snake_block, igroc.snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(igroc.snake_block, snake_List)


        if Common.foodx >= x1 and Common.foodx <= x1 + igroc.snake_block and Common.foody >= y1 and Common.foody <= y1 + igroc.snake_block:
            Common.foodx = round(random.randrange(0, igroc.dis_width - igroc.snake_block) / 20.0) * 20.0
            Common.foody = round(random.randrange(0, igroc.dis_height - igroc.snake_block) / 20.0) * 20.0
            Length_of_snake += 1
        #print('x1 = ' , x1, 'y1 = ', y1, 'foodx = ', foodx, 'foody = ', foody)

        pygame.display.update()
        Common.clock.tick(igroc.snake_speed)
    pygame.quit()
    quit()
gameLoop()