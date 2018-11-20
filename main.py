#from pathlib import Path
#import kivy

import time
from kivy.app import App
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.uix.filechooser import FileChooser
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.event import EventDispatcher
import os
# from pathlib import Path
#layouts
#import Factory kivy.factory.Factory
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.pagelayout import PageLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import OptionProperty, NumericProperty, ListProperty, StringProperty
from kivy.uix.video import Video
from kivy.uix.videoplayer import VideoPlayer

Builder.load_string('''
<Player>:
    text: 'Play' 
    BoxLayout:
        cols: 3
        height: 24 * 5
        Button:
            size_hint:(None,0.1)
            text: "Choose File"
            on_release: root.manager.current = 's2'
        Button:
            size_hint:(None,0.1)
            text: "play"
            on_release: root.playx()
        VideoPlayer:
            id:Playerx
            source: '/home/lubeck/Videos/muestra.avi'
            status: 'stop'         
<Filesx>:
    id: filechooser
    GridLayout:
        cols:1
        id :cajita
        FileChooserListView:
            id: filechooser
            on_selection: root.selected()
        Button:
            size_hint:(None, 0.1)
            text: "OK" 
            on_release: root.manager.current='s1'     
    '''
)
'''
 Slider:
                min: 0.
                max: 1.
'''
#on_selection: root.selected(filechooser.selection)
class Player(Screen):
    fuente = 'nada'#str(App.get_running_app().saver.getx())
    def playx(self):
        lol = App.get_running_app().saver.getx()
        fuente = lol
        print ('se procede a reproducir ... ')
        print (str(self.ids.Playerx.source))
        self.ids.Playerx.source = (fuente[2:-2]) #VideoPlayer(source=fuente)
        #print (fuente[2:-1] + "-:v")
        #self.ids.Playerx.source = '/home/lubeck/Videos/muestra2.avi'
        print (str(self.ids.Playerx.source))
        pass
    pass

class Saver(EventDispatcher):
    fullpath = StringProperty("alv perro :V")
    #defaultPath = os.path.expanduser('~')+'/Videos'
    def setx(self, name):
        self.fullpath = name
        pass
    def getx(self):
        return self.fullpath
    pass

class Filesx(Screen):
    def selected(self):
        #app = App.get_running_app()
        self.fullpath = self.ids.filechooser.selection
        print (self.fullpath)
        App.get_running_app().saver.setx(str(self.fullpath))
        print (App.get_running_app().saver.fullpath)
        #App.get_running_app().Player.ids.Playerx.source = self.fullpath
        #print (App.get_running_app().Player.ids.Playerx.source)
        return str(self.fullpath)
    pass

class controller(Player,Filesx):
    def __init__(self):
        super(controller, self).__init__()

        self.defaultPath = os.path.expanduser('~')+'/Videos'
        self.mainScreen = Player(name='s1')
        #print ("ttrt"+ self.mainScreen.ids.Playerx.source+"trtr")
        #app = App.get_running_app().saver.fullpath
        #print (app)
        #self.mainScreen.ids.Playerx.source = "teeee"
        print ("ttrt  "+ self.mainScreen.ids.Playerx.source+"  trtr")
        self.fileScreen = Filesx(name='s2')
        self.fileScreen.ids.filechooser.path = self.defaultPath
        pass

    def selected(self):
        print ("halla ctm")
        #text = Filesx.selected(self)
        text = super(controller, self).selected() + "45"
        print (text)
        pass
    pass

control = controller()
sm = ScreenManager()
#sm.add_widget(Player(name = 's1'))
#sm.add_widget(Filesx(name='s2'))
sm.add_widget(control.mainScreen)
#control.mainScreen.ids.Player.source = Saver.fullpath.get()
sm.add_widget(control.fileScreen)

class TestApp(App):
    saver = Saver()
    def build(self):
        return sm#Player()
            #return  Button(text= 'reconchatumadre')
TestApp().run()