import tkinter as tk
import tkinter.font as tkFont
import racesearch

class App:
    def __init__(self, root):
        #setting title
        root.title("raceFinder")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        guititle=tk.Message(root)
        ft = tkFont.Font(family='Times',size=16)
        guititle["font"] = ft
        guititle["fg"] = "#333333"
        guititle["justify"] = "left"
        guititle["text"] = "raceFinder"
        guititle.place(x=50,y=30,width=200,height=50)

        region=tk.Entry(root)
        region["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        region["font"] = ft
        region["fg"] = "#333333"
        region["justify"] = "center"
        region["text"] = "Region"
        region.place(x=50,y=80,width=250,height=25)

        state=tk.Entry(root)
        state["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        state["font"] = ft
        state["fg"] = "#333333"
        state["justify"] = "center"
        state["text"] = "State"
        state.place(x=50,y=120,width=250,height=25)

        distance=tk.Entry(root)
        distance["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        distance["font"] = ft
        distance["fg"] = "#333333"
        distance["justify"] = "center"
        distance["text"] = "Distance"
        distance.place(x=50,y=160,width=250,height=25)

        year=tk.Entry(root)
        year["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        year["font"] = ft
        year["fg"] = "#333333"
        year["justify"] = "center"
        year["text"] = "Year"
        year.place(x=50,y=200,width=250,height=25)

        eventtype=tk.Entry(root)
        eventtype["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        eventtype["font"] = ft
        eventtype["fg"] = "#333333"
        eventtype["justify"] = "center"
        eventtype["text"] = "Event Type"
        eventtype.place(x=50,y=240,width=250,height=25)

        parameters = [region, state, distance, year, eventtype]

        createCSV=tk.Button(root)
        createCSV["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        createCSV["font"] = ft
        createCSV["fg"] = "#000000"
        createCSV["justify"] = "center"
        createCSV["text"] = "Create CSV File"
        createCSV.place(x=150,y=350,width=300,height=45)
        createCSV["command"] = self.createCSV_command

        showTopResult=tk.Button(root)
        showTopResult["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        showTopResult["font"] = ft
        showTopResult["fg"] = "#000000"
        showTopResult["justify"] = "center"
        showTopResult["text"] = "Show Top Result"
        showTopResult.place(x=150,y=400,width=300,height=45)
        showTopResult["command"] = self.showTopResult_command


    def createCSV_command(self):
        print("command")


    def showTopResult_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
