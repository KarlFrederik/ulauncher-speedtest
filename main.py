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
	        description=supload,
	        icon_path='images/icon.png',
            duration=10,
            urgency='normal'
		).send()



class DemoExtension(Extension):

    def __init__(self):
        super(DemoExtension, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())


class KeywordQueryEventListener(EventListener):

    def on_event(self, event, extension):
        items = []
        for i in range(5):
            items.append(ExtensionResultItem(icon='images/icon.png',
                                             name='Item %s' % i,
                                             description='Item description %s' % i,
                                             on_enter=notifiyer))

        return RenderResultListAction(items)

if __name__ == '__main__':
    DemoExtension().run()
