import pygame

pygame.init()   # 초기화

#화면 크기 설정
screen_width    = 480
screen_height   = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption('My First Game!')

# FPS
clock = pygame.time.Clock()

# 배경 이미지 불러오기
background = pygame.image.load("C:/IT_Study/Python/Python_Game_Making/pygmae_basic/background.png")

# 캐릭터(sprite) 불러오기
character           = pygame.image.load("C:/IT_Study/Python/Python_Game_Making/pygmae_basic/character.png")
character_size      = character.get_rect().size # 이미지 크기를 구해옴
character_width     = character_size[0]         # 캐릭터 가로 크기
character_height    = character_size[1]         # 캐릭터 세로 크기
character_x_pos     = (screen_width - character_width) / 2  # 화면 가로의 절반 크기 = 정중앙 (가로)
character_y_pos     = screen_height - character_height      # 화면 세로 크기 = 가장 아래 (세로)

# 캐릭터 이동할 좌표
to_x = 0
to_y = 0

# 캐릭터 이동 속도
character_speed = 0.6

# 이벤트 루프
running = True  # 게임 실행중인가?
while running:
    dt = clock.tick(60) # 게임 화면 초당 프레임 수를 넣어준다

# 프레임 수에 따라 캐릭터 이동속도가 달라짐
# 10 fps : 1초당 10번 동작 -> 1번에 10만큼 -> 100 이동
# 20 fps : 1초당 5번 동작을 해야 5 * 20 해서 같은 시간동안 100을 이동한다.
# 따라서! **보정**이 들어가야 한다

    # print("fps : " + str(clock.get_fps()))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:       # 확인한 이벤트가 Quit일 때 아래를 실행
            running = False                 # 게임 종료

        if event.type == pygame.KEYDOWN:    # 키보드 눌렀는지 확인
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            elif event.key == pygame.K_UP:
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:
                to_y += character_speed

        if event.type == pygame.KEYUP:      # 키보드 손 뗐는지 확인
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x_pos += to_x * dt    # dt 값은 프레임 간 시간차이를 뜻함
    character_y_pos += to_y * dt    # dt 값은 fps와 반비례

    # 가로 한계 지정
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    # 세로 한계 지정
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height


    screen.blit(background, (0, 0))         # 배경 그리기

    screen.blit(character, (character_x_pos, character_y_pos))

    pygame.display.update()                 # 프레임마다 화면 update


pygame.quit()

