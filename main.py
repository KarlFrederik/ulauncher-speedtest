# ulauncher-speedtest
# https://github.com/KarlFrederik/ulauncher-speedtest
# by karl_f under the WTFPL license (http://www.wtfpl.net/about)

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


class DemoExtension(Extension):

    def __init__(self):
        super(DemoExtension, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())


class KeywordQueryEventListener(EventListener):

    def on_event(self, event, extension):
        items = []

        items.append(ExtensionResultItem(icon='images/icon.png',
                                         name='Speedtest',
                                         description='Download: ' + str(round((round(s.download()) / 1048576), 2)) + " mbps" + ", Upload: " + str(round((round(s.upload()) / 1048576), 2)) + " mbps, " + 'Ping: ' + str(round(s.results.ping)) + ' ms',
                                         on_enter=HideWindowAction()))



        return RenderResultListAction(items)

if __name__ == '__main__':
    DemoExtension().run()
