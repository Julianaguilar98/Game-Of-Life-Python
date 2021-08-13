import sys
import getopt
import pygame
import game_of_life as game

BLACK, WHITE = (0, 0, 0), (255, 255, 255)
X_POS, Y_POS = 0, 1
WIDTH, HEIGHT, MARGIN = 20, 20, 5

T_MS = 1000
CONTINUE_SIM =  pygame.USEREVENT + 1

pygame.init()

clock = pygame.time.Clock()
game_display = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Conway's Game of Life")

positions = set()
continue_simulation = False

try:
  opts, args = getopt.getopt(sys.argv[1:], "t", [])
  for opt, arg in opts:
    if opt == "-t":
      positions = set([(10, 10), (10, 11), (10, 12)])
  continue_simulation = True
  pygame.time.set_timer(CONTINUE_SIM, T_MS)
except getopt.GetoptError:
  print('gui.py -s <inputs>')
  sys.exit(2)

running = True

while running:

  for event in pygame.event.get():
    if event.type == pygame.QUIT: running = False

    elif event.type == pygame.MOUSEBUTTONDOWN:
      pos = pygame.mouse.get_pos()
      x_pos = pos[X_POS] // (WIDTH + MARGIN)
      y_pos = pos[Y_POS] // (HEIGHT + MARGIN)

      if (x_pos, y_pos) in positions: positions.remove((x_pos, y_pos))
      else: positions.add((x_pos, y_pos))
    
    elif event.type == CONTINUE_SIM: positions = game.next_generation(positions)

    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_SPACE: positions = game.next_generation(positions)
      elif event.key == pygame.K_c: 
        continue_simulation = True if not continue_simulation else False
        pygame.time.set_timer(CONTINUE_SIM, T_MS) if continue_simulation else pygame.time.set_timer(CONTINUE_SIM, 0)

  game_display.fill(BLACK)

  for cell in positions:
    pygame.draw.rect(game_display, 
                  WHITE, 
                  [int((MARGIN + WIDTH) * cell[X_POS] + MARGIN / 2),
                    int((MARGIN + HEIGHT) * cell[Y_POS] + MARGIN / 2),
                    WIDTH,
                    HEIGHT])
    
  pygame.display.flip()
  clock.tick(60)

pygame.quit()
