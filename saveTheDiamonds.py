import pygame, time, random
import gameobjects

pygame.init()

# Initialize the game
bg_img = pygame.image.load('background.jpg')
bg_rect = (150,0,1000,666)


screen = pygame.display.set_mode((1300, 666))
screen_rect = screen.get_rect()

savedsprite = pygame.sprite.Group()
takensprite = pygame.sprite.Group()

no_of_diamonds = 10
diamond_group = pygame.sprite.Group()
for i in range(no_of_diamonds):
   diamond_group.add(gameobjects.Diamond(screen_rect))

no_of_spaceships = 1
spaceship_group = pygame.sprite.Group()
for i in range(no_of_spaceships):
   spaceship_group.add(gameobjects.Spaceship(screen_rect))



blue = (67,115, 194)

left_rect_width = 150
left_rect_height = 666
left_draw = pygame.Rect(0,0,left_rect_width,left_rect_height)
l_rect = gameobjects.Recte(0, 0, left_rect_width, left_rect_height)

right_rect_width = 150
right_rect_height = 666
right_draw = pygame.Rect(screen_rect.width- 150, 0 , right_rect_width, right_rect_height)
r_rect = gameobjects.Recte(screen_rect.width - 150, 0, right_rect_width, right_rect_height)

di = pygame.image.load("diamond.png")

font = pygame.font.Font('CoffeeHealing.ttf', 34)
save = font.render(f"Saved:{int(len(savedsprite))}", True, (223,50,31))
take =  font.render(f"Taken: {int(len(takensprite))}", True, (223, 50, 31))



def render():
    screen.blit(bg_img,bg_rect)
    r_rect.drawRect(screen, blue)
    l_rect.drawRect(screen, blue)


    diamond_group.update(screen_rect)
    diamond_group.draw(screen)

    spaceship_group.update(screen_rect)
    spaceship_group.draw(screen)
    takensprite.draw(screen)
    savedsprite.draw(screen)
    screen.blit(take, (10,5))
    screen.blit(save, (1150,5))

    pygame.display.flip()


render()
running = True
# gameloop
while running:
    #event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for sprite in diamond_group.sprites():
                if sprite.rect.collidepoint(event.pos):
                    
                    diamond_group.remove(sprite)               
                    diamond_group.update(screen_rect)
                    diamond_group.draw(screen)
                    savedsprite.add(gameobjects.panelDiamond(right_draw))
                    save = font.render(f"Saved:{int(len(savedsprite))}", True, (223,50,31))
                    print("saved " , savedsprite)
                    

                        
    #game logic
    for diam in pygame.sprite.groupcollide(diamond_group,spaceship_group,True,False).keys():
        dim = gameobjects.panelDiamond(left_draw)
        takensprite.add(dim)
        print("taken ", takensprite)
        l_rect.draws(di)
        take =  font.render(f"Taken: {int(len(takensprite))}", True, (223, 50, 31))
   

    #render
    render()
    time.sleep(0.05)

pygame.quit()