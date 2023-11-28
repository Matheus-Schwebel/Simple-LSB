import pygame
import sys
import random
from tkinter import messagebox

# Cores
#preto = (0, 0, 0)        # Preto
#branco = (255, 255, 255)      # Branco
#vermelho = (255, 0, 0)           # Vermelho
#amarelo = (255, 255, 0)        # Amarelo
#verde = (0, 255, 0) #Verde

# Inicialização do Pygame
pygame.init()

# Configuração da tela
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Legendary Stickman Blasic")

# Cores
white = (255, 255, 255)
red = (255, 0, 0)
yellow = (255, 255, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
orange = (255, 165, 0)
ciano = (0, 255, 255)
roxo = (128, 0, 128)

# Jogador
player_width, player_height = 50, 50
player_x = (width - player_width) // 2
player_y = height - player_height - 10
player_speed = 50

# Inimigo
enemy_width, enemy_height = 50, 50
enemy_x = random.randint(0, width - enemy_width)
enemy_y = 0
enemy_speed = 5

# Bala
bullet_width, bullet_height = 5, 15
bullet_x, bullet_y = 0, 0
bullet_speed = 10
bullet_state = "ready"

# Pontuação
score = 0

# Fonte
font = pygame.font.Font(None, 36)

# Função para desenhar o jogador
def draw_player(x, y):

    pygame.draw.rect(screen, white, [x, y, player_width, player_height])

# Função para desenhar o inimigo
def draw_enemy(x, y):
    pygame.draw.rect(screen, red, [x, y, enemy_width, enemy_height])

# Função para desenhar a bala
def draw_bullet(x, y):
    pygame.draw.rect(screen, yellow, [x, y, bullet_width, bullet_height])

# Função para exibir a pontuação na tela
def show_score():
    score_text = font.render("Pontuação: {}".format(score), True, white)
    screen.blit(score_text, (10, 10))

# Loop principal do jogo
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Controles do jogador
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x -= player_speed
            elif event.key == pygame.K_RIGHT:
                player_x += player_speed
            elif event.key == pygame.K_SPACE and bullet_state == "ready":
                bullet_state = "fire"
                bullet_x = player_x + (player_width - bullet_width) // 2
                bullet_y = player_y


    # Atualizações do jogo
    player_x = max(0, min(width - player_width, player_x))
    enemy_y += enemy_speed

    # Verifica se o jogador atingiu o inimigo
    if player_x < enemy_x + enemy_width and player_x + player_width > enemy_x and player_y < enemy_y + enemy_height and player_y + player_height > enemy_y:
        messagebox.showinfo("Game Over!","Pontuação: {}".format(score))
        pygame.quit()
        sys.exit()

    # Verifica se a bala atingiu o inimigo
    if bullet_state == "fire":
        if bullet_x < enemy_x + enemy_width and bullet_x + bullet_width > enemy_x and bullet_y < enemy_y + enemy_height and bullet_y + bullet_height > enemy_y:
            bullet_state = "ready"
            enemy_x = random.randint(0, width - enemy_width)
            enemy_y = 0
            score += 1

    # Verifica se o jogador perdeu o primeiro alvo
    if enemy_y > height:
        messagebox.showinfo("Perdeu o jogo!", "Pontuação: {}".format(score))
        pygame.quit()
        sys.exit()

    # Desenha os elementos na tela
    screen.fill((0, 0, 0))
    draw_player(player_x, player_y)
    draw_enemy(enemy_x, enemy_y)
    
    if bullet_state == "fire":
        draw_bullet(bullet_x, bullet_y)
        bullet_y -= bullet_speed
        if bullet_y < 0:
            bullet_state = "ready"

    show_score()
    pygame.display.flip()
    clock.tick(30)  # Controle de frames por segundo
