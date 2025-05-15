####################################################################
# Project)

# [조건]
# 1. 캐릭터는 화면 아래 위치, 좌우 이동만 허용
# 2. space 키로 무기 쏘아올리기
# 3. 게임 시작 시 큰 공 1개 나타나서 바운스
# 4. 공이 무기에 닿으면 작은 크기의 공 2개로 분할, 가장 작은 크기의 공은 사라짐
# 5. 모든 공 없애면 게임 종료 (win)
# 6. 공에 닿으면 게임 종료 (lose)
# 7. 시간 제한 (99초) 초과 시 게임 종료 (lose)
# 8. FPS 30 (필요시 speed 값 조정)

# [이미지]
# 1. 배경 : 640*480 (가로*세로) - background.png
# 2. 무대 : 640*50 - stage.png
# 3. 캐릭터 : 33*60 - character.png
# 4. 무기 : 20*430 - weapon.png
# 5. 공 : 160*160, 80*80, 40*40, 20*20 - balloon1 ~ 4.png
####################################################################

import os
import pygame

####################################################################
## 0. 기본 초기화
##  1) init() 처리
##  2) Layout 설정
####################################################################

pygame.init()   # 초기화

#화면 크기 설정
screen_width    = 640
screen_height   = 480
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption('My Second Game!(Pang)')

# FPS
clock = pygame.time.Clock()

####################################################################
## 1. 사용자 게임 초기화
##  - 배경화면, 이미지, 좌표, 속도, 폰트 등등
####################################################################

# 배경 이미지 불러오기
current_path = os.path.dirname(__file__)    # 현재 파일의 위치 반환
image_path = os.path.join(current_path, "images")   # image 폴더 위치 반환


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

# 적 캐릭터 불러오기    //// "캐릭터 불러오기" 함수 만들어서 사용해 보기!
enemy           = pygame.image.load("C:/IT_Study/Python/Python_Game_Making/pygmae_basic/enemy.png")
enemy_size      = enemy.get_rect().size # 이미지 크기를 구해옴
enemy_width     = enemy_size[0]         # 캐릭터 가로 크기
enemy_height    = enemy_size[1]         # 캐릭터 세로 크기
enemy_x_pos     = (screen_width - enemy_width) / 2      # 화면 가로의 절반 크기 = 정중앙 (가로)
enemy_y_pos     = (screen_height - enemy_height) / 2    # 화면 세로 크기 = 가장 아래 (세로)

# 폰트 정의
game_font = pygame.font.Font(None, 40)  # 폰트 객체 생성 (font, size)

# 게임 플레이 시간
total_time = 10

# 시작 시간
start_ticks = pygame.time.get_ticks()   # 프로그램 시작 tick 받아오기

# 이벤트 루프
running = True  # 게임 실행중인가?
while running:
    dt = clock.tick(60) # 게임 화면 초당 프레임 수를 넣어준다

    ####################################################################
    ## 2. event 처리
    ####################################################################

    for event in pygame.event.get():
        if event.type == pygame.QUIT:       # 확인한 이벤트가 Quit일 때 아래를 실행
            running = False                 # 게임 종료

        ####################################################################
        ## 3. 게임 캐릭터 위치 정의의
        ####################################################################

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

    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

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

    # 타이머 text 표시
    # 경과 시간 계산
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000   # (ms) -> (s)

    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255, 255, 255))
    # (text, antialias, color[tuple], background color(생략시 투명))
    screen.blit(timer, (10, 10))

    # total - elapsed time < 0 일 때 게임 종료
    if total_time - elapsed_time <= 0:
        print("종료!")
        running = False

    ####################################################################
    ## 6. 화면 업데이트
    ####################################################################
    pygame.display.update()                 # 프레임마다 화면 update

# 종료 전 대기
pygame.time.delay(1000) # 2초 정도 대기 후 게임 종료

# pygame 종료
pygame.quit()

# https://www.youtube.com/watch?v=Dkx8Pl6QKW0&list=PL8vjco9na8CMCEetkzBf_ALw5VTpRgYIK&index=6&t=1s