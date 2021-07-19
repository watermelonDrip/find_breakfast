import wx
import random
 
window = wx.App()
class s_report(wx.Frame):
    def __init__(self):
        self.food = {'0':'粉面类','1':'饺子','2':'米饭','3':'粥','4':'饼','5':'面包','6':'杂粮'}
        self.method = {'0':'水煮（清汤）','1':'水煮（火锅汤底）','2':'水煮（呛汤）','3':'水煮（酸汤）','4':'水煮（菌汤）','5':'清蒸','6':'油煎','7':'油炸','8':'油焖','9':'炒','10':'干拌'}

        wx.Frame.__init__(self, None, -1, "Choose One!", size=(500, 700))
        self.panel = wx.Panel(self, -1)
        self.panel.Bind(wx.EVT_ERASE_BACKGROUND,self.OnEraseBack)

        #self.SetBackgroundColour('rgba(222, 211, 140, 1)')
       # wx.Colour == “rgba(255, 0, 0, 0.333)”)
      #  image_file = 'WechatIMG342.jpeg'
        #bmp1 = wx.Image(image_file, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        #self.bitmap1 = wx.StaticBitmap(self, -1, bmp1, (100, 100))
        # show some image details


        self.st0 = wx.StaticText(self.panel, -1,
                      "Welcome to my Home!.\n\nPlease enter your decision for Dr.Zhao and the wife's breakfast. ",
                      pos=(30+10, 150))
       # self.st0.SetFont(wx.Font(15, wx.ROMAN, wx.NORMAL, wx.NORMAL))

        wx.StaticText(self.panel, -1, "Please choose one food:", pos=(10+40, 220))
        wx.StaticText(self.panel, -1, "Please choose one method:", pos=(200+40, 220))

        distance = 0
        tmp_food = self.food
        tmp_method = self.method

        for i in range(len(self.food)):
            wx.StaticText(self.panel, -1, str(i+1) +"."+  tmp_food[str(i)], pos=(10+40, 150+100+25*i))
        for j in range(len(self.method)):
            wx.StaticText(self.panel, -1, str(j+1) +"."+  tmp_method[str(j)], pos=(200+40, 150+100+25*j))



        wx.Button(self.panel, 201, "选一个吧，小婊砸", pos=(110 , 380+150))
        self.Bind(wx.EVT_BUTTON, self.Done, id=201)

        self.Centre()
        self.Show()

    def OnEraseBack(self, event):
        dc = event.GetDC()
        if not dc:
            dc = wx.ClientDC(self)
            rect = self.GetUpdateRegion().GetBox()
            dc.SetClippingRect(rect)
        dc.Clear()
        # get the bitmap from somewhere

        # rescale it to have size of 32*32


        bmp = wx.Bitmap("WechatIMG342.jpeg")
        image = bmp.ConvertToImage()

        w = bmp.GetWidth()
        h = bmp.GetHeight()

        bmp = wx.Bitmap(image.Scale(w/5, h/5))
        image.Rescale(32, 32)

        dc.DrawBitmap(bmp, 0, 0)
        #image_file = 'WechatIMG342.jpeg'


    def Done(self, event):


        value_food = random.randint(0,len(self.food)-1)
        value_method = random.randint(0,len(self.method)-1)

        tmp_food = self.food
        tmp_method = self.method


        i = 0

        #self.st1 = wx.StaticText(self.panel, -1, tmp_food[str(value_food)] + tmp_method[str(value_method)] , pos=(100, 425+i))
        self.st1 = wx.StaticText(self.panel, -1,
                     "food is:"+tmp_food[str(value_food)]+"\n method is:"+ tmp_method[str(value_method)],
                     pos=(90, 380+150+30))
        self.st2 = wx.StaticText(self.panel, -1, "the final dish is: "+ tmp_method[str(value_method)] +'+'+ tmp_food[str(value_food)], pos=(70, 380+150+50+30))
        #self.st2.SetBackgroundColour('blue')
        self.st2.SetFont(wx.Font(20, wx.SWISS, wx.NORMAL, wx.NORMAL))


        self.btn = wx.Button(self.panel, id=1, label="不满意，垃圾（只能点一下）", pos=(260, 380+150))
        self.btn.Bind(wx.EVT_BUTTON, self.Onclick)

        #wx.StaticText(self.panel, -1, str(value), pos=(200, 425))

    def Onclick(self, event):
        # destroy static text
        self.st1.Destroy()
        self.st2.Destroy()

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

