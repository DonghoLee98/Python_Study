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

# 캐릭터(sprite) 불러오기
character           = pygame.image.load("C:/IT_Study/Python/Python_Game_Making/pygmae_basic/character.png")
character_size      = character.get_rect().size # 이미지 크기를 구해옴
character_width     = character_size[0]         # 캐릭터 가로 크기
character_height    = character_size[1]         # 캐릭터 세로 크기
character_x_pos     = (screen_width - character_width) / 2  # 화면 가로의 절반 크기 = 정중앙 (가로)
character_y_pos     = screen_height - character_height      # 화면 세로 크기 = 가장 아래 (세로)



# 이벤트 루프
running = True  # 게임 실행중인가?
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:       # 확인한 이벤트가 Quit일 때 아래를 실행
            running = False                 # 게임 종료

    screen.blit(background, (0, 0))         # 배경 그리기

    screen.blit(character, (character_x_pos, character_y_pos))

    pygame.display.update()                 # 프레임마다 화면 update


pygame.quit()

