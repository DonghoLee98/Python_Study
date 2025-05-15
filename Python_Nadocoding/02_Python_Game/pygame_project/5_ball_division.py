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

# 배경 만들기
background = pygame.image.load(os.path.join(image_path, "background.png"))

# 스테이지 만들기
stage = pygame.image.load(os.path.join(image_path, "stage.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1]    # 스테이지 높이 위에 캐릭터 두기 위함

# 캐릭터 만들기
character = pygame.image.load(os.path.join(image_path, "character.png"))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width - character_width) / 2
character_y_pos = (screen_height - (stage_height + character_height))

# 캐릭터 이동 방향
character_to_x = 0  # y방향은 필요없음

# 캐릭터 이동 속도
character_speed = 5

# 무기 만들기
weapon = pygame.image.load(os.path.join(image_path, "weapon.png"))
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]

# 무기는 한 번에 여러 발 발사 가능
weapons = []

# 무기 이동 속도
weapon_speed = 10

# 공 만들기 (4 개 크기에 대해 독립적으로 처리)
ball_images = [
    pygame.image.load(os.path.join(image_path, "balloon1.png")),
    pygame.image.load(os.path.join(image_path, "balloon2.png")),
    pygame.image.load(os.path.join(image_path, "balloon3.png")),
    pygame.image.load(os.path.join(image_path, "balloon4.png"))]

# 공 크기에 따른 최초 스피드
ball_speed_y = [-18, -15, -12, -9]  # index 0, 1, 2, 3 의 값

# 공 info   (dictionary)
balls = []

balls.append({
    "pos_x" : 50,   # 공의 x 좌표
    "pos_y" : 50,   # 공의 y 좌표
    "img_idx" : 0,  # 공의 이미지 인덱스
    "to_x" : 3,     # 공의 x축 이동방향 (3 : 우 / -3 : 좌)
    "to_y" : -6,    # 공의 y축 이동방향
    "init_spd_y" : ball_speed_y[0]})    # 공 최초 속도

# 사라질 무기, 공 정보 저장 변수
weapon_to_remove = -1
ball_to_remove = -1

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

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                character_to_x -= character_speed   # 캐릭터 오른쪽 이동
            elif event.key == pygame.K_RIGHT:
                character_to_x += character_speed   # 캐릭터 왼쪽 이동
            elif event.key == pygame.K_SPACE:
                weapon_x_pos = character_x_pos + ((character_width - weapon_width) / 2)
                weapon_y_pos = character_y_pos
                weapons.append([weapon_x_pos, weapon_y_pos])

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                character_to_x = 0

    ####################################################################
    # 3. 게임 캐릭터 위치 정의
    ####################################################################

    character_x_pos += character_to_x

    # 캐릭터 가로 이동 한계 지정
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    # 무기 위치 조정
    # w[0] : 무기의 x 위치값
    # w[1] : 무기의 y 위치값
    # 이중 list 이므로 이 점에 유의!
    weapons = [ [w[0], w[1] - weapon_speed] for w in weapons] # 무기 위치를 위로 올림

    # 천장에 닿은 무기 없애기
    # 천장에 닿지 않은 무기들만 다시 값을 weapons 리스트에 저장하겠다는 뜻
    # 오버라이드 이므로, weapons 리스트를 초기화하고 다시 담게 되니 자연스럽게 삭제?되는 효과
    weapons = [ [w[0], w[1]] for w in weapons if w[1] > 0]

    # 공 위치 정의
    for ball_idx, ball_val in enumerate(balls):
        ball_pos_x = ball_val["pos_x"]
        ball_pos_y = ball_val["pos_y"]
        ball_img_idx = ball_val["img_idx"]

        ball_size = ball_images[ball_img_idx].get_rect().size
        ball_width = ball_size[0]
        ball_height = ball_size[1]

        # 벽에 닿았을 때, 튕겨서 방향이 바뀌는 효과
        if ball_pos_x < 0 or ball_pos_x > screen_width - ball_width:
            ball_val["to_x"] = ball_val["to_x"] * -1

        # 세로 위치
        # 공이 바닥 상태일 때 (튕겨 올라가는 순간)
        if ball_pos_y >= screen_height - stage_height - ball_height:
            ball_val["to_y"] = ball_val["init_spd_y"]
        else:   # 그 외 모든 경우, 아래로 가속도 받도록 한다 (시작값이 (-)라, 포물선 운동 한다)
            ball_val["to_y"] += 0.5

        ball_val["pos_x"] += ball_val["to_x"]
        ball_val["pos_y"] += ball_val["to_y"]


    ####################################################################
    ## 4. 충돌 처리
    ####################################################################

    # 캐릭터 rect 정보 업데이트
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    for ball_idx, ball_val in enumerate(balls):
        ball_pos_x = ball_val["pos_x"]
        ball_pos_y = ball_val["pos_y"]
        ball_img_idx = ball_val["img_idx"]

        # 공 rect 정보 업데이트
        ball_rect = ball_images[ball_img_idx].get_rect()
        ball_rect.left = ball_pos_x
        ball_rect.top = ball_pos_y

        # 공과 캐릭터 충돌 체크크
        if character_rect.colliderect(ball_rect):
            running = False
            break

        # 공과 무기들 충돌 처리
        for weapon_idx, weapon_val in enumerate(weapons):
            weapon_pos_x = weapon_val[0]
            weapon_pos_y = weapon_val[1]

            # 무기 rect 정보 업데이트
            weapon_rect = weapon.get_rect()
            weapon_rect.left = weapon_pos_x
            weapon_rect.top = weapon_pos_y

            # 충돌 체크
            if weapon_rect.colliderect(ball_rect):
                weapon_to_remove = weapon_idx   # 공에 닿은 무기 없애기 위한 값 설정
                ball_to_remove = ball_idx       # 무기에 닿은 공 없애기 위한 값 설정
                
                # 원래 있던 상위의 공 없애고 하위의 공 2개로 분리
                if ball_img_idx < 3:
                    # 현재 공 크기 가져오기 (상위 공 위치에서 쪼개져야 함)
                    ball_width = ball_rect.size[0]
                    ball_height = ball_rect.size[1]

                    # 나눠진 공 정보
                    small_ball_rect = ball_images[ball_img_idx + 1].get_rect()
                    small_ball_width = small_ball_rect.size[0]
                    small_ball_height = small_ball_rect.size[1]

                    # 왼쪽으로 튕기는 하위 공 추가
                    balls.append({
                        "pos_x" : ball_pos_x + ((ball_width - small_ball_width) / 2),   # 공의 x 좌표
                        "pos_y" : ball_pos_y + ((ball_height - small_ball_height) / 2),   # 공의 y 좌표
                        "img_idx" : ball_img_idx + 1,  # 공의 이미지 인덱스
                        "to_x" : -3,     # 공의 x축 이동방향 (3 : 우 / -3 : 좌)
                        "to_y" : -6,    # 공의 y축 이동방향
                        "init_spd_y" : ball_speed_y[ball_img_idx + 1]})    # 공 최초 속도
                    
                    # 오른쪽으로 튕기는 하위 공 추가
                    balls.append({
                        "pos_x" : ball_pos_x + ((ball_width - small_ball_width) / 2),   # 공의 x 좌표
                        "pos_y" : ball_pos_y + ((ball_height - small_ball_height) / 2),   # 공의 y 좌표
                        "img_idx" : ball_img_idx + 1,  # 공의 이미지 인덱스
                        "to_x" : 3,     # 공의 x축 이동방향 (3 : 우 / -3 : 좌)
                        "to_y" : -6,    # 공의 y축 이동방향
                        "init_spd_y" : ball_speed_y[ball_img_idx + 1]})    # 공 최초 속도
                break

    # 충돌된 공 or 무기 없애기
    if ball_to_remove > -1:
        del balls[ball_to_remove]
        ball_to_remove = -1

    if weapon_to_remove > -1:
        del weapons[weapon_to_remove]
        weapon_to_remove = -1


    ####################################################################
    ## 5. 화면에 그리기
    ####################################################################

    screen.blit(background, (0, 0))         # 배경 그리기
    for weapon_x_pos, weapon_y_pos in weapons:
        screen.blit(weapon, (weapon_x_pos, weapon_y_pos))

    for idx, val in enumerate(balls):
        ball_pos_x = val["pos_x"]
        ball_pos_y = val["pos_y"]
        ball_img_idx = val["img_idx"]
        screen.blit(ball_images[ball_img_idx], (ball_pos_x, ball_pos_y))

    screen.blit(stage, (0, screen_height - stage_height))
    screen.blit(character, (character_x_pos, character_y_pos))


    ####################################################################
    ## 6. 화면 업데이트
    ####################################################################
    pygame.display.update()                 # 프레임마다 화면 update

# 종료 전 대기
# pygame.time.delay(1000) # 2초 정도 대기 후 게임 종료

# pygame 종료
pygame.quit()

# https://www.youtube.com/watch?v=Dkx8Pl6QKW0&list=PL8vjco9na8CMCEetkzBf_ALw5VTpRgYIK&index=6&t=1s