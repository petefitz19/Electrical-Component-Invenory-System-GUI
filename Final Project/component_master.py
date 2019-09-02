from tkinter import*
from tkinter import constants, Tk, StringVar, ttk
from ttkthemes import themed_tk as tk

from componentStorage import componentStorage

#----------------------------------------------------------------------------------------------------------------
# This is an Electrical Inventory Program. The necessary files are component_master.py and componentStorage.py
# To run the program, simply navigate to the 'Final Project' Folder and run the command 'python3 component_master.py'
#----------------------------------------------------------------------------------------------------------------

class mainWindow(tk.ThemedTk):

    def __init__(self):
        tk.ThemedTk.__init__(self)

        self.lblTitle = ttk.Label(self, text = "Electrical Components Inventory System", font = 'Arial 35 bold', anchor = CENTER)
        self.lblTitle.pack(side = TOP, fill = X)

        self.bottomFrame = ttk.Frame(self)
        self.bottomFrame.pack(side = TOP, fill = BOTH, expand = True)
        
        #---------------------------LEFT FRAME SELECTION----------------------------
        self.leftFrame = ttk.Frame(self.bottomFrame)
        self.leftFrame.pack(side = LEFT, fill = BOTH, expand = True)

        self.buttonAddComponent = ttk.Button(self.leftFrame, text = "Add Folder", command = self.addFolder)
        self.buttonAddComponent.pack(side = TOP, fill = X)

        self.leftTreeFrame = ttk.Frame(self.leftFrame)
        self.leftTreeFrame.pack(side = TOP, fill = BOTH, expand = True)

        self.folderList = ttk.Treeview(self.leftTreeFrame, columns = 0)
        self.folderList.heading("#0", text = "Folder Name", anchor = W)
        for i in c.categories:
            self.folderList.insert("", 'end', text = str(i))
        if(len(self.folderList.get_children()) > 0):
            startID = self.folderList.get_children()[0]
            self.folderList.focus(startID)
            self.folderList.selection_set(startID)
        self.folderList.bind('<Double-Button-1>', self.deleteFolder)
        self.folderList.bind('<ButtonRelease-1>', self.folderSelectHandler)

        self.folderList.pack(side = LEFT, fill = BOTH, expand = True)

        self.scrollbarLeft = ttk.Scrollbar(self.leftTreeFrame, command = self.folderList.yview)
        self.folderList.configure(yscroll = self.scrollbarLeft.set)
        self.scrollbarLeft.pack(side = LEFT, fill = Y)


        #---------------------------RIGHT FRAME SELECTION----------------------------
        self.rightFrame = ttk.Frame(self.bottomFrame)
        self.rightFrame.pack(side = LEFT, fill = BOTH, expand = True)

        self.buttonAddComponent = ttk.Button(self.rightFrame, text = "Add Component", command = self.addComponent)
        self.buttonAddComponent.pack(side = TOP, fill = X,)

        self.rightTreeFrame = ttk.Frame(self.rightFrame)
        self.rightTreeFrame.pack(side = TOP, fill = BOTH, expand = True)

        self.componentList = ttk.Treeview(self.rightTreeFrame, columns = 2)
        self.componentList["columns"] = ("one")
        self.componentList.heading("#0", text = "Name", anchor = W)
        self.componentList.heading("one", text = "Quantity", anchor = W)
        for i in c.currComponents:
            self.componentList.insert("", 'end', text = str(i.name), values = i.num)

        self.componentList.bind('<Double-Button-1>', self.componentSelectHandler)
        self.componentList.pack(side = LEFT, fill = BOTH, expand = True)

        self.scrollbarRight = ttk.Scrollbar(self.rightTreeFrame, command = self.componentList.yview)
        self.componentList.configure(yscroll = self.scrollbarRight.set)

        self.scrollbarRight.pack(side = LEFT, fill = Y)


    def folderSelectHandler(self, a):
        curSelected = self.folderList.focus()
        c.loadComponents(c.categories[self.folderList.index(curSelected)])
        self.clearComponentList()
        self.updateComponentList()

    def componentSelectHandler(self, a):
        curSelected = self.componentList.focus()
        self.selectComponent(self.componentList.index(curSelected))

    def clearFolderList(self):
        self.folderList.delete(*self.folderList.get_children())

    def clearComponentList(self):
        self.componentList.delete(*self.componentList.get_children())

    def updateFolderList(self):
        for i in c.categories:
            self.folderList.insert("", 'end', text = str(i))

    def updateComponentList(self):
        for i in c.currComponents:
            self.componentList.insert("", 'end', text = str(i.name), values = i.num)

    def addFolder(self):
        #print("addFolder pressed")
        folderWin = folderWindow()
        folderWin.grab_set()
        folderWin.attributes('-topmost', True)
        folderWin.set_theme('equilux')
        folderWin.wm_title("Add Folder")
        folderWin.wm_geometry("%dx%d+%d+%d" %(int(self.winfo_screenwidth()/4), int(self.winfo_screenheight()/10), int(self.winfo_screenwidth()/2 - self.winfo_screenwidth()/8 ), int(self.winfo_screenheight()/2 - self.winfo_screenheight()/20)))
        folderWin.mainloop()
        

    def selectComponent(self, component):
        #print("Component Selected")
        selectComponentWin = selectComponentWindow()
        selectComponentWin.grab_set()
        selectComponentWin.attributes('-topmost', True)
        selectComponentWin.set_theme('equilux')
        selectComponentWin.wm_title("Edit Component")
        selectComponentWin.wm_geometry("%dx%d+%d+%d" %(int(self.winfo_screenwidth()/3), int(self.winfo_screenheight()/2),int(self.winfo_screenwidth()/2 - self.winfo_screenwidth()/6), int(self.winfo_screenheight()/2) - self.winfo_screenheight()/4))
        selectComponentWin.mainloop()
    
    def deleteFolder(self, a):
        #print("folderDelete pressed")
        folderDeleteWin = folderDeleteWindow()
        folderDeleteWin.grab_set()
        folderDeleteWin.attributes('-topmost', True)
        folderDeleteWin.set_theme('equilux')
        folderDeleteWin.wm_title("Delete Folder")
        folderDeleteWin.wm_geometry("%dx%d+%d+%d" %(int(self.winfo_screenwidth()/4), int(self.winfo_screenheight()/10), int(self.winfo_screenwidth()/2 - self.winfo_screenwidth()/8 ), int(self.winfo_screenheight()/2 - self.winfo_screenheight()/20)))
        folderDeleteWin.mainloop()

    def addComponent(self):
        #print( "addComponent pressed")
        componentWin = componentWindow()
        componentWin.grab_set()
        componentWin.attributes('-topmost', True)
        componentWin.set_theme('equilux')
        componentWin.wm_title("Add Component")
        componentWin.wm_geometry("%dx%d+%d+%d" %(int(self.winfo_screenwidth()/2), int(self.winfo_screenheight()/2), int(self.winfo_screenwidth()/4), int(self.winfo_screenheight()/4)))
        componentWin.mainloop()

class componentWindow(tk.ThemedTk):
    def __init__(self):
        tk.ThemedTk.__init__(self)

        self.nameFrame = ttk.Frame(master = self)
        self.nameFrame.pack(side = TOP, fill = BOTH, expand = True)

        self.lblComponentName = ttk.Label(self.nameFrame, text = "Name:    ", font = 'Arial 20 bold')
        self.lblComponentName.pack(side = LEFT, fill = X, expand = True)

        self.entryComponentName = ttk.Entry(self.nameFrame)
        self.entryComponentName.pack(side = RIGHT, fill = X,  expand = True)

        self.numFrame = ttk.Frame(master = self)
        self.numFrame.pack(side = TOP, fill = BOTH, expand = True)

        self.lblComponentNumber = ttk.Label(self.numFrame, text = "Number:", font = 'Arial 20 bold')
        self.lblComponentNumber.pack(side = LEFT, fill = X, expand = True)

        self.entryComponentNumber = ttk.Entry(self.numFrame)
        self.entryComponentNumber.pack(side = RIGHT, fill = X, expand = True)

        self.buttonFrame = ttk.Frame(master = self)
        self.buttonFrame.pack(side = BOTTOM, fill = BOTH, expand = True)

        self.btnExit = ttk.Button(self.buttonFrame, text = "EXIT", command = self.destroy)
        self.btnExit.pack(side = LEFT, fill = BOTH, expand = True)

        self.btnAdd = ttk.Button(self.buttonFrame, text = "ADD", command = self.addComponent)
        self.btnAdd.pack(side = RIGHT, fill = BOTH, expand = True)

        self.textboxFrame = ttk.Frame(master = self)
        self.textboxFrame.pack(side = TOP, fill = BOTH, expand = True)

        self.lblComponentDescription = ttk.Label(self.textboxFrame, text = "Description:", font = 'Arial 20 bold')
        self.lblComponentDescription.pack(side = TOP, fill = X, expand = True)

        self.entryComponentDescription = Text(self.textboxFrame, background = 'gray32', foreground = 'gray64')
        self.entryComponentDescription.config(font=("Arial", 14, "bold"))
        self.entryComponentDescription.pack(side = TOP, fill = X, expand = True)

        

    def addComponent(self):
        name = self.entryComponentName.get().replace("\n", "")
        num = self.entryComponentNumber.get().replace("\n", "")
        desc = self.entryComponentDescription.get("0.0", END).replace("\n", " ")
        if(num == ""):
            num = 0
        c.addComponent(tempName = name, tempNum = num, tempDescription = desc)
        w.clearComponentList()
        w.updateComponentList()
        self.destroy()


class folderWindow(tk.ThemedTk):
    def __init__(self):
        tk.ThemedTk.__init__(self)
        self.nameFrame = ttk.Frame(self)
        self.nameFrame.pack(side = TOP, fill = BOTH, expand = True)

        self.lblFolderName = ttk.Label(self.nameFrame, text = "Name:", font = 'Arial 20 bold')
        self.lblFolderName.pack(side = LEFT, fill = X, expand = True)

        self.entryFolderName = ttk.Entry(self.nameFrame)
        self.entryFolderName.pack(side = RIGHT, fill = X, expand = True)

        self.buttonFrame = ttk.Frame(self)
        self.buttonFrame.pack(side = TOP, fill = BOTH, expand = True)

        self.btnExit = ttk.Button(self.buttonFrame, text = "EXIT", command = self.destroy)
        self.btnExit.pack(side = LEFT, fill = BOTH, expand = True)

        self.btnAdd = ttk.Button(self.buttonFrame, text = "ADD", command = self.addFolder)
        self.btnAdd.pack(side = RIGHT, fill = BOTH, expand = True)

    def addFolder(self):
        w.clearFolderList()
        c.addCategory(self.entryFolderName.get())
        for i in c.categories:
            w.folderList.insert("", 'end', text = str(i))
            
        self.destroy()

class folderDeleteWindow(tk.ThemedTk):
    def __init__(self):
        tk.ThemedTk.__init__(self)

        self.lblFolderName = ttk.Label(self, text = "Delete Folder?", font = 'Arial 20 bold', anchor = CENTER)
        self.lblFolderName.pack(side = TOP, fill = BOTH, expand = True)

        self.buttonFrame = ttk.Frame(self)
        self.buttonFrame.pack(side = TOP, fill = BOTH, expand = True)

        self.btnExit = ttk.Button(self.buttonFrame, text = "NO", command = self.exitWindow)
        self.btnExit.pack(side = LEFT, fill = BOTH, expand = True)

        self.btnAdd = ttk.Button(self.buttonFrame, text = "YES", command = self.deleteFolder)
        self.btnAdd.pack(side = RIGHT, fill = BOTH, expand = True)

    def exitWindow(self):
        self.destroy()

    def deleteFolder(self):
        w.clearComponentList()
        c.removeCategory(c.categories[w.folderList.index(w.folderList.focus())])
        w.folderList.delete(w.folderList.focus())
        self.destroy()

class selectComponentWindow(tk.ThemedTk):
    var1 = 0
    def __init__(self):
        self.var1 = int(c.currComponents[w.componentList.index(w.componentList.focus())].num)
        tk.ThemedTk.__init__(self)

        self.lblFolderName = ttk.Label(self, text = c.currComponents[w.componentList.index(w.componentList.focus())].name, font = 'Arial 20 bold', anchor = CENTER)
        self.lblFolderName.pack(side = TOP, fill = BOTH, expand = True)

        self.numFrame = ttk.Frame(self)
        self.numFrame.pack(side = TOP, fill = BOTH, expand = True)

        self.btnIncrease = ttk.Button(self.numFrame, text = "+", command = self.increment)
        self.btnIncrease.pack(side = LEFT, fill = BOTH, expand = True)

        self.lblCurrentQuantity = ttk.Label(self.numFrame, text = self.var1, font = 'Arial 20 bold', anchor = CENTER)
        self.lblCurrentQuantity.pack(side = LEFT, fill = BOTH, expand = True)

        self.btnDecrease = ttk.Button(self.numFrame, text = "-", command = self.decrement)
        self.btnDecrease.pack(side = RIGHT, fill = BOTH, expand = True)

        self.btnConfirm = ttk.Button(self, text = "Confirm", command = self.confirmQuantity)
        self.btnConfirm.pack(side = BOTTOM, fill = BOTH, expand = True)

        self.buttonFrame = ttk.Frame(self)
        self.buttonFrame.pack(side = BOTTOM, fill = BOTH, expand = True)

        self.btnExit = ttk.Button(self.buttonFrame, text = "Cancel", command = self.destroy)
        self.btnExit.pack(side = LEFT, fill = BOTH, expand = True)

        self.btnAdd = ttk.Button(self.buttonFrame, text = "Delete", command = self.deleteComponent)
        self.btnAdd.pack(side = RIGHT, fill = BOTH, expand = True)

        self.lblDescription = Text(self, background = 'gray33', highlightthickness=0, foreground = 'gray64', pady = 2, padx = 2)
        self.lblDescription.insert('1.0', c.currComponents[w.componentList.index(w.componentList.focus())].description)
        self.lblDescription.config(state=DISABLED, font=("Arial", 12, "bold"))
        self.lblDescription.pack(side = TOP, fill = BOTH, expand = True)

        

    def deleteComponent(self):
        #print("Component Deleted")
        c.removeComponent(c.currComponents[w.componentList.index(w.componentList.focus())].name)
        w.componentList.delete(w.componentList.focus())
        self.destroy()

    def confirmQuantity(self):
        #print("Quantity confirmed")
        c.changeComponentNum(c.currComponents[w.componentList.index(w.componentList.focus())].name, self.var1)
        w.clearComponentList()
        w.updateComponentList()
        self.destroy()

    def increment(self):
        self.var1 += 1
        self.lblCurrentQuantity.configure(text = str(self.var1))

    def decrement(self):
        self.var1 -= 1
        self.lblCurrentQuantity.configure(text = str(self.var1))

c = componentStorage()
c.categoriesInit()
if(len(c.categories) > 0):
    c.loadComponents(c.categories[0])

w = mainWindow()
w.set_theme('equilux')
w.geometry("%dx%d+0+0" %(w.winfo_screenwidth(), w.winfo_screenheight()))
w.title("Electrical Components GUI")
w.mainloop()
