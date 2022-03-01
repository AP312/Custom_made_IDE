from tkinter import *

def draw(event):
	x1,y1=(event.x-1),(event.y-1)
	x2,y2=(event.x+1),(event.y+1)
	c.create_oval(x1,y1,x2,y2)

test = Tk()
test.geometry("1000x500")
test.title("Demo app")

c = Canvas(test,width=1000,height=800,cursor='pencil')
c.pack()
c.bind("<B1-Motion>",draw)

test.mainloop()
