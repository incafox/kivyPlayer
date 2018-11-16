#import kivy
import time
from kivy.app import App
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.uix.filechooser import FileChooser
from kivy.uix.tabbedpanel import TabbedPanel
#layouts

from kivy.uix.floatlayout import FloatLayout
from kivy.uix.pagelayout import PageLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout

from kivy.properties import OptionProperty, NumericProperty, ListProperty, \
        BooleanProperty
from kivy.uix.video import Video
from kivy.uix.videoplayer import VideoPlayer

Builder.load_string('''
<Player>:
    do_default_tab: False
    TabbedPanelItem:
        text: 'Play'
        StackLayout:
            canvas:
                Color:
                    rgb: (0.05, 0.41, 0.51)
                Rectangle:
                    
                    size: self.width - 200, self.height - 200
                    pos: self.x + 10 , self.y+150 
            StackLayout:
                cols: 3
                size_hint: 1, None
                height: 24 * 5
                    
                StackLayout:
                    rows : 3
                    VideoPlayer:
                        status: 'stop'
                        size_hint: (None, 4.5)
                    Slider:
                        min: 0.
                        max: 1.
    TabbedPanelItem:
        text: 'Search'
        BoxLayout:
            FileChooserListView:
                id: filechooser
            BoxLayout:
                size_hint_y: None
                height: 30
            Button:
                text: "Cancel"                    
    '''
)

class Player(TabbedPanel):
    pass

class TestApp(App):
    def build(self):
        return Player()
            #return  Button(text= 'reconchatumadre')

TestApp().run()