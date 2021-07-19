import wx
import random
#/Users/luoman/PycharmProjects/find_breakfast/my_breakfast.py

window = wx.App()
class s_report(wx.Frame):
    def __init__(self):
        self.dist_list = {'1':'西红柿炒鸡蛋','2':'方便面','3':'拌面','4':'火锅面','5':'印度饼+小肠','6':'饺子','7':'大米粥+煎蛋+小肠'}

        wx.Frame.__init__(self, None, -1, "Choose One!", size=(500, 700))

        self.panel = wx.Panel(self, -1)




        wx.StaticText(self.panel, -1,
                      "Welcome to my Home!.\nPlease enter your decision for Dr.Zhao and the wife's breakfast. ",
                      pos=(10, 10))
        wx.StaticText(self.panel, -1, "Please choose one dish:", pos=(10, 70))

        wx.StaticText(self.panel, -1, "1.西红柿炒鸡蛋", pos=(10, 100))
        wx.StaticText(self.panel, -1, "2.方便面", pos=(10, 125))
        wx.StaticText(self.panel, -1, "3.拌面", pos=(10, 150))
        wx.StaticText(self.panel, -1, "4:火锅面", pos=(10, 175))
        wx.StaticText(self.panel, -1, "5:印度饼+小肠", pos=(10, 200))
        wx.StaticText(self.panel, -1, "6：饺子", pos=(10, 225))
        wx.StaticText(self.panel, -1, "7:大米粥+煎蛋+小肠", pos=(10, 250))
        #wx.StaticText(self.panel, -1, "History/Civics:", pos=(10, 275))
       # wx.StaticText(self.panel, -1, "Geography:", pos=(10, 300))
       # wx.StaticText(self.panel, -1, "Environmental Education", pos=(10, 325))
       # wx.StaticText(self.panel, -1, "Computer Science", pos=(10, 350))
       # wx.StaticText(self.panel, -1, "Computer Practicals", pos=(10, 375))

       # self.one = wx.TextCtrl(self.panel, -1, pos=(150, 100), size=(200, 20))
       # self.two = wx.TextCtrl(self.panel, -1, pos=(150, 125), size=(200, 20))
       # self.three = wx.TextCtrl(self.panel, -1, pos=(150, 150), size=(40, 20))
       # self.four = wx.TextCtrl(self.panel, -1, pos=(150, 175), size=(40, 20))
       # self.five = wx.TextCtrl(self.panel, -1, pos=(150, 200), size=(40, 20))
       # self.six = wx.TextCtrl(self.panel, -1, pos=(150, 225), size=(40, 20))
       # self.seven = wx.TextCtrl(self.panel, -1, pos=(150, 250), size=(40, 20))
       # self.eight = wx.TextCtrl(self.panel, -1, pos=(150, 275), size=(40, 20))
       # self.nine = wx.TextCtrl(self.panel, -1, pos=(150, 300), size=(40, 20))
       # self.ten = wx.TextCtrl(self.panel, -1, pos=(150, 325), size=(40, 20))
       # self.eleven = wx.TextCtrl(self.panel, -1, pos=(150, 350), size=(40, 20))
       # self.twelve = wx.TextCtrl(self.panel, -1, pos=(150, 375), size=(40, 20))

        wx.Button(self.panel, 201, "选一个吧，小婊砸", pos=(150, 400))
        self.Bind(wx.EVT_BUTTON, self.Done, id=201)

        self.Centre()
        self.Show()



    def Done(self, event):
        #marks = []

       # marks.append(str(self.one.GetValue()))
       # marks.append(str(self.two.GetValue()))
        #marks.append(int(self.three.GetValue()))
       # marks.append(int(self.four.GetValue()))
        #marks.append(int(self.five.GetValue()))
      #  marks.append(int(self.six.GetValue()))
       # marks.append(int(self.seven.GetValue()))
      #  marks.append(int(self.eight.GetValue()))
      #  marks.append(int(self.nine.GetValue()))
       # marks.append(int(self.ten.GetValue()))
        #marks.append(int(self.eleven.GetValue()))
        #marks.append(int(self.twelve.GetValue()))
       # sum = 0


        value = random.randint(1,len(self.dist_list))


        tmp = self.dist_list


        i = 0
        wx.StaticText(self.panel, -1, "the final dish is: ", pos=(10, 425))

        self.st = wx.StaticText(self.panel, -1, tmp[str(value)], pos=(200, 425+i))
        self.btn = wx.Button(self.panel, id = 1, label ="不满意，垃圾（只能点一下）",  pos=(300, 400))
        self.btn.Bind(wx.EVT_BUTTON, self.Onclick)

        #wx.StaticText(self.panel, -1, str(value), pos=(200, 425))

    def Onclick(self, event):
        # destroy static text
        self.st.Destroy()

    def Quit(self, event):
        self.Close()

    def about(self, event):
        self.about = wx.AboutDialogInfo()

        self.about.SetName("FIND It!")
       # self.about.SetCopyright("(c) 2009 Sravan")
        #self.about.SetWebSite("http://www.uberpix.wordpress.com")
       # self.about.AddDeveloper("Sravan")

        wx.AboutBox(self.about)


#s_report()
#window.MainLoop()
if __name__ == '__main__':
    app = s_report()


    # frame = MyNewFrame(None)
   # frame.Show(True)
    window.MainLoop()

