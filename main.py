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

s = speedtest.Speedtest()

supload = s.upload()
sdownload = s.download()

notifiyer =    Notification(
	        title='Speedtest Results',
	        description='Download: ' + str(sdownload) + ' Upload: ' + str(supload),
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
                                         description='Item description',
                                         on_enter=notifiyer, keep_app_open=False))

        return RenderResultListAction(items)

if __name__ == '__main__':
    DemoExtension().run()
