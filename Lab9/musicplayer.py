import pygame
import os

pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Pygame Music Player")

#music_files = [f for f in os.listdir(".") if f.endswith(".mp3") or f.endswith(".ogg")]
#Build full paths to music files
script_dir = os.path.dirname(os.path.abspath(__file__))
music_files = [
    os.path.join(script_dir, f) 
    for f in os.listdir(script_dir) 
    if f.lower().endswith((".mp3", ".ogg"))
]
current_index = 0

pygame.mixer.init()

running = True
playing = False
screencolor = (50, 50, 50)  

if music_files:
    pygame.mixer.music.load(music_files[current_index])

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE or event.key == pygame.K_p:
                if not playing:
                    pygame.mixer.music.play()
                    playing = True
                    screencolor = (0, 255, 0)  # Green when playing
                else:
                    pygame.mixer.music.unpause()

            elif event.key == pygame.K_s:
                pygame.mixer.music.stop()
                playing = False
                screencolor = (255, 0, 0)  # Red when stopped

            elif event.key == pygame.K_n:
                current_index = (current_index + 1) % len(music_files)
                pygame.mixer.music.load(music_files[current_index])
                pygame.mixer.music.play()
                playing = True

            elif event.key == pygame.K_b:
                current_index = (current_index - 1) % len(music_files)
                pygame.mixer.music.load(music_files[current_index])
                pygame.mixer.music.play()
                playing = True

    screen.fill((screencolor))
    pygame.display.flip()

pygame.quit()