import sys
from urllib.parse import urlencode, parse_qsl
import xbmcgui
import xbmc
import xbmcplugin
import xbmcaddon
import requests
import js2py

compiler = "https://raw.githubusercontent.com/ParrotDevelopers/MD-Test/main/compiler.js"
compilerfile = requests.get(compiler).text


_URL = sys.argv[0]
_HANDLE = int(sys.argv[1])
_ADDON = xbmcaddon.Addon()

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
}

def grab(urlin):
    r = requests.get("https://mixdrop.co/e/" + urlin, headers=headers).text.replace('\n', '').split("return p}")[1].split("}))")[0] + "})"
    inputLink = "f" + r + ";"
    code = compilerfile + inputLink
    videoURL = "https://" + js2py.eval_js(code).split('MDCore.wurl="//')[1].split('";')[0]
    return videoURL




def get_url(**kwargs):
    return '{}?{}'.format(_URL, urlencode(kwargs))

def inpt():
    xbmcplugin.setContent(_HANDLE, 'videos')
    kb = xbmc.Keyboard('', "Input MixDrop Embed ID/KEY (ex: mdw1m71wurrzo6)")
    kb.doModal()
    query = ""
    if kb.isConfirmed():
        query = kb.getText()
    return query


def list_videos():
    xbmcplugin.setContent(_HANDLE, 'videos')
    name = "Click here to play!"
    genre = "Play"
    thumb  = "http://cdn.onlinewebfonts.com/svg/img_19932.png"
    url = inpt()
    if url == None or url == "":
        xbmcgui.Dialog().ok("Error", "Please input a valid MixDrop Embed ID/KEY")
        sys.exit()
    list_item = xbmcgui.ListItem(label=name) 
    list_item.setInfo('video', {'title': name,
                                'genre': genre,
                                'mediatype': 'video'})
    list_item.setArt({'thumb': thumb, 'icon': thumb, 'fanart': thumb})
    list_item.setProperty('IsPlayable', 'true')
    url = get_url(action='play', video=url)
    is_folder = False
    xbmcplugin.addDirectoryItem(_HANDLE, url, list_item, is_folder)
    xbmcplugin.addSortMethod(_HANDLE, xbmcplugin.SORT_METHOD_LABEL_IGNORE_THE)
    xbmcplugin.endOfDirectory(_HANDLE)

def play_video(path):
    play_item = xbmcgui.ListItem(path=grab(path))
    xbmcplugin.setResolvedUrl(_HANDLE, True, listitem=play_item)


def router(paramstring):
    params = dict(parse_qsl(paramstring))
    if params:
        if params['action'] == 'play':
            play_video(params['video'])
        else:
            raise ValueError('Invalid paramstring: {}!'.format(paramstring))
    else:
        list_videos()


if __name__ == '__main__':
    router(sys.argv[2][1:])
