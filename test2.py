import wx

window = wx.App()


class s_report(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, -1, "Grade It!", size=(500, 700))

        self.panel = wx.Panel(self, -1)

        menu = wx.MenuBar()

        file_menu = wx.Menu()
        file_menu.Append(301, "Quit")
        self.Bind(wx.EVT_MENU, self.Quit, id=301)

        help_menu = wx.Menu()
        help_menu.Append(302, "About")
        self.Bind(wx.EVT_MENU, self.about, id=302)

        menu.Append(file_menu, "File")
        menu.Append(help_menu, "Help")

        self.SetMenuBar(menu)

        wx.StaticText(self.panel, -1,
                      "Welcome to Grade It!.\nPlease enter your exam marks for 12 subjects. Your highest\nscoring and lowest scoring subject, along with your percentage and grade will be displayed.",
                      pos=(10, 10))
        wx.StaticText(self.panel, -1, "Please enter the marks of 12 subjects:", pos=(10, 70))

        wx.StaticText(self.panel, -1, "English Language:", pos=(10, 100))
        wx.StaticText(self.panel, -1, "English Literature:", pos=(10, 125))
        wx.StaticText(self.panel, -1, "Mathematics:", pos=(10, 150))
        wx.StaticText(self.panel, -1, "Language II", pos=(10, 175))
        wx.StaticText(self.panel, -1, "Physics:", pos=(10, 200))
        wx.StaticText(self.panel, -1, "Chemistry:", pos=(10, 225))
        wx.StaticText(self.panel, -1, "Biology:", pos=(10, 250))
        wx.StaticText(self.panel, -1, "History/Civics:", pos=(10, 275))
        wx.StaticText(self.panel, -1, "Geography:", pos=(10, 300))
        wx.StaticText(self.panel, -1, "Environmental Education", pos=(10, 325))
        wx.StaticText(self.panel, -1, "Computer Science", pos=(10, 350))
        wx.StaticText(self.panel, -1, "Computer Practicals", pos=(10, 375))

        self.one = wx.TextCtrl(self.panel, -1, pos=(150, 100), size=(40, 20))
        self.two = wx.TextCtrl(self.panel, -1, pos=(150, 125), size=(40, 20))
        self.three = wx.TextCtrl(self.panel, -1, pos=(150, 150), size=(40, 20))
        self.four = wx.TextCtrl(self.panel, -1, pos=(150, 175), size=(40, 20))
        self.five = wx.TextCtrl(self.panel, -1, pos=(150, 200), size=(40, 20))
        self.six = wx.TextCtrl(self.panel, -1, pos=(150, 225), size=(40, 20))
        self.seven = wx.TextCtrl(self.panel, -1, pos=(150, 250), size=(40, 20))
        self.eight = wx.TextCtrl(self.panel, -1, pos=(150, 275), size=(40, 20))
        self.nine = wx.TextCtrl(self.panel, -1, pos=(150, 300), size=(40, 20))
        self.ten = wx.TextCtrl(self.panel, -1, pos=(150, 325), size=(40, 20))
        self.eleven = wx.TextCtrl(self.panel, -1, pos=(150, 350), size=(40, 20))
        self.twelve = wx.TextCtrl(self.panel, -1, pos=(150, 375), size=(40, 20))

        wx.Button(self.panel, 201, "Done", pos=(130, 400))
        self.Bind(wx.EVT_BUTTON, self.Done, id=201)

        self.Centre()
        self.Show()

    def Done(self, event):
        marks = []

        marks.append(int(self.one.GetValue()))
        marks.append(int(self.two.GetValue()))
        marks.append(int(self.three.GetValue()))
        marks.append(int(self.four.GetValue()))
        marks.append(int(self.five.GetValue()))
        marks.append(int(self.six.GetValue()))
        marks.append(int(self.seven.GetValue()))
        marks.append(int(self.eight.GetValue()))
        marks.append(int(self.nine.GetValue()))
        marks.append(int(self.ten.GetValue()))
        marks.append(int(self.eleven.GetValue()))
        marks.append(int(self.twelve.GetValue()))
        sum = 0
        for num in marks:
            sum = sum + num

        wx.StaticText(self.panel, -1, "Average: ", pos=(10, 425))
        wx.StaticText(self.panel, -1, str(sum / len(marks)), pos=(200, 425))

    def Quit(self, event):
        self.Close()

    def about(self, event):
        self.about = wx.AboutDialogInfo()

        self.about.SetName("Grade It!")
        self.about.SetCopyright("(c) 2009 Sravan")
        self.about.SetWebSite("http://www.uberpix.wordpress.com")
        self.about.AddDeveloper("Sravan")

        wx.AboutBox(self.about)


s_report()
window.MainLoop()