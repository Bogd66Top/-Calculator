import tkinter as tk
import keyboard
from PIL import Image, ImageTk

ok = [False, False]
with open("resources\config.txt", "r") as f:
    save_config = f.readlines()
    for item_config_ in save_config:
        item_config = item_config_.split(":")
        if item_config[0] == "SizeX":
            scale_x = float(item_config[1])
            ok[0] = True
        elif item_config[0] == "SizeY":
            scale_y = float(item_config[1])
            ok[1] = True

if not(all(ok)):
    scale_x = 2
    scale_y = 2

w = tk.Tk()
w.title("Калькулятор")
w.geometry(f"{round(192*scale_x)}x{round(192*scale_y)}")
w.resizable(False, False)

icon_photo = ImageTk.PhotoImage(Image.open('resources\icon\icon.png'))
icon_settings = ImageTk.PhotoImage(Image.open('resources\icon\icon_settings.png'))

w.iconphoto(False, icon_photo)

save_data = None
with open("resources\data.txt", "r") as f:
    save_data = f.readline()


class Calculator:
    def __init__(self, inp_data=""):
        self.B_close = tk.Button(w, text="X", command=self.Close)
        self.B_Equals = tk.Button(w, text="=", command=self.Calculation)
        self.B_Plus = tk.Button(w, text="+", command=lambda: self.Add("+"))
        self.B_Minus = tk.Button(w, text="-", command=lambda: self.Add("-"))
        self.B_Multiply = tk.Button(w, text="*", command=lambda: self.Add("*"))
        self.B_Divide = tk.Button(w, text="/", command=lambda: self.Add("/"))
        self.E_InpOut = tk.Entry(w)
        self.B_rem = tk.Button(w, text="<-", command=self.Remove)
        
        self.B_1 = tk.Button(w, text="1", command=lambda: self.Add("1"))
        self.B_2 = tk.Button(w, text="2", command=lambda: self.Add("2"))
        self.B_3 = tk.Button(w, text="3", command=lambda: self.Add("3"))
        self.B_4 = tk.Button(w, text="4", command=lambda: self.Add("4"))
        self.B_5 = tk.Button(w, text="5", command=lambda: self.Add("5"))
        self.B_6 = tk.Button(w, text="6", command=lambda: self.Add("6"))
        self.B_7 = tk.Button(w, text="7", command=lambda: self.Add("7"))
        self.B_8 = tk.Button(w, text="8", command=lambda: self.Add("8"))
        self.B_9 = tk.Button(w, text="9", command=lambda: self.Add("9"))
        self.B_0 = tk.Button(w, text="0", command=lambda: self.Add("0"))
        self.B_point = tk.Button(w, text=".", command=lambda: self.Add("."))

        
        self.B_sL = tk.Button(w, text="(", command=lambda: self.Add("("))
        self.B_sR = tk.Button(w, text=")", command=lambda: self.Add(")"))
        self.B_Sq = tk.Button(w, text="x²", command=lambda: self.Add("**2"))
        self.B_SqC = tk.Button(w, text="√x", command=lambda: self.Add("**0.5"))
        self.B_Clear = tk.Button(w, text="C", command=self.Clear)

        self.B_Settings = tk.Button(w, image=icon_settings, command=self.Settings_)
        
        
        self.Add(inp_data)
    def Load(self):
        self.B_close.place(x=0*scale_x, y=0*scale_y, height=32*scale_x, width=32*scale_y)
        self.B_Settings.place(x=32*scale_x, y=0*scale_y, height=32*scale_x, width=32*scale_y)
        self.B_Equals.place(x=0*scale_x, y=32*scale_y, height=32*scale_x, width=32*scale_y)
        self.B_Plus.place(x=0*scale_x, y=64*scale_y, height=32*scale_x, width=32*scale_y)
        self.B_Minus.place(x=0*scale_x, y=96*scale_y, height=32*scale_x, width=32*scale_y)
        self.B_Multiply.place(x=0*scale_x, y=128*scale_y, height=32*scale_x, width=32*scale_y)
        self.B_Divide.place(x=0*scale_x, y=160*scale_y, height=32*scale_x, width=32*scale_y)
        self.E_InpOut.place(x=32*scale_x, y=32*scale_y, height=32*scale_x, width=128*scale_y)
        self.B_rem.place(x=160*scale_x, y=32*scale_y, height=32*scale_x, width=32*scale_y)
        
        self.B_1.place(x=32*scale_x, y=64*scale_y, height=32*scale_x, width=32*scale_y)
        self.B_2.place(x=64*scale_x, y=64*scale_y, height=32*scale_x, width=32*scale_y)
        self.B_3.place(x=96*scale_x, y=64*scale_y, height=32*scale_x, width=32*scale_y)
        self.B_4.place(x=32*scale_x, y=96*scale_y, height=32*scale_x, width=32*scale_y)
        self.B_5.place(x=64*scale_x, y=96*scale_y, height=32*scale_x, width=32*scale_y)
        self.B_6.place(x=96*scale_x, y=96*scale_y, height=32*scale_x, width=32*scale_y)
        self.B_7.place(x=32*scale_x, y=128*scale_y, height=32*scale_x, width=32*scale_y)
        self.B_8.place(x=64*scale_x, y=128*scale_y, height=32*scale_x, width=32*scale_y)
        self.B_9.place(x=96*scale_x, y=128*scale_y, height=32*scale_x, width=32*scale_y)
        self.B_0.place(x=64*scale_x, y=160*scale_y, height=32*scale_x, width=32*scale_y)
        self.B_point.place(x=96*scale_x, y=160*scale_y, height=32*scale_x, width=32*scale_y)

        
        self.B_sL.place(x=128*scale_x, y=64*scale_y, height=32*scale_x, width=32*scale_y)
        self.B_sR.place(x=128*scale_x, y=96*scale_y, height=32*scale_x, width=32*scale_y)
        self.B_Sq.place(x=128*scale_x, y=128*scale_y, height=32*scale_x, width=32*scale_y)
        self.B_SqC.place(x=128*scale_x, y=160*scale_y, height=32*scale_x, width=32*scale_y)

        self.B_Clear.place(x=160*scale_x, y=64*scale_y, height=32*scale_x, width=32*scale_y)
        
        
    def UnLoad(self):
        self.B_close.place_forget()
        self.B_Settings.place_forget()
        self.B_Equals.place_forget()
        self.B_Plus.place_forget()
        self.B_Minus.place_forget()
        self.B_Multiply.place_forget()
        self.B_Divide.place_forget()
        self.E_InpOut.place_forget()
        self.B_rem.place_forget()
        
        self.B_1.place_forget()
        self.B_2.place_forget()
        self.B_3.place_forget()
        self.B_4.place_forget()
        self.B_5.place_forget()
        self.B_6.place_forget()
        self.B_7.place_forget()
        self.B_8.place_forget()
        self.B_9.place_forget()
        self.B_0.place_forget()
        self.B_point.place_forget()

        self.B_sL.place_forget()
        self.B_sR.place_forget()
        self.B_Sq.place_forget()
        self.B_SqC.place_forget()

        self.B_Clear.place_forget()
        

    def Close(self):
        self.Save()
        S.Save()
        global runing
        runing = False
        w.destroy()
    def Settings_(self):
        self.UnLoad()
        S.Load()
        
    def Add(self, text_: str):
        text = self.E_InpOut.get()
        self.E_InpOut.delete(0, "end")
        self.E_InpOut.insert(0, text+text_)
    def Remove(self):
        text = self.E_InpOut.get()
        self.E_InpOut.delete(0, "end")
        self.E_InpOut.insert(0, text[0:-1])
    def Calculation(self):
        text = self.E_InpOut.get()
        self.E_InpOut.delete(0, "end")
        self.E_InpOut.insert(0, eval(text))
    def Clear(self):
        self.E_InpOut.delete(0, "end")
        self.E_InpOut.insert(0, "")
    def Save(self):
        with open("resources\data.txt", "w") as f:
            f.truncate()
            f.write(self.E_InpOut.get())

class Settings:
    def __init__(self):
        self.B_Back = tk.Button(w, image=icon_photo, command=self.Calculator_)
        self.L_Settings = tk.Label(w, image=icon_settings)
        
        self.B_Settings_Remove_1_x_size = tk.Button(w, text="<", command=lambda: self.Correct_X(-0.2))
        self.B_Settings_Remove_4_x_size = tk.Button(w, text="<<", command=lambda: self.Correct_X(-0.8))
        self.L_x_size = tk.Label(w, text=scale_x)
        self.B_Settings_Add_1_x_size = tk.Button(w, text=">", command=lambda: self.Correct_X(0.2))
        self.B_Settings_Add_4_x_size = tk.Button(w, text=">>", command=lambda: self.Correct_X(0.8))
        self.B_Settings_Remove_1_y_size = tk.Button(w, text="<", command=lambda: self.Correct_Y(-0.2))
        self.B_Settings_Remove_4_y_size = tk.Button(w, text="<<", command=lambda: self.Correct_Y(-0.8))
        self.L_y_size = tk.Label(w, text=scale_x)
        self.B_Settings_Add_1_y_size = tk.Button(w, text=">", command=lambda: self.Correct_Y(0.2))
        self.B_Settings_Add_4_y_size = tk.Button(w, text=">>", command=lambda: self.Correct_Y(0.8))
        
    def Load(self):
        self.B_Back.place(x=0*scale_x, y=0*scale_y, height=32*scale_x, width=32*scale_y)
        self.L_Settings.place(x=32*scale_x, y=0*scale_y, height=32*scale_x, width=32*scale_y)
        
        self.B_Settings_Remove_1_x_size.place(x=32*scale_x, y=32*scale_y, height=32*scale_x, width=32*scale_y)
        self.B_Settings_Remove_4_x_size.place(x=0*scale_x, y=32*scale_y, height=32*scale_x, width=32*scale_y)
        self.L_x_size.place(x=64*scale_x, y=38*scale_y, height=16*scale_x, width=32*scale_y)
        self.B_Settings_Add_1_x_size.place(x=96*scale_x, y=32*scale_y, height=32*scale_x, width=32*scale_y)
        self.B_Settings_Add_4_x_size.place(x=128*scale_x, y=32*scale_y, height=32*scale_x, width=32*scale_y)
        self.B_Settings_Remove_1_y_size.place(x=32*scale_x, y=64*scale_y, height=32*scale_x, width=32*scale_y)
        self.B_Settings_Remove_4_y_size.place(x=0*scale_x, y=64*scale_y, height=32*scale_x, width=32*scale_y)
        self.L_y_size.place(x=64*scale_x, y=72*scale_y, height=16*scale_x, width=32*scale_y)
        self.B_Settings_Add_1_y_size.place(x=96*scale_x, y=64*scale_y, height=32*scale_x, width=32*scale_y)
        self.B_Settings_Add_4_y_size.place(x=128*scale_x, y=64*scale_y, height=32*scale_x, width=32*scale_y)
        
    def UnLoad(self):
        self.B_Back.place_forget()
        self.L_Settings.place_forget()
        
        self.B_Settings_Remove_1_x_size.place_forget()
        self.B_Settings_Remove_4_x_size.place_forget()
        self.L_x_size.place_forget()
        self.B_Settings_Add_1_x_size.place_forget()
        self.B_Settings_Add_4_x_size.place_forget()
        self.B_Settings_Remove_1_y_size.place_forget()
        self.B_Settings_Remove_4_y_size.place_forget()
        self.L_y_size.place_forget()
        self.B_Settings_Add_1_y_size.place_forget()
        self.B_Settings_Add_4_y_size.place_forget()
        
    def UpDate(self):
        self.UnLoad()
        self.Load()
    def Correct_X(self, force):
        global scale_x
        scale_x += force
        self.L_x_size.config(text=scale_x)
        self.UpDate()
        w.geometry(f"{round(192*scale_x)}x{round(192*scale_y)}")
    def Correct_Y(self, force):
        global scale_y
        scale_y += force
        self.L_y_size.config(text=scale_y)
        self.UpDate()
        w.geometry(f"{round(192*scale_x)}x{round(192*scale_y)}")
    def Calculator_(self):
        self.UnLoad()
        CL.Load()
    def Save(self):
        with open("resources\config.txt", "w") as f:
            f.truncate()
            f.write(f"SizeX:{round(scale_x)}\n")
            f.write(f"SizeY:{round(scale_y)}")




CL = Calculator(save_data)
S = Settings()
CL.Load()

runing = True
while runing:
    w.update()
