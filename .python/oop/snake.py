import pygame # type: ignore
import random
import sys
import time

# Настройки окна
WIDTH, HEIGHT = 600, 600
CELL_SIZE = 20

# Цвета
SNAKE_COLOR = (0, 255, 0)  # Тело змеи
HEAD_COLOR = (0, 200, 0)    # Голова змеи
BG_COLOR = (0, 0, 0)        # Фон (будет меняться)
GRID_COLOR = (30, 30, 30)   # Сетка
TEXT_COLOR = (255, 255, 255) # Текст
GAME_OVER_COLOR = (150, 0, 0) # Фон экрана завершения
BUTTON_COLOR = (50, 50, 50)  # Цвет кнопки
BUTTON_HOVER_COLOR = (100, 100, 100)  # Цвет кнопки при наведении

# Инициализация
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption('Змейка')

# Шрифты
font = pygame.font.SysFont('Arial', 25)
large_font = pygame.font.SysFont('Arial', 50)
button_font = pygame.font.SysFont('Arial', 30)

def draw_grid():
    for x in range(0, WIDTH, CELL_SIZE):
        pygame.draw.line(screen, GRID_COLOR, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, CELL_SIZE):
        pygame.draw.line(screen, GRID_COLOR, (0, y), (WIDTH, y))

def draw_fruit(pos, color):
    center = (pos[0] + CELL_SIZE // 2, pos[1] + CELL_SIZE // 2)
    pygame.draw.circle(screen, color, center, CELL_SIZE // 2)

def random_position():
    x = random.randint(0, (WIDTH - CELL_SIZE) // CELL_SIZE) * CELL_SIZE
    y = random.randint(0, (HEIGHT - CELL_SIZE) // CELL_SIZE) * CELL_SIZE
    return (x, y)

def random_color():
    return (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))

def show_score(score):
    score_text = font.render(f"Очки: {score}", True, TEXT_COLOR)
    screen.blit(score_text, (10, 10))

def draw_button(text, rect, mouse_pos):
    # Проверяем, находится ли мышь над кнопкой
    is_hovered = rect.collidepoint(mouse_pos)
    button_color = BUTTON_HOVER_COLOR if is_hovered else BUTTON_COLOR
    
    # Рисуем кнопку
    pygame.draw.rect(screen, button_color, rect)
    pygame.draw.rect(screen, TEXT_COLOR, rect, 2)  # Обводка
    
    # Рисуем текст на кнопке
    button_text = button_font.render(text, True, TEXT_COLOR)
    text_rect = button_text.get_rect(center=rect.center)
    screen.blit(button_text, text_rect)
    
    return is_hovered

def game_over_screen(score):
    screen.fill(GAME_OVER_COLOR)
    
    # Текст "Игра окончена"
    game_over_text = large_font.render("Игра окончена!", True, TEXT_COLOR)
    game_over_rect = game_over_text.get_rect(center=(WIDTH//2, HEIGHT//2 - 100))
    screen.blit(game_over_text, game_over_rect)
    
    # Отображение счёта
    score_text = font.render(f"Ваш счёт: {score}", True, TEXT_COLOR)
    score_rect = score_text.get_rect(center=(WIDTH//2, HEIGHT//2 - 20))
    screen.blit(score_text, score_rect)
    
    # Определяем прямоугольник для кнопки "Перезапустить" (увеличенный размер)
    restart_rect = pygame.Rect(WIDTH//2 - 125, HEIGHT//2 + 20, 250, 60)
    
    # Ожидание выбора игрока
    waiting = True
    while waiting:
        mouse_pos = pygame.mouse.get_pos()
        
        # Рисуем кнопку
        draw_button("Перезапустить", restart_rect, mouse_pos)
        
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Левая кнопка мыши
                if restart_rect.collidepoint(mouse_pos):
                    waiting = False
                    return True  # Перезапуск
        
        clock.tick(10)

def main():
    global BG_COLOR
    while True:
        # Инициализация игры
        snake = [(100, 100), (80, 100), (60, 100)]
        direction = (CELL_SIZE, 0)
        fruit = random_position()
        fruit_color = random_color()
        score = 0
        BG_COLOR = (0, 0, 0)  # Сбрасываем цвет фона
        move_delay = 150  # Начальный интервал движения в миллисекундах
        last_move_time = time.time() * 1000  # Время последнего шага в миллисекундах

        running = True
        while running:
            current_time = time.time() * 1000  # Текущее время в миллисекундах
            screen.fill(BG_COLOR)
            draw_grid()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Обработка ввода с клавиатуры
            keys = pygame.key.get_pressed()
            new_direction = direction
            if keys[pygame.K_UP] and direction != (0, CELL_SIZE):
                new_direction = (0, -CELL_SIZE)
            elif keys[pygame.K_DOWN] and direction != (0, -CELL_SIZE):
                new_direction = (0, CELL_SIZE)
            elif keys[pygame.K_LEFT] and direction != (CELL_SIZE, 0):
                new_direction = (-CELL_SIZE, 0)
            elif keys[pygame.K_RIGHT] and direction != (-CELL_SIZE, 0):
                new_direction = (CELL_SIZE, 0)

            direction = new_direction

            # Обновление движения змейки по таймеру
            if current_time - last_move_time >= move_delay:
                head_x = (snake[0][0] + direction[0]) % WIDTH
                head_y = (snake[0][1] + direction[1]) % HEIGHT
                new_head = (head_x, head_y)

                # Проверка столкновения
                if new_head in snake:
                    running = False
                    if game_over_screen(score):  # Если игрок выбрал перезапуск
                        break

                snake.insert(0, new_head)

                # Проверка съедания фрукта
                if new_head == fruit:
                    score += 1
                    fruit = random_position()
                    fruit_color = random_color()
                    if score % 5 == 0:  # Увеличение сложности каждые 5 очков
                        move_delay = max(50, move_delay - 30)  # Уменьшаем задержку на 30 мс
                    if score % 7 == 0:  # Меняем цвет фона каждые 7 очков
                        BG_COLOR = random_color()
                else:
                    snake.pop()

                last_move_time = current_time  # Обновляем время последнего шага

            # Отрисовка змеи
            for segment in snake[1:]:
                pygame.draw.rect(screen, SNAKE_COLOR, (*segment, CELL_SIZE, CELL_SIZE))
            pygame.draw.rect(screen, HEAD_COLOR, (*snake[0], CELL_SIZE, CELL_SIZE))

            draw_fruit(fruit, fruit_color)
            show_score(score)

            pygame.display.flip()
            clock.tick(60)  # Постоянный FPS для плавной отрисовки

if __name__ == "__main__":
    main()