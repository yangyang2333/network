from tkinter import *
import tkinter as tk
import tkinter.filedialog
from PIL import Image,ImageTk

def op():
    filename=tk.filedialog.askopenfilename()
    print(filename)

window=tk.Tk()
window.geometry('800x800')
menubar = tk.Menu(window)
##定义一个空菜单单元
filemenu = tk.Menu(menubar, tearoff=0)
##将上面定义的空菜单命名为`File`，放在菜单栏中，就是装入那个容器中
menubar.add_cascade(label='File', menu=filemenu)
##在`File`中加入`New`的小菜单，即我们平时看到的下拉菜单，每一个小菜单对应命令操作。
##如果点击这些单元, 就会触发`do_job`的功能
filemenu.add_command(label='Open', command=op)
filemenu.add_separator()##这里就是一条分割线
##同样的在`File`中加入`Exit`小菜单,此处对应命令为`window.quit`
filemenu.add_command(label='Exit', command=window.quit)
window.config(menu=menubar)
L1=tk.Label(window,text='CC')
L1.pack()
canvas = tk.Canvas(window, bg='white', height=400, width=400,)
pilimage=Image.open('max.jpg')
w,h=pilimage.size
w2=200
h2=200
tkImage=ImageTk.PhotoImage(pilimage)
image=canvas.create_image(0,0,anchor='nw',image=tkImage)
canvas.place(x=200,y=250,anchor='nw')
group = tk.LabelFrame(window, text="Group", padx=5, pady=5,bg='blue')
nodes_num=Label(group,text='number of nodes').pack()
edges_num=Label(group,text='number of edges').pack()
label_cluster_coefficient=Label(group,text='CC').pack()
label_coreness=Label(group,text='coreness').pack()
group.place(x=20,y=200,anchor='nw')

window.mainloop()
