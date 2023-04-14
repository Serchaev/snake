import random
import time

import pygame

pygame.init()

WIDTH = 1280
HEIGHT = 720
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
FPS = 20

display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Наша змейка")
clock = pygame.time.Clock()
font_style = pygame.font.SysFont(None, 36)


# time.sleep(2)

def score(scr):
    value = font_style.render("Ваш счет: " + str(scr), True, BLUE)
    display.blit(value, [10, 10])
    # pygame.display.update()


def message(text, color):
    msg = font_style.render(text, True, color)
    display.blit(msg, [WIDTH / 10, HEIGHT / 10])
    pygame.display.update()


def game():
    game_close = False
    game_over = False
    snake_x = WIDTH / 2
    snake_y = HEIGHT / 2
    snake_width = 10
    snake_height = 10
    x_change = 0
    y_change = 0
    food_x = round(random.randrange(0, WIDTH - snake_width) / 10) * 10
    food_y = round(random.randrange(0, HEIGHT - snake_height) / 10) * 10
    len_snake = 1
    snake_list = []

    while not game_close:
        while game_over:
            display.fill(WHITE)
            message("Вы проиграли. Q - Выход из игры. E - Начать заново.", RED)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_close = True
                    game_over = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_close = True
                        game_over = False
                    if event.key == pygame.K_e:
                        game()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_close = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y_change = -10
                    x_change = 0
                if event.key == pygame.K_DOWN:
                    y_change = 10
                    x_change = 0
                if event.key == pygame.K_LEFT:
                    x_change = -10
                    y_change = 0
                if event.key == pygame.K_RIGHT:
                    x_change = 10
                    y_change = 0
        snake_y += y_change
        snake_x += x_change

        if snake_y >= HEIGHT or snake_y < 0 or snake_x < 0 or snake_x >= WIDTH:
            game_over = True

        snake_list.append([snake_x, snake_y])

        if len(snake_list) > len_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_list[-1:][0]:
                game_over = True

        display.fill(WHITE)
        if snake_y == food_y and snake_x == food_x:
            food_x = round(random.randrange(0, WIDTH - snake_width) / 10) * 10
            food_y = round(random.randrange(0, HEIGHT - snake_height) / 10) * 10
            len_snake += 1

            # print(len_snake)

        score(len_snake - 1)
        pygame.draw.rect(display, GREEN, [food_x, food_y, snake_width, snake_height])

        for x in snake_list:
            pygame.draw.rect(display, BLACK, [x[0], x[1], snake_width, snake_height])
        pygame.display.update()

        clock.tick(FPS)


game()
pygame.quit()
