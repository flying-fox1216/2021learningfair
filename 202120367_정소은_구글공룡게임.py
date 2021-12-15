#수정 파일_구글 공룡게임
import pygame
import random
import time

#초기화 #중요!
pygame.init() 

score = 0
#FPS
clock = pygame.time.Clock()

#화면 크기 설정
screenWidth = 800 #가로크기
screenHeight = 400 #세로크기

screen = pygame.display.set_mode((screenWidth,screenHeight))  #가로, 세로

#배경이미지
background = pygame.image.load("image/background.png")


#스테이지
stage = pygame.image.load("image/stage.png")
stageSize = stage.get_rect().size
stageHeight = stageSize[1]

#캐릭터
character = pygame.image.load("image/char-1.png")
character2 = pygame.image.load("image/char-2.png")
characterSize = character.get_rect().size  #img크기 불러옴
characterWidth = characterSize[0]
characterHeight = characterSize[1]
characterXpos = 100
characterYpos = screenHeight - characterHeight - stageHeight
move = True

#점프 코드
jump = 30
jumpHeight = jump

jumping = False

#이동할 좌표
toX = 0
toY = 0

#이동속도
characterSpeed = 0.6

#난수 생성 - 똥 생성용
randomNumber = 30
Speed = 1
speed2 = 2

#적
enemy = pygame.image.load("image/flyenemy2.png")
enemySize = enemy.get_rect().size
enemyWidth = enemySize[0] 
enemyHeight = enemySize[1] 
enemyXpos = screenWidth - enemyWidth
enemyYpos = stageHeight

tree = pygame.image.load("image/tree.png")
treeSize = tree.get_rect().size
treeWidth = treeSize[0]
treeHeight = treeSize[1]
treeXpos = screenWidth - treeWidth
treeYpos = screenHeight - treeHeight - stageHeight

#게임오버 텍스트
game_result = "GAME OVER"

#Title
pygame.display.set_caption("202120367_정소은_구글공룡게임")

#폰트 정의
game_font = pygame.font.Font(None,40) #폰트, 크기

#게임 플레이 총 시간
totalTime = 0
startTicks = pygame.time.get_ticks()

#Event
running = True
while running:  #실행창
    dt = clock.tick(60)
    #print("fps: " + str(clock.get_fps()))
    
    #캐릭터가 1초 100만큼 이동:
    #10FPs : 1초동안 10번 작동 -> 10만큼~~~ 100
    #20FPs : 1초동안 20번 작동 -> 5만큼~~~ 100
    for event in pygame.event.get(): #어떤 이벤트 발생했는지 판단함
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                toX -= characterSpeed
            if event.key == pygame.K_RIGHT:
                toX += characterSpeed
            if event.key == pygame.K_SPACE:
                jumping = True
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                toX = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                toY = 0
            elif event.key == pygame.K_SPACE:
                pass #스페이스바에서 손 뗏을때
            
    if jumping:
        characterYpos -= jumpHeight
        jumpHeight -= 2
        time.sleep(0.01)
        if characterYpos == screenHeight - characterHeight - stageHeight:
            next
            characterYpos = screenHeight - characterHeight - stageHeight
            jumping = False
            jumpHeight = jump
    
    #캐릭터 이동 & 프레임맞추기
    characterXpos += toX * dt
    characterYpos += toY * dt
    
    
    #경계 설정-가로
    if characterXpos < 0:
        characterXpos = 0
    elif characterXpos > screenWidth - characterWidth:
        characterXpos = screenWidth - characterWidth
    #경계 설정-세로
    
    
    randomY = random.randrange(0,screenHeight - enemyHeight - stageHeight) # 장애물 y 위치로 수정
    
    if enemyXpos <= 0 :
        enemyXpos = screenWidth - enemyWidth
        enemyYpos = randomY
        #enemyXpos = randomNumber2
        score += 1
        Speed += 0.5
        
    if treeXpos <= 0 :
        treeXpos = screenWidth - treeWidth
        #enemyXpos = randomNumber2
        score += 1
        speed2 += 0.5
    
    enemyXpos -= Speed
    treeXpos -= speed2
        
    #충돌
    characterRect = character.get_rect()
    characterRect.left = characterXpos
    characterRect.top = characterYpos
    
    enemyRect = enemy.get_rect()
    enemyRect.left = enemyXpos
    enemyRect.top = enemyYpos

    treeRect = tree.get_rect()
    treeRect.left = treeXpos
    treeRect.top = treeYpos
    
    if characterRect.colliderect(enemyRect):
        print("충돌했습니다!")
        print("GAME OVER")
        running = False
    if characterRect.colliderect(treeRect):
        print("충돌했습니다!")
        print("GAME OVER")
        running = False
            
    #타이머
    elapsedTime = (pygame.time.get_ticks()) / 1000
    #경과시간이 ms 이므로 초단위로 표시
    #if totalTime - elapsedTime < 0:
        #print("시간초과")
        #running = False
    timer = game_font.render(str(int(totalTime + elapsedTime)), True, (255,255,255))
    # 출력할 글자, , 색상
    scoree = game_font.render(str(score), True, (200,200,200))
    
    
    #screen.fill((0,0,255))
    screen.blit(background, (0,0))
    #screen.blit(backpic, (0,0))
    screen.blit(stage, (0,screenHeight - stageHeight))
    screen.blit(enemy, (enemyXpos , enemyYpos))
    screen.blit(tree, (treeXpos , treeYpos))
    screen.blit(timer, (10,10))
    screen.blit(scoree, (10,30))

    #캐릭터 움직임
    if move :
        screen.blit(character, (characterXpos , characterYpos))
        move = False
    else :
        screen.blit(character2, (characterXpos , characterYpos))
        move = True
        
        
    pygame.display.update() #화면 새로고침

# 게임오버
gameover = game_font.render(game_result, True , (255,0,0))
gameover_rect = gameover.get_rect(center = (int(screenWidth / 2), int(screenHeight / 2)))
screen.blit(gameover, gameover_rect)
pygame.display.update()

pygame.time.delay(2000)

pygame.quit()    #pygame 종료
