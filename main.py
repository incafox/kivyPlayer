#from pathlib import Path
#import kivy
import time
from kivy.app import App
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.uix.filechooser import FileChooser
from kivy.uix.tabbedpanel import TabbedPanel

import os
# from pathlib import Path
#layouts
#import Factory kivy.factory.Factory
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.pagelayout import PageLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import OptionProperty, NumericProperty, ListProperty, \
        BooleanProperty
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
        VideoPlayer:
            id:Player
            status: 'stop'
            size_hint: (None, 4.5)         
<Filesx>:
    id: filechooser
    GridLayout:
        cols:1
        id :cajita
        FileChooserListView:
            id: filechooser
            path: "$HOME/"
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

class Player(Screen):
    pass

class Filesx(Screen):
    pass

class controller():
    def __init__(self):
        self.defaultPath = os.path.expanduser('~')
        self.mainScreen = Player(name='s1')
        self.fileScreen = Filesx(name='s2')
        self.fileScreen.ids.filechooser.path = self.defaultPath
        pass
    pass

control = controller()
sm = ScreenManager()
#sm.add_widget(Player(name = 's1'))
#sm.add_widget(Filesx(name='s2'))
sm.add_widget(control.mainScreen)
sm.add_widget(control.fileScreen)

class TestApp(App):
    def build(self):
        return sm#Player()
            #return  Button(text= 'reconchatumadre')

TestApp().run()