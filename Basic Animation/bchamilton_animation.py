import pygame

def loadFrames(sheet_path, frame_width, frame_height, columns, rows):
    picture = pygame.image.load(sheet_path).convert_alpha()
    frames = []
    for row in range(rows):
        for col in range(columns):
            x = col * frame_width
            y = row * frame_height
            frame = picture.subsurface(pygame.Rect(x, y, frame_width, frame_height))
            frames.append(frame)
    return frames

def main():
    pygame.init()
    
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Watch this guy walk around")
    
    background = pygame.image.load("country-platform-preview.png")
    background.convert()
    background = pygame.transform.scale(background, (640, 480))
    
    frames = loadFrames("PrinceRanger.png", 32, 32, 8, 4)
    walk_row = 2
    walk_frames = frames[walk_row * 8: (walk_row + 1) * 8]
    walk_frames = [
        pygame.transform.scale(f, (80, 80))
        for f in walk_frames
    ]
    current_frame = 0
    frame_x = 44
    frame_y = 340
    direction = "right"
    speed = 5
    
    clock = pygame.time.Clock()
    keepGoing = True
    while keepGoing:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            #if event.type == pygame.MOUSEBUTTONDOWN:
                #pos = pygame.mouse.get_pos()
                #print(f"Mouse clicked at: {pos}")
            
        current_frame = (current_frame - 0.2) % len(walk_frames)
        frame = walk_frames[int(current_frame)]
        
        if direction == "right":
            frame_x += speed
            if frame_x + 80 >= 640:
                walk_frames = [pygame.transform.flip(f, True, False) for f in walk_frames]
                direction = "left"
        elif direction == "left":
            frame_x -= speed
            if frame_x <= 0:
                walk_frames = [pygame.transform.flip(f, True, False) for f in walk_frames]
                direction = "right"
        else:
            frame_x = 0
            direction = "right"
        
        screen.blit(background, (0, 0))
        screen.blit(frame, (frame_x, frame_y))
        pygame.display.flip()
    
    pygame.quit()
    
if __name__ == "__main__":
    main()