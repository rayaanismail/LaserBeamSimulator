import pygame # type: ignore
from sys import exit
from helpers import cursorAngle, calculateDistance, calculateColor, chargeClick
import random

pygame.init()
screen = pygame.display.set_mode((1920, 1080))
screenxy = (screen.get_width(), screen.get_height())
screen.fill('black')
tickrate = 500
chargeLength = 2.5
decaying = False
cellulist = []
cellulistcopy = cellulist
colors = [
    (255, 255, 0), (255, 252, 0), (255, 249, 0), (255, 246, 0), (255, 243, 0),
    (255, 240, 0), (255, 237, 0), (255, 234, 0), (255, 231, 0), (255, 228, 0),
    (255, 225, 0), (255, 222, 0), (255, 219, 0), (255, 216, 0), (255, 213, 0),
    (255, 210, 0), (255, 207, 0), (255, 204, 0), (255, 201, 0), (255, 198, 0),
    (255, 195, 0), (255, 192, 0), (255, 189, 0), (255, 186, 0), (255, 183, 0),
    (255, 180, 0), (255, 177, 0), (255, 174, 0), (255, 171, 0), (255, 168, 0),
    (255, 165, 0), (255, 162, 0), (255, 159, 0), (255, 156, 0), (255, 153, 0),
    (255, 150, 0), (255, 147, 0), (255, 144, 0), (255, 141, 0), (255, 138, 0),
    (255, 135, 0), (255, 132, 0), (255, 129, 0), (255, 126, 0), (255, 123, 0),
    (255, 120, 0), (255, 117, 0), (255, 114, 0), (255, 111, 0), (255, 108, 0),
    (255, 105, 0), (255, 102, 0), (255, 99, 0), (255, 96, 0), (255, 93, 0),
    (255, 90, 0), (255, 87, 0), (255, 84, 0), (255, 81, 0), (255, 78, 0),
    (255, 75, 0), (255, 72, 0), (255, 69, 0), (255, 66, 0), (255, 63, 0),
    (255, 60, 0), (255, 57, 0), (255, 54, 0), (255, 51, 0), (255, 48, 0),
    (255, 45, 0), (255, 42, 0), (255, 39, 0), (255, 36, 0), (255, 33, 0),
    (255, 30, 0), (255, 27, 0), (255, 24, 0), (255, 21, 0), (255, 18, 0),
    (255, 15, 0), (255, 12, 0), (255, 9, 0), (255, 6, 0), (255, 3, 0),
    (255, 0, 0)
]

colorlist = [
    (255, 255, 0), (255, 252, 0), (255, 249, 0), (255, 246, 0), (255, 243, 0),
    (255, 240, 0), (255, 237, 0), (255, 234, 0), (255, 231, 0), (255, 228, 0),
    (255, 225, 0), (255, 222, 0), (255, 219, 0), (255, 216, 0), (255, 213, 0),
    (255, 210, 0), (255, 207, 0), (255, 204, 0), (255, 201, 0), (255, 198, 0),
    (255, 195, 0), (255, 192, 0), (255, 189, 0), (255, 186, 0), (255, 183, 0),
    (255, 180, 0), (255, 177, 0), (255, 174, 0), (255, 171, 0), (255, 168, 0),
    (255, 165, 0), (255, 162, 0), (255, 159, 0), (255, 156, 0), (255, 153, 0),
    (255, 150, 0), (255, 147, 0), (255, 144, 0), (255, 141, 0), (255, 138, 0),
    (255, 135, 0), (255, 132, 0), (255, 129, 0), (255, 126, 0), (255, 123, 0),
    (255, 120, 0), (255, 117, 0), (255, 114, 0), (255, 111, 0), (255, 108, 0),
    (255, 105, 0), (255, 102, 0), (255, 99, 0), (255, 96, 0), (255, 93, 0),
    (255, 90, 0), (255, 87, 0), (255, 84, 0), (255, 81, 0), (255, 78, 0),
    (255, 75, 0), (255, 72, 0), (255, 69, 0), (255, 66, 0), (255, 63, 0),
    (255, 60, 0), (255, 57, 0), (255, 54, 0), (255, 51, 0), (255, 48, 0),
    (255, 45, 0), (255, 42, 0), (255, 39, 0), (255, 36, 0), (255, 33, 0),
    (255, 30, 0), (255, 27, 0), (255, 24, 0), (255, 21, 0), (255, 18, 0),
    (255, 15, 0), (255, 12, 0), (255, 9, 0), (255, 6, 0), (255, 3, 0),
    (255, 0, 0)
]

colorswitch = 0

Center = (1920/2 - 50, 1080/2 - 25)
pygame.display.set_caption('Turret Simulator')
clock = pygame.time.Clock()
charge = 0.0
chargeBarPos = ((.05 * screenxy[0]),(.9 * screenxy[1]),(.9 * screenxy[0]),(.05 * screenxy[1]))

turret_original = pygame.image.load('Graphics/eye.png').convert_alpha()
turret_original = pygame.transform.scale_by(turret_original, .8)
cursor = pygame.image.load('Graphics/crosshair.png').convert_alpha()
cursor_rect = cursor.get_rect(center = Center)
pygame.mouse.set_visible(False)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    
    
    clickStatus = pygame.mouse.get_pressed(num_buttons=3)

    charge = chargeClick(clickStatus[0], charge, tickrate, chargeLength)
    offset = random.randrange(0, 3) - 1
    

    mpos = pygame.mouse.get_pos()
    angle = cursorAngle(cursor_rect.centerx, cursor_rect.centery, mpos[0], mpos[1])
    barcolor = calculateColor(charge*100, 250, "bar")
    cursorBeam = calculateColor(charge*100, 250, "beam")

    if colorswitch == len(colorlist)-1:
        colorswitch = 0
    else:
        colorswitch+=1
    pygame.draw.line(screen, colorlist[colorswitch], Center, mpos, round(round(charge * 100) / 8)+ 1)
    pygame.draw.rect(screen, "white", chargeBarPos, 5)
    if charge > 0 and charge < chargeLength:
        if clickStatus[0]:
            pygame.draw.rect(screen, barcolor, (chargeBarPos[0] + 5,chargeBarPos[1] + 5 ,(chargeBarPos[2] / chargeLength) * charge - 10, .04 * screenxy[1] + 1))
        else:
            pygame.draw.rect(screen, "white", (chargeBarPos[0] + 5,chargeBarPos[1] + 5 ,(chargeBarPos[2] / chargeLength) * charge - 10, .04 * screenxy[1] + 1)) 
    elif charge == chargeLength:
        pygame.draw.rect(screen, barcolor, (chargeBarPos[0] + 5,chargeBarPos[1] + 5 ,(chargeBarPos[2] / chargeLength) * charge - 10, .04 * screenxy[1] + 1))
    beamSize = (23/2.5)*charge
    pygame.draw.circle(screen, cursorBeam, (mpos[0] + offset,mpos[1] - offset), beamSize)
    
    turret = pygame.transform.rotate(turret_original, angle - 180)
    turret_rect = turret.get_rect(center = Center)

    screen.blit(turret, turret_rect)
    
    # draw all elements
    # update everything
    #print(f"Mouse: {mpos}\nObject:{cursor_rect.centerx}, {cursor_rect.centery}")
    #print(angle)
    pygame.display.update()
    screen.fill('black')
    if charge > 0:
        decayLength = 86
        alivecells = [cursorBeam,mpos,beamSize, decayLength]
        
        
        cellulist.append(alivecells)
    for cells in cellulist:
        pygame.draw.circle(screen, cells[0], cells[1], cells[2])
        cells[3]-= 1
        cells[0] = colors[cells[3]]
        cellulistcopy = cellulist
        if cells[3] == 0:
            cellulist.remove(cells)
            cellulistcopy = cellulist
    pygame.draw
        
    clock.tick(tickrate)