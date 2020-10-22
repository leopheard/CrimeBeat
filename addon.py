from xbmcswift2 import Plugin, xbmcgui
from resources.lib import mainaddon

plugin = Plugin()
url1 = "https://www.omnycontent.com/d/playlist/fdc2ad13-d199-4e97-b2db-a59300cb6cc2/45a0e162-b88a-43bc-8c19-a9eb0140c1d3/cb6a559a-e724-47a5-8346-a9eb0142740e/podcast.rss"
@plugin.route('/')
def main_menu():
    items = [
        {
            'label': plugin.get_string(30001),
            'path': plugin.url_for('episodes1'),
            'thumbnail': "https://www.omnycontent.com/d/programs/fdc2ad13-d199-4e97-b2db-a59300cb6cc2/45a0e162-b88a-43bc-8c19-a9eb0140c1d3/image.jpg?t=1601912880&size=Large"},
        {
            'label': plugin.get_string(30000),
            'path': plugin.url_for('episodes'),
            'thumbnail': "https://www.omnycontent.com/d/programs/fdc2ad13-d199-4e97-b2db-a59300cb6cc2/45a0e162-b88a-43bc-8c19-a9eb0140c1d3/image.jpg?t=1601912880&size=Large"},
    ]
    return items

@plugin.route('/episodes1/')
def episodes1():
    soup1 = mainaddon.get_soup1(url1)
    playable_podcast1 = mainaddon.get_playable_podcast1(soup1)
    items = mainaddon.compile_playable_podcast1(playable_podcast1)
    return items

@plugin.route('/episodes/')
def episodes():
    soup1 = mainaddon.get_soup1(url1)
    playable_podcast = mainaddon.get_playable_podcast(soup1)
    items = mainaddon.compile_playable_podcast(playable_podcast)
    return items

if __name__ == '__main__':
    plugin.run()
