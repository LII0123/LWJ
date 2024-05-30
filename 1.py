# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc


###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"李文杰", pos=wx.DefaultPosition, size=wx.Size(500, 300),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        self.m_menubar1 = wx.MenuBar(0)
        self.m_menu1 = wx.Menu()
        self.m_menuItem1 = wx.MenuItem(self.m_menu1, wx.ID_ANY, u"退出", wx.EmptyString, wx.ITEM_NORMAL)
        self.m_menu1.AppendItem(self.m_menuItem1)

        self.m_menubar1.Append(self.m_menu1, u"选项")

        self.SetMenuBar(self.m_menubar1)

        self.Centre(wx.BOTH)

        # Connect Events
        self.Bind(wx.EVT_MENU, self.m_menuItem1OnMenuSelection, id=self.m_menuItem1.GetId())

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def m_menuItem1OnMenuSelection(self, event):
        event.Skip()



app = wx.App(False)

# 创建一个MyFrame1的实例，并将None作为parent（因为此时没有父窗口）
frame = MyFrame1(None)

# 显示窗口
frame.Show(True)

# 进入主事件循环
app.MainLoop()