from PIL import Image, ImageTk
import PIL
from tkinter import *
import tkinter
import math
import AStar


# he,heczad
class chess_board:
    startXY = None
    endXY = None

    to_green = AStar.Green.TO_GREEN

    def __init__(self, board_size):
        self.chess_board_arr = []

        self.root = Tk()
        self.default_size = board_size * 60
        self.start_flag = False
        self.finish_flag = False

        s_img = PIL.Image.open("start.png")
        s_img = s_img.resize((60, 60))
        self.start_img = ImageTk.PhotoImage(s_img)

        g_img = PIL.Image.open("finish.png")
        g_img = g_img.resize((60, 60))
        self.goal_img = ImageTk.PhotoImage(g_img)

        img = PIL.Image.open("wall2.png")
        img = img.resize((60, 60))
        self.wall_image = ImageTk.PhotoImage(img)

        p_img = PIL.Image.open("way.png")
        p_img = p_img.resize((59, 59))
        self.path_img = ImageTk.PhotoImage(p_img)

        self.root.title("A* MAZE")
        self.root.minsize(width=self.default_size +
                          150, height=self.default_size)
        self.root.maxsize(width=self.default_size +
                          150, height=self.default_size)

        self.canvas = Canvas(
            self.root, width=self.default_size, height=self.default_size)
        self.canvas.pack(expand=YES, fill=BOTH)
        self.createCanvas(board_size)

        # Find the path button
        find_path_button = Button(
            self.canvas, text="Find the path", command=self.showCalculatedWay)  # then doo it
        find_path_button.pack()
        find_path_button.place(x=self.default_size + 50, y=10)

        restart_button = Button(self.root, text="Restart",
                                command=self.restart_program)
        restart_button.place(x=self.default_size + 50, y=50)
        

        # Bind button clicks
        self.canvas.bind("<Button-1>", self.mouse_click)
        self.canvas.bind("<Button-2>", self.MidMouseClick)
        self.canvas.bind("<Button-3>", self.RightMouseClick)
        self.root.mainloop()

    @staticmethod
    def showChessArray(self):
        print(self.chess_board_arr)

    def returnChessArray(self):
        return self.chess_board_arr

    def restart_program(self):
        self.root.destroy()
        chess_board(13)

    def mouse_click(self, event):
        # Wall
        x = math.ceil(event.x / 60 - 1)
        y = math.ceil(event.y / 60 - 1)
        if self.chess_board_arr[x][y] == 0:
            self.putFigure(x, y)
            self.chess_board_arr[x][y] = 1
        else:
            self.deleteFigure(x, y)
            self.chess_board_arr[x][y] = 0

    def createCanvas(self, n):
        for i in range(n):
            temp_arr = []
            for j in range(n):
                self.deleteFigure(i, j)
                temp_arr.append(0)
            self.chess_board_arr.append(temp_arr)

    def putFigure(self, x, y):
        self.canvas.create_image(
            x * 60 + 30, y * 60 + 30, image=self.wall_image)

    def deleteFigure(self, x, y):
        self.canvas.create_rectangle(
            x * 60, y * 60, x * 60 + 60, y * 60 + 60, fill="#F9F9F9")

    def RightMouseClick(self, event):
        # START
        if self.start_flag:
            return
        x = math.ceil(event.x / 60 - 1)
        y = math.ceil(event.y / 60 - 1)
        if self.chess_board_arr[x][y] == 0:
            self.putStart(x, y)
            self.startXY = (y, x)
            self.start_flag = True
        else:
            self.deleteFigure(x, y)
            self.start_flag = False

    def putStart(self, x, y):
        self.canvas.create_image(
            x * 60 + 30, y * 60 + 30, image=self.start_img)

    def MidMouseClick(self, event):
        # END
        if self.finish_flag:
            return
        x = math.ceil(event.x / 60 - 1)
        y = math.ceil(event.y / 60 - 1)
        if self.chess_board_arr[x][y] == 0:
            self.putEnd(x, y)
            self.endXY = (y, x)
            self.finish_flag = True
        else:
            self.finish_flag = False
            self.deleteFigure(x, y)

    def putEnd(self, x, y):
        self.canvas.create_image(
            x * 60 + 30, y * 60 + 30, image=self.goal_img)

    def showCalculatedWay(self):

        AStar.solve(self)
        path_array = AStar.solve(self)

        for each in path_array[1:-1:]:
            self.canvas.create_image(
                each[1] * 60 + 30, each[0] * 60 + 30, image=self.path_img)

        
