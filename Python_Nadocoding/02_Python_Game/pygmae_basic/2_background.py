import pygame

pygame.init()   # 초기화

#화면 크기 설정
screen_width    = 480
screen_height   = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption('My First Game!')

# 배경 이미지 불러오기
background = pygame.image.load("C:/IT_Study/Python/Python_Game_Making/pygmae_basic/background.png")

# 이벤트 루프
running = True  # 게임 실행중인가?
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:       # 확인한 이벤트가 Quit일 때 아래를 실행
            running = False                 # 게임 종료

    #screen.fill((0, 0, 255))               # 색으로만 채울 수도 있음
    screen.blit(background, (0, 0))         # 배경 그리기

    pygame.display.update()                 # 프레임마다 화면 update


pygame.quit()

