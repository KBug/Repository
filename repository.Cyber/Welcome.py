# -*- coding: utf-8 -*-


import time
import xbmc, xbmcaddon, xbmcgui
import json
import traceback

try:
    from urllib import urlopen
except ImportError:
    from urllib.request import urlopen

INTERVAL =  24 * 60 * 60 
ANNOUNCEMENTS = 'https://raw.githubusercontent.com/ParrotDevelopers/Repository/Addons/Welcome/Welcome.json'
LAST = 'last_ann'

if __name__ == '__main__':
    monitor = xbmc.Monitor()
    
    while not monitor.abortRequested():
        try:
            response = urlopen(ANNOUNCEMENTS)
            data = json.loads(response.read())
            data = sorted(data.items())
            addon = xbmcaddon.Addon()
            last_ann = addon.getSetting(LAST)
            last_ann = 0 if not last_ann else int(last_ann)
            for ann in data:
                ikey = int(ann[0])
                print(str(ikey))
                print(str(last_ann))
                if ikey > last_ann:
                    last_ann = ikey
                    xbmcgui.Dialog().textviewer(addon.getAddonInfo('name'), ann[1])
            addon.setSetting(LAST,str(last_ann))
        except:
            traceback.print_exc()

        if monitor.waitForAbort(INTERVAL):
            break
