from tkinter import *
from PIL import ImageTk, Image
import numpy as np


root = Tk()
root.title('Crack The Maze')    
root.configure(bg='gray')
root.geometry('400x400')
def reset_it():
    #remove from the original spot
    old_number = (player_pos[0]-2)*5 + player_pos[1] + 1
    blank = ImageTk.PhotoImage(Image.open('true.png'))
    dic[old_number].configure(image=blank, width=75, height=75)
    dic[old_number].image = blank

    #update back to the origin
    player_here = ImageTk.PhotoImage(Image.open('player.png'))
    grid_0_0.configure(image=player_here, width=75, height=75)
    grid_0_0.image = player_here
    
    #also update player's position
    player_pos[0] = 2
    player_pos[1] = 0



def go_back():
    return


def go_next():
    return


#title
title = Label(root, text='Welcome to Crack The Maze')
title.grid(row=0, column=0, columnspan=5)


#control panel
reset = Button(root, text='reset',command=reset_it, padx=40, pady=10, bg='green')
exit = Button(root, text='quit', command=root.quit, padx=40, pady=10, fg='white', bg='red')
reset.grid(row=1, column=0, columnspan=3)
exit.grid(row=1,column=3, columnspan=2)





#maze
#load the datasheet as a matrix
maze_grid = np.loadtxt(open("datasheet/datasheet_0.csv", "rb"), delimiter=",", skiprows=1)
#dimension of the grid
grid_dim_x = len(maze_grid)
grid_dim_y = len(maze_grid[0])


#first row
img_1 = ImageTk.PhotoImage(Image.open('player.png'))
grid_0_0 = Label(image=img_1,width=75,height=75)
grid_0_0.grid(row=2, column=0)

img_2 = ImageTk.PhotoImage(Image.open('false.png'))
grid_0_1 = Label(image=img_2,width=75,height=75)
grid_0_1.grid(row=2, column=1)

img_3 = ImageTk.PhotoImage(Image.open('false.png'))
grid_0_2 = Label(image=img_3,width=75,height=75)
grid_0_2.grid(row=2, column=2)

img_4 = ImageTk.PhotoImage(Image.open('false.png'))
grid_0_3 = Label(image=img_4,width=75,height=75)
grid_0_3.grid(row=2, column=3)

img_5 = ImageTk.PhotoImage(Image.open('false.png'))
grid_0_4 = Label(image=img_5,width=75,height=75)
grid_0_4.grid(row=2, column=4)


#second row
img_6 = ImageTk.PhotoImage(Image.open('true.png'))
grid_1_0 = Label(image=img_6,width=75,height=75)
grid_1_0.grid(row=3, column=0)
img_7 = ImageTk.PhotoImage(Image.open('false.png'))
grid_1_1 = Label(image=img_7,width=75,height=75)
grid_1_1.grid(row=3, column=1)
img_8 = ImageTk.PhotoImage(Image.open('true.png'))
grid_1_2 = Label(image=img_8,width=75,height=75)
grid_1_2.grid(row=3, column=2)
img_9 = ImageTk.PhotoImage(Image.open('true.png'))
grid_1_3 = Label(image=img_9,width=75,height=75)
grid_1_3.grid(row=3, column=3)
img_10 = ImageTk.PhotoImage(Image.open('true.png'))
grid_1_4 = Label(image=img_10,width=75,height=75)
grid_1_4.grid(row=3, column=4)


#third row
img_11 = ImageTk.PhotoImage(Image.open('true.png'))
grid_2_0 = Label(image=img_11,width=75,height=75)
grid_2_0.grid(row=4, column=0)

img_12 = ImageTk.PhotoImage(Image.open('true.png'))
grid_2_1 = Label(image=img_12,width=75,height=75)
grid_2_1.grid(row=4, column=1)

img_13 = ImageTk.PhotoImage(Image.open('true.png'))
grid_2_2 = Label(image=img_13,width=75,height=75)
grid_2_2.grid(row=4, column=2)

img_14 = ImageTk.PhotoImage(Image.open('false.png'))
grid_2_3 = Label(image=img_14,width=75,height=75)
grid_2_3.grid(row=4, column=3)

img_15 = ImageTk.PhotoImage(Image.open('true.png'))
grid_2_4 = Label(image=img_15,width=75,height=75)
grid_2_4.grid(row=4, column=4)


#fourth row
img_16 = ImageTk.PhotoImage(Image.open('false.png'))
grid_3_0 = Label(image=img_16,width=75,height=75)
grid_3_0.grid(row=5, column=0)

img_17 = ImageTk.PhotoImage(Image.open('false.png'))
grid_3_1 = Label(image=img_17,width=75,height=75)
grid_3_1.grid(row=5, column=1)

img_18 = ImageTk.PhotoImage(Image.open('false.png'))
grid_3_2 = Label(image=img_18,width=75,height=75)
grid_3_2.grid(row=5, column=2)

img_19 = ImageTk.PhotoImage(Image.open('false.png'))
grid_3_3 = Label(image=img_19,width=75,height=75)
grid_3_3.grid(row=5, column=3)

img_20 = ImageTk.PhotoImage(Image.open('exit.png'))
grid_3_4 = Label(image=img_20,width=75,height=75)
grid_3_4.grid(row=5, column=4)


#a dictionary that maps labels to numeric values
dic = {
    1 : grid_0_0, 2 : grid_0_1, 3 : grid_0_2, 4 : grid_0_3, 5 : grid_0_4,
    6 : grid_1_0, 7 : grid_1_1, 8 : grid_1_2, 9 : grid_1_3, 10 :grid_1_4,
    11 : grid_2_0, 12 : grid_2_1, 13 : grid_2_2, 14 : grid_2_3, 15 : grid_2_4,
    16 : grid_3_0, 17 : grid_3_1, 18 : grid_3_2, 19 : grid_3_3, 20 : grid_3_4
}

#a set that keeps track of block cells
blocks = set()
blocks.add(2)
blocks.add(3)
blocks.add(4)
blocks.add(5)
blocks.add(7)
blocks.add(14)
blocks.add(16)
blocks.add(17)
blocks.add(18)
blocks.add(19)


#a variable that indicates that the player wins
win = 20


#player's initial position
info = grid_0_0.grid_info()
player_pos = [info["row"], info["column"]]


#judge whether the player already wins
def judge():
    position_number = (player_pos[0]-2)*5 + player_pos[1] + 1
    return win == position_number


def congrat():
    title['text'] = "You made it! Congratulations!"
    title.grid(row=0, column=0, columnspan=5)

def go_down(e):
    #update the old spot
    old_number = (player_pos[0]-2)*5 + player_pos[1] + 1
    if (old_number+5) not in blocks and (old_number+5) <= 20:
        #update image
        blank = ImageTk.PhotoImage(Image.open('true.png'))
        dic[old_number].configure(image=blank, width=75, height=75)
        dic[old_number].image = blank
        #update grid position
        rows = dic[old_number].grid_info()['row']
        cols = dic[old_number].grid_info()['column']
        dic[old_number].grid(row=rows, column=cols) 

        #update player's position
        player_pos[0] += 1
    
        #update the new spot
        new_number = (player_pos[0]-2)*5 + player_pos[1] + 1
        player = ImageTk.PhotoImage(Image.open('player.png'))
        dic[new_number].configure(image=player, width=75, height=75)
        row_2 = dic[new_number].grid_info()['row']
        col_2 = dic[new_number].grid_info()['column']
        dic[new_number].image = player
        dic[new_number].grid(row=row_2, column=col_2) 
        if judge():
            congrat()



def go_up(e): 
    #update the old spot
    old_number = (player_pos[0]-2)*5 + player_pos[1] + 1
    #not encounter blocks upward 
    if (old_number-5) not in blocks and (old_number-5) > 0:
        #update image
        blank = ImageTk.PhotoImage(Image.open('true.png'))
        dic[old_number].configure(image=blank, width=75, height=75)
        dic[old_number].image = blank
        #update grid position
        rows = dic[old_number].grid_info()['row']
        cols = dic[old_number].grid_info()['column']
        dic[old_number].grid(row=rows, column=cols) 

        #update player's position
        player_pos[0] -= 1
    
        #update the new spot
        new_number = (player_pos[0]-2)*5 + player_pos[1] + 1
        #update image
        player = ImageTk.PhotoImage(Image.open('player.png'))
        dic[new_number].configure(image=player, width=75, height=75)
        dic[new_number].image = player
        #update grid position
        row_2 = dic[new_number].grid_info()['row']
        col_2 = dic[new_number].grid_info()['column']
        dic[new_number].grid(row=row_2, column=col_2)
        if judge():
            congrat()


def go_left(e): 
    #update the old spot
    old_number = (player_pos[0]-2)*5 + player_pos[1] + 1
    #not encounter blocks upward 
    if (old_number-1) not in blocks and old_number % 5 != 1 :
        #update image
        blank = ImageTk.PhotoImage(Image.open('true.png'))
        dic[old_number].configure(image=blank, width=75, height=75)
        dic[old_number].image = blank
        #update grid position
        rows = dic[old_number].grid_info()['row']
        cols = dic[old_number].grid_info()['column']
        dic[old_number].grid(row=rows, column=cols) 

        #update player's position
        player_pos[1] -= 1
    
        #update the new spot
        new_number = (player_pos[0]-2)*5 + player_pos[1] + 1
        #update image
        player = ImageTk.PhotoImage(Image.open('player.png'))
        dic[new_number].configure(image=player, width=75, height=75)
        dic[new_number].image = player
        #update grid position
        row_2 = dic[new_number].grid_info()['row']
        col_2 = dic[new_number].grid_info()['column']
        dic[new_number].grid(row=row_2, column=col_2)
        if judge():
            congrat()


def go_right(e): 
    #update the old spot
    old_number = (player_pos[0]-2)*5 + player_pos[1] + 1
    #not encounter blocks upward 
    if (old_number+1) not in blocks and old_number % 5 != 0:
        #update image
        blank = ImageTk.PhotoImage(Image.open('true.png'))
        dic[old_number].configure(image=blank, width=75, height=75)
        dic[old_number].image = blank
        #update grid position
        rows = dic[old_number].grid_info()['row']
        cols = dic[old_number].grid_info()['column']
        dic[old_number].grid(row=rows, column=cols) 

        #update player's position
        player_pos[1] += 1
    
        #update the new spot
        new_number = (player_pos[0]-2)*5 + player_pos[1] + 1
        #update image
        player = ImageTk.PhotoImage(Image.open('player.png'))
        dic[new_number].configure(image=player, width=75, height=75)
        dic[new_number].image = player
        #update grid position
        row_2 = dic[new_number].grid_info()['row']
        col_2 = dic[new_number].grid_info()['column']
        dic[new_number].grid(row=row_2, column=col_2) 
        if judge():
            congrat()

#keyboard input
root.bind("<Down>", go_down)
root.bind("<Up>", go_up)
root.bind("<Left>", go_left)
root.bind("<Right>",go_right)


#mainloop
root.mainloop()