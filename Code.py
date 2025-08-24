import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Window setup
WIDTH, HEIGHT = 700, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dice Battle: You vs AI 🎲")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# ✅ Your dice image paths
dice_paths = [
    r"D:\Research\Promotion\4\1.jpg",
    r"D:\Research\Promotion\4\2.jpg",
    r"D:\Research\Promotion\4\3.jpg",
    r"D:\Research\Promotion\4\4.jpg",
    r"D:\Research\Promotion\4\5.jpg",
    r"D:\Research\Promotion\4\6.jpg",
]

# Load and scale images
dice_images = [pygame.transform.scale(pygame.image.load(path), (120, 120)) for path in dice_paths]

# Font
font = pygame.font.SysFont("Arial", 28, bold=True)

# Scores
player_score = 0
ai_score = 0

# Current dice values
player_dice = 1
ai_dice = 1

def draw_window(message="Press SPACE to Roll | ESC to Quit"):
    WIN.fill(WHITE)

    # Draw dice
    WIN.blit(dice_images[player_dice - 1], (150, HEIGHT//2 - 60))   # Player dice
    WIN.blit(dice_images[ai_dice - 1], (WIDTH - 270, HEIGHT//2 - 60))  # AI dice

    # Labels
    player_text = font.render("YOU", True, BLACK)
    ai_text = font.render("AI", True, BLACK)
    WIN.blit(player_text, (180, HEIGHT//2 - 100))
    WIN.blit(ai_text, (WIDTH - 230, HEIGHT//2 - 100))

    # Scores
    score_text = font.render(f"Score: You {player_score} - {ai_score} AI", True, BLACK)
    WIN.blit(score_text, (WIDTH//2 - score_text.get_width()//2, 50))

    # Instructions / Result
    info_text = font.render(message, True, BLACK)
    WIN.blit(info_text, (WIDTH//2 - info_text.get_width()//2, HEIGHT - 50))

    pygame.display.update()

def main():
    global player_dice, ai_dice, player_score, ai_score

    clock = pygame.time.Clock()
    running = True
    message = "Press SPACE to Roll | ESC to Quit"

    while running:
        clock.tick(30)  # FPS
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_score < 5 and ai_score < 5:
                    # Roll both dice
                    player_dice = random.randint(1, 6)
                    ai_dice = random.randint(1, 6)

                    # Decide winner of this round
                    if player_dice > ai_dice:
                        player_score += 1
                        message = "You win this round!"
                    elif ai_dice > player_dice:
                        ai_score += 1
                        message = "AI wins this round!"
                    else:
                        message = "It's a tie!"

                    # Check if game ended
                    if player_score == 5:
                        message = "🎉 YOU WON THE GAME!"
                    elif ai_score == 5:
                        message = "🤖 AI WON THE GAME!"

                elif event.key == pygame.K_ESCAPE:
                    running = False

        draw_window(message)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
