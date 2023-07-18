import pygame

# 파이게임 초기화
pygame.init()

# 창 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width,screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("나의 첫 파이게임") # 게임 이름

# 이벤트 루프
running = True
while running:
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            running = False

# pygmae 종료
pygame.quit()
