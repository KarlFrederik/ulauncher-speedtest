# ulauncher-speedtest
# https://github.com/KarlFrederik/ulauncher-speedtest
# by KarlFrederik under the WTFPL license (http://www.wtfpl.net/about)

from ulauncher.api.client.Extension import Extension
import gi
gi.require_version('Gtk', '3.0')
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.HideWindowAction import HideWindowAction
import speedtest

servers = []
threads = None
# Initalised speedtest.net
s = speedtest.Speedtest()
s.get_servers(servers)
s.get_best_server()

class DemoExtension(Extension):

    def __init__(self):
        super(DemoExtension, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())

class KeywordQueryEventListener(EventListener):

    def on_event(self, event, extension):
        items = []

        download = round((round(s.download(threads=threads)) / 1048576), 2)
        upload = round((round(s.upload(threads=threads)) / 1048576), 2)
        ping = round(s.results.ping)

        items.append(ExtensionResultItem(
            icon='images/icon.png',
            name='Speedtest',
            description=f'Ping {ping} ms | Download: {download} mbps | Upload: {upload} mbps',
            on_enter=HideWindowAction())
        )

        return RenderResultListAction(items)

if __name__ == '__main__':
    DemoExtension().run()
