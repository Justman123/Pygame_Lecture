import pygame

# 파이게임 초기화
pygame.init()

# 창 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width,screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("나의 첫 파이게임") # 게임 이름

# 배경 이미지 불러오기
background = pygame.image.load("C:/Users/gunho/OneDrive/바탕 화면/pythonWorkSpace/pygame_basic/background.png")

# 이벤트 루프
running = True
while running:
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
        if (event.type == pygame.QUIT): # 창이 닫히는 이벤트가 발생 하였는가?
            running = False
    screen.blit(background, (0,0)) # 배경 그리기

    pygame.display.update() # 게임 화면 그리기
# pygmae 종료
pygame.quit()
