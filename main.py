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
from datetime import datetime

# Initalised speedtest.net
s = speedtest.Speedtest()

# Sends a Push-Notification while the Speedtest is Preparing
notifiyerRunning =    Notification(
	        title='Speedtest Running',
	        description='Please wait while the Speedtest is running',
	        icon_path='.local/share/ulauncher/extensions/speedtest.test/images/icon.png',
            duration=20,
            urgency='normal'
		).send()



# Does Speedtest and stores the result into upList for Upload, downList for Download and pingList for Ping
upList = [0];
upList = round((round(s.upload()) / 1048576), 2)
downList = [0]
downList = round((round(s.download()) / 1048576), 2)
pingList = [0]
pingList = round(s.results.ping)



# Sends a Notification with the Speedtest result
notifiyer =    Notification(
	        title='Speedtest Results',
	        description='Download: ' + str(downList) + " mbps" + ", Upload: " + str(upList) + " mbps, " + 'Ping: ' + str(pingList) + ' ms',
	        icon_path='images/icon.png',
            duration=30,
            urgency='normal'
		).send()

notifyOnEnter = notifiyerRunning, notifiyer


class Extension(Extension):

    def __init__(self):
        super(DemoExtension, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())


class KeywordQueryEventListener(EventListener):

    def on_event(self, event, extension):
        items = []

        items.append(ExtensionResultItem(icon='images/icon.png',
                                         name='Speedtest',
                                         description='Download: ' + str(downList) + " mbps" + ", Upload: " + str(upList) + " mbps, " + 'Ping: ' + str(pingList) + ' ms',
                                         on_enter=HideWindowAction()))



        return RenderResultListAction(items)

if __name__ == '__main__':
    DemoExtension().run()
