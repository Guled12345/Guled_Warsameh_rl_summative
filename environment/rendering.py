import pygame

def visualize_learning_platform():
    pygame.init()
    
    screen = pygame.display.set_mode((600, 400))
    pygame.display.set_caption("Learning Platform RL Visualization")
    
    font = pygame.font.Font(None, 36)
    
    messages = [
        "Student is a Beginner...",
        "Student is an Active Learner...",
        "Student is Proficient...",
        "Student is an Independent Thinker!"
    ]
    
    running = True
    level = 0
    
    while running:
        screen.fill((255, 255, 255))
        
        text = font.render(messages[level], True, (0, 0, 0))
        screen.blit(text, (100, 180))
        
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                level = (level + 1) % len(messages)  # Cycle through messages
    
    pygame.quit()

if __name__ == "__main__":
    visualize_learning_platform()
