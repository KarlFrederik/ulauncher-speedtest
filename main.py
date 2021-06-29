# ulauncher-speedtest
# https://github.com/KarlFrederik/ulauncher-speedtest
# by Karl_F

from ulauncher.api.client.Extension import Extension
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent, ItemEnterEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.HideWindowAction import HideWindowAction
from pynotifier import Notification
import speedtest
import time
import math

# Initalised speedtest.net
s = speedtest.Speedtest()


# Does Speedtest and stores the result into aList for Upload or bList for Download
aList = [0];
aList = round((round(s.upload()) / 1048576), 2)
bList = [0]
bList = round((round(s.download()) / 1048576), 2)



# Sends a Notification with the Speedtest result
notifiyer =    Notification(
	        title='Speedtest Results',
	        description='Upload: ' + str(aList) + " Download: " + str(bList),
	        icon_path='images/icon.png',
            duration=15,
            urgency='normal'
		).send()



class DemoExtension(Extension):

    def __init__(self):
        super(DemoExtension, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())


class KeywordQueryEventListener(EventListener):

    def on_event(self, event, extension):
        items = []

        items.append(ExtensionResultItem(icon='images/icon.png',
                                         name='Speedtest',
                                         description="Download: " + bList + ", Upload: " + alist,
                                         on_enter=HideWindowAction()))

        return RenderResultListAction(items)

if __name__ == '__main__':
    DemoExtension().run()
