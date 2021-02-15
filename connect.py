import numpy as np 
import pygame
import math 

ROWS=6
COLUMNS = 7

image = pygame.image.load("pop.png")
board= np.zeros((ROWS,COLUMNS))

SLOT=100
width = COLUMNS * SLOT
height = (ROWS+1) * SLOT
size = (width,height)

RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
GRAY = (128,128,128)
OFFSET = 100
RADIUS = int((SLOT/2) - 5)

game_over =False

turn =0 # to indicate the turn of player

def draw_board(board):
    pygame.draw.rect(window,GRAY,(0,0,width,SLOT))
    for c in range(COLUMNS):
        for r in range(ROWS):
            rect = (c*SLOT,r*SLOT*OFFSET,SLOT,SLOT)
            c1= (int(c*SLOT+SLOT/2),int(r*SLOT+OFFSET+SLOT/2))
            pygame.draw.rect(window,BLUE,rect)
            pygame.draw.circle(window,GRAY,c1,RADIUS)
    for c in range(COLUMNS):
        for r in range(ROWS):
            c2 = (int(c*SLOT+SLOT/2),int(r*SLOT+OFFSET+SLOT/2))
            if board[r][c] ==1:
                pygame.draw.circle(window,RED,c2,RADIUS)
            elif board[r][c]==2:
                pygame.draw.circle(window,GREEN,c2,RADIUS)       
    pygame.display.update()





#print(board)


def is_valid_location(board,col):
    return board[ROWS-1][col] == 0 #checks if it is empty or taken


def drop_piece(board,col,piece):
    for r in range(ROWS):
        if board[r][col]==0:
            row=r 
            break
    board[row][col] = piece

def is_winning_move(board,piece):
    #check horizontal location for win
    for c in range(COLUMNS-3):#as they cant win starting col=4
        for r in range(ROWS):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2]==piece and board[r][c+3]==piece:
                return True
    #check vertical location for win    
    for c in range(COLUMNS):#as they cant win starting ROWS=3
        for r in range(ROWS-3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c]==piece and board[r+3][c]==piece:
                return True
    #check for positive diagonal win
    for c in range(COLUMNS-3):#as they cant win starting col=4
        for r in range(ROWS-3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2]==piece and board[r+3][c+3]==piece:
                return True
    
    #check for negative diagonal win
    for c in range(COLUMNS-3):#as they cant win starting col=4
        for r in range(3,ROWS):
            if board[r][c] == piece and board[r-1][c-1] == piece and board[r-2][c-2]==piece and board[r-3][c-3]==piece:
                return True
    
print(board)

pygame.init()
window = pygame.display.set_mode(size)
pygame.display.set_caption("connect 4")
font = pygame.font.SysFont("Comic Sans MS",33,True)
draw_board(board)


while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        
        
        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(window,GRAY,(0,0,width,SLOT))
            posx = event.pos[0]
            if turn%2 ==0:
                pygame.draw.circle(window,RED,(posx,int(SLOT/2)),RADIUS)
            else:
                pygame.draw.circle(window,GREEN,(posx,int(SLOT/2)),RADIUS)    
        pygame.display.update()    

        if event.type ==pygame.MOUSEBUTTONDOWN:
            print(event.pos)
            
            if turn %2 ==0:
                #ask for player 1's input
                posx = event.pos[0]
                col = math.floor(posx/SLOT)
                #col=int(input("Player 1 please select your coumn please(0-6):  "))
                if is_valid_location(board,col):
                    drop_piece(board,col,1)
                    if is_winning_move(board,1):
                        #print("CONGRATS PLAYER 1")
                        label = font.render("Player 1 WON !",True,RED)
                        game_over =True
                else:
                    turn -=1
            else:
                #ask for player 2's input
                #col=int(input("Player 2 please select your coumn please(0-6):  "))
                
                posx = event.pos[0]
                col = math.floor(posx/SLOT)
                if is_valid_location(board,col):
                    drop_piece(board,col,2)
                    if is_winning_move(board,2):
                        #print("CONGRATS PLAYER 2")
                        label = font.render("Player 2 WON !",True,GREEN)
                        game_over =True
                else:
                    turn -=1
                

            turn = turn + 1
            print(np.flip(board,0))
            draw_board(board)

    if game_over:
        window.blit(image,(120,220))
        window.blit(label,(170,350))
        pygame.display.update()
        pygame.time.wait(3000)