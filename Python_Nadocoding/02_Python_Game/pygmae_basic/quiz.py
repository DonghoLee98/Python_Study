####################################################################
# Quiz : 응가 피하기 게임 만들기

# [조건]
# 1. 캐릭터 화면 가장 아래 위치, 좌우 이동만 허용
# 2. 응가는 화면 가장 위에서 출발. x좌표 랜덤 설정
# 3. 응가를 피하면(== 바닥에 닿으면) 새로운 응가가 출발
# 4. 응가랑 닿으면 게임 끝
# 5. fps : 30 고정

# [attachment]
# 1. 배경 : 640*480(세로*가로) - background.png
# 2. 캐릭터 / 응가 : 70*70 - character.png / enemy.png
####################################################################

import random
import pygame

####################################################################
## 0. 기본 초기화
##  1) init() 처리
##  2) Layout 설정
####################################################################

pygame.init()   # 초기화

#화면 크기 설정
screen_width    = 480
screen_height   = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption('Shit Escape')

# FPS
clock = pygame.time.Clock()

####################################################################
## 1. 사용자 게임 초기화
##  - 배경화면, 이미지, 좌표, 속도, 폰트 등등
####################################################################

# 배경 이미지 불러오기
background = pygame.image.load("C:/IT_Study/Python/Python_Game_Making/pygmae_basic/background.png")

# 캐릭터(sprite) 불러오기
character           = pygame.image.load("C:/IT_Study/Python/Python_Game_Making/pygmae_basic/character.png")
character_size      = character.get_rect().size # 이미지 크기를 구해옴
character_width     = character_size[0]         # 캐릭터 가로 크기
character_height    = character_size[1]         # 캐릭터 세로 크기
character_x_pos     = (screen_width - character_width) / 2  # 화면 가로의 절반 크기 == 정중앙 (가로)
character_y_pos     = screen_height - character_height      # 화면 세로 크기 == 가장 아래 (세로)

# 캐릭터 이동 좌표 초기화화
to_x = 0
to_y = 0

# 캐릭터 이동 속도
character_speed = 0.6
shit_speed = 0.5

# 적 캐릭터 불러오기    //// "캐릭터 불러오기" 함수 만들어서 사용해 보기!
enemy           = pygame.image.load("C:/IT_Study/Python/Python_Game_Making/pygmae_basic/enemy.png")
enemy_size      = enemy.get_rect().size # 이미지 크기를 구해옴
enemy_width     = enemy_size[0]         # 캐릭터 가로 크기
enemy_height    = enemy_size[1]         # 캐릭터 세로 크기
enemy_x_pos     = random.randint(0, int(screen_width - character_width))    # screen_width 내에서 랜덤값
enemy_y_pos     = 0                     # Screen_Top

# 폰트 정의
game_font = pygame.font.Font(None, 40)  # 폰트 객체 생성 (font, size)

# 게임 점수
base_score = 10
total_score = 0

# 시작 시간
start_ticks = pygame.time.get_ticks()   # 프로그램 시작 tick 받아오기

# 이벤트 loop
running = True  # 게임 실행중인가?
while running:
    dt = clock.tick(30) # 게임 화면 초당 프레임 수를 넣어준다

    ####################################################################
    ## 2. event 처리
    ####################################################################

    for event in pygame.event.get():
        if event.type == pygame.QUIT:       # 확인한 이벤트가 Quit일 때 아래를 실행
            running = False                 # 게임 종료

        ####################################################################
        ## 3-1. 게임 캐릭터 위치 정의
        ####################################################################

        if event.type == pygame.KEYDOWN:    # 키보드 눌렀는지 확인
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed

        if event.type == pygame.KEYUP:      # 키보드 손 뗐는지 확인
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0

    character_x_pos += to_x * dt

    # 가로 한계 지정
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    ####################################################################
    ## 3-2. 응가 위치 정의
    ####################################################################
    
    enemy_y_pos += shit_speed * dt
    if enemy_y_pos >= screen_height - character_height:
        enemy_x_pos = random.randint(0, int(screen_width - character_width))
        enemy_y_pos = 0
        total_score += base_score

    ####################################################################
    ## 4. 충돌 처리
    ####################################################################

    # 충돌 처리 (character의 rect 속성값을 x, y position으로 업데이트)
    character_rect = character.get_rect()   # <rect(0, 0, 70, 70)> : left, top, width, height
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos   # enemy_pos 최초 업데이트
    enemy_rect.top = enemy_y_pos

    # 충돌 체크
    if character_rect.colliderect(enemy_rect):
        print("아야!")
        running = False

    ####################################################################
    ## 5. 화면에 그리기
    ####################################################################

    screen.blit(background, (0, 0))         # 배경 그리기

    screen.blit(character, (character_x_pos, character_y_pos))  # 캐릭터 그리기
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))              # 적 그리기

    str_score = "Score : " + str(total_score)
    score = game_font.render(str(str_score), True, (255, 255, 255))
    screen.blit(score, (10, 10))

    ####################################################################
    ## 6. 화면 업데이트
    ####################################################################
    pygame.display.update()                 # 프레임마다 화면 update

# 종료 전 대기
# pygame.time.delay(1000) # 2초 정도 대기 후 게임 종료

# pygame 종료
pygame.quit()

