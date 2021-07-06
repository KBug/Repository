
import sys
from urllib.parse import urlencode, parse_qsl
import xbmcgui
import xbmcplugin

# Get the plugin url in plugin:// notation.
_url = sys.argv[0]
# Get the plugin handle as an integer number.
_handle = int(sys.argv[1])

# Free sample videos are provided by www.vidsplay.com
# Here we use a fixed set of properties simply for demonstrating purposes
# In a "real life" plugin you will need to get info and links to video files/streams
# from some web-site or online service.
VIDEOS = {'1. SK Channels': [{'name': '1. SK Channels',
                       'thumb': 'https://i.ibb.co/2cH2kVB/SK.jpg',
                       'video': 'https://i.ibb.co/2cH2kVB/SK.jpg',
                       'genre': 'SK Channels'},
                      {'name': '2. JoJ',
                       'thumb': 'https://i.ibb.co/SccZK6g/JOJ.png',
                       'video': 'http://nn2.joj.sk/hls/joj-720.m3u8',
                       'genre': 'SK Channels'},
                      {'name': '3. JoJ Plus',
                       'thumb': 'https://i.ibb.co/G5VWSNM/Plus.png',
                       'video': 'http://nn2.joj.sk/hls/jojplus-540.m3u8',
                       'genre': 'SK Channels'},
                      {'name': '4. JoJ Family',
                       'thumb': 'https://i.ibb.co/MNRvsnZ/JOJ-Family.jpg',
                       'video': 'http://nn.geo.joj.sk/hls/family-360.m3u8',
                       'genre': 'SK Channels'},
                      {'name': '5. Wau',
                       'thumb': 'https://i.ibb.co/kmDHqy3/WAU.png',
                       'video': 'https://nn.geo.joj.sk/live/wau-index.m3u8',
                       'genre': 'SK Channels'},
                      {'name': '6. TA3',
                       'thumb': 'https://i.ibb.co/vcSFT8C/TA3.png',
                       'video': 'https://tv.parrottv.tk/TA3.m3u8',
                       'genre': 'SK Channels'},
                      {'name': '7. Fashion TV',
                       'thumb': 'https://i.ibb.co/XzBpYkL/Fashion-TV.png',
                       'video': 'http://lb.streaming.sk/fashiontv/stream/playlist.m3u8?fluxustv.m3u8',
                       'genre': 'SK Channels'},
                      {'name': '8. Rik',
                       'thumb': 'https://i.ibb.co/WPy9w4n/Rik.png',
                       'video': 'https://nn.geo.joj.sk/live/hls/rik-540.m3u8',
                       'genre': 'SK Channels'},
                      {'name': '9. TV Lux',
                       'thumb': 'https://i.ibb.co/4jx6gzZ/TV-Lux.png',
                       'video': 'http://live.tvlux.sk:1935/lux/lux.stream_360p/chunklist_w1295439472.m3u8',
                       'genre': 'SK Channels'},
                      {'name': '10. Life TV HD',
                       'thumb': 'https://i.ibb.co/3YktrSX/Life-TV.png',
                       'video': 'https://lifetv.mpks.sk/s.m3u8',
                       'genre': 'SK Channels'},
                      {'name': '11. Senzi TV',
                       'thumb': 'https://i.ibb.co/fnMky9c/Senzi.png',
                       'video': 'http://109.74.144.130/live/senzitest/playlist.m3u8',
                       'genre': 'SK Channels'},
                      {'name': '12. Televizia OSEM',
                       'thumb': 'https://i.ibb.co/wRG1nkt/TV-OSEM.png',
                       'video': 'http://109.74.145.11:1935/tv8/ngrp:tv8.stream_all/playlist.m3u8',
                       'genre': 'SK Channels'},
                      {'name': '13. TV Raj',
                       'thumb': 'https://i.ibb.co/J3TT3bZ/TV-Raj.png',
                       'video': 'http://ottst05.flexitv.sk/2827-tv-pc.m3u8',
                       'genre': 'SK Channels'},
                      {'name': '14. Bardejovská TV',
                       'thumb': 'https://i.ibb.co/CVrPbfy/BTV.jpg',
                       'video': 'rtmp://s1.media-planet.sk:80/live/bardejov1?checkedby:hlscat.com',
                       'genre': 'SK Channels'},
                      {'name': '15. KoŠice:Dnes',
                       'thumb': 'https://i.ibb.co/phBd44T/Kosice-Dnes.jpg',
                       'video': 'http://lb.streaming.sk/tvnasa/stream/playlist.m3u8?checkedby:hlscat.com',
                       'genre': 'SK Channels'},
                      {'name': '16. TV Nové Zámky',
                       'thumb': 'https://i.ibb.co/Y2XDLmH/NZTV.png',
                       'video': 'http://s1.media-planet.sk:80/live/novezamky/BratuMarian.m3u8?checkedby:hlscat.com',
                       'genre': 'SK Channels'},
                      {'name': '17. TV Reduta',
                       'thumb': 'https://i.ibb.co/S6snjM0/TVR.png',
                       'video': 'rtmp://s1.media-planet.sk:80/live/reduta?checkedby:hlscat.com',
                       'genre': 'SK Channels'},
                      {'name': '18. TV Ružinov',
                       'thumb': 'https://i.ibb.co/mzbMHpg/TVRU.png',
                       'video': 'http://lb.streaming.sk/tvruzinov/stream/playlist.m3u8?checkedby:hlscat.com',
                       'genre': 'SK Channels'},
                      {'name': '19. TV Turzovka',
                       'thumb': 'https://i.ibb.co/bmTMnr4/TVT.png',
                       'video': 'rtmp://s1.media-planet.sk:80/live/turzovka?checkedby:hlscat.com',
                       'genre': 'SK Channels'}
                      ],
            '2. CZ Channels': [{'name': '1. CZ Channels',
                      'thumb': 'https://i.ibb.co/mb6Q81H/CZ.jpg',
                      'video': 'https://i.ibb.co/mb6Q81H/CZ.jpg',
                      'genre': 'CZ Channels'},
                     {'name': '2. Nova',
                      'thumb': 'https://i.ibb.co/z4NMCjV/Nova.png',
                      'video': 'https://nova-live.ssl.cdn.cra.cz/channels/nova_avod/playlist/cze/live_hq.m3u8',
                      'genre': 'CZ Channels'},
                     {'name': '3. Nova 2',
                      'thumb': 'https://i.ibb.co/925Rmkq/Nova-2.png',
                      'video': 'https://nova-live.ssl.cdn.cra.cz/channels/nova_2_avod/playlist.m3u8',
                      'genre': 'CZ Channels'},
					 {'name': '4. Nova Gold',
                      'thumb': 'https://i.ibb.co/dpSZ22v/Nova-Gold.png',
                      'video': 'https://nova-live.ssl.cdn.cra.cz/channels/nova_gold_avod/playlist.m3u8',
                      'genre': 'CZ Channels'},
                     {'name': '5. Nova Action',
                      'thumb': 'https://i.ibb.co/99VYDCc/Nova-Action.jpg',
                      'video': 'https://nova-live.ssl.cdn.cra.cz/channels/nova_action_avod/playlist.m3u8',
                      'genre': 'CZ Channels'},
				     {'name': '6. Nova Cinema',
                      'thumb': 'https://i.ibb.co/rkL4pnC/Nova-Cinema.png"',
                      'video': 'https://nova-live.ssl.cdn.cra.cz/channels/nova_cinema_avod/playlist/cze/live_hq.m3u8',
                      'genre': 'CZ Channels'},
                     {'name': '7. Elektrika TV',
                      'thumb': 'https://i.ibb.co/sRVbxTv/Elektrika-TV.jpg',
                      'video': 'http://rtmp.elektrika.cz/live/myStream.sdp/playlist.m3u8',
                      'genre': 'CZ Channels'},
                     {'name': '8.Óčko',
                      'thumb': 'https://i.ibb.co/1fbv9Qq/Ocko.png',
                      'video': 'http://ocko-live.ssl.cdn.cra.cz/channels/ocko/playlist.m3u8',
                      'genre': 'CZ Channels'},
                     {'name': '9. Óčko Gold',
                      'thumb': 'https://i.ibb.co/g35N1VV/Ocko-Gold.gif',
                      'video': 'http://ocko-live.ssl.cdn.cra.cz/channels/ocko_gold/playlist/cze/live_hq.m3u8',
                      'genre': 'CZ Channels'},
				     {'name': '10.  Óčko Expres',
                      'thumb': 'https://i.ibb.co/q9pwKJC/Ocko-Expres.png',
                      'video': 'http://ocko-live.ssl.cdn.cra.cz/channels/ocko_expres/playlist/cze/live_hq.m3u8',
                      'genre': 'CZ Channels'},
                     {'name': '11. Óčko STAR',
                      'thumb': 'https://i.ibb.co/HX9M2pS/Ocko-Star.png',
                      'video': 'http://ocko-live.ssl.cdn.cra.cz/channels/ocko_gold/playlist/cze/live_hq.m3u8',
                      'genre': 'CZ Channels'},
                     {'name': '12. Polar TV',
                      'thumb': 'https://i.ibb.co/8sQ8yxh/Polar.png',
                      'video': 'https://stream.polar.cz/polar/polarlive-1/playlist.m3u8',
                      'genre': 'CZ Channels'},
                     {'name': '13. HunterTV',
                      'thumb': 'https://i.ibb.co/tzNHRp9/HunterTV.png',
                      'video': 'http://www.huntertv.cz/live/4-playlist.m3u8',
                      'genre': 'CZ Channels'},
				     {'name': '14. Praha TV',
                      'thumb': 'https://i.ibb.co/yqrcmvW/PrahaTV.png',
                      'video': 'https://stream.polar.cz/prahatv/prahatvlive-1/playlist.m3u8',
                      'genre': 'CZ Channels'},
                     {'name': '15. TV Noe',
                      'thumb': 'https://i.ibb.co/z7fQ7yJ/TV-Noe.png',
                      'video': 'https://w100.quickmedia.tv/prozeta-live04/_definst_/prozeta-live04.smil/Playlist.m3u8',
                      'genre': 'CZ Channels'},
                     {'name': '16. Retro',
                      'thumb': 'https://i.ibb.co/YPtmSrV/Retro.png',
                      'video': 'http://stream.mediawork.cz/retrotv/retrotvHQ1/playlist.m3u8',
                      'genre': 'CZ Channels'},
                     {'name': '17. Šlágr',
                      'thumb': 'https://i.ibb.co/Nx2fR74/Slagr.png',
                      'video': 'https://slagrtv-live-hls.ssl.cdn.cra.cz/channels/slagrtv/playlist/cze/live_hq.m3u8',
                      'genre': 'CZ Channels'},
                     {'name': '18. Šlágr 2',
                      'thumb': 'https://i.ibb.co/WxDvCry/Slagr2.png',
                      'video': 'http://92.62.234.233/slagr2.m3u',
                      'genre': 'CZ Channels'},
                     {'name': '19. TV Natura',
                      'thumb': 'https://i.ibb.co/K0HR49p/TV-Natura.png',
                      'video': 'http://media1.tvnatura.cz/live_out/1/live.m3u8',
                      'genre': 'CZ Channels'},
				     {'name': '20. Východočeská TV',
                      'thumb': 'https://i.ibb.co/ggWW1L0/VCTV.png',
                      'video': 'https://stream.polar.cz/vctv/vctvlive-1/playlist.m3u8',
                      'genre': 'CZ Channels'},
                     {'name': '21. TV Morava',
                      'thumb': 'https://i.ibb.co/LRfyxNG/TV-Morava.png',
                      'video': 'https://i.ibb.co/LRfyxNG/TV-Morava.png',
                      'genre': 'CZ Channels'}
                     ],
            '3. Movies': [{'name': '1. Movies',
                      'thumb': 'https://i.ibb.co/zbt3KHp/Movies.png',
                      'video': 'https://i.ibb.co/zbt3KHp/Movies.png',
                      'genre': 'Movies'},
                     {'name': '2. Spongebob ve Filmu: Houba Na Útěku [CZ Dabing] [2020]',
                      'thumb': 'https://i.ibb.co/LrZ2Rcn/Spongebob-Sponge-On-The-Run.jpg',
                      'video': 'https://files.fm/down.php?i=nhumjsc9j',
                      'genre': 'Movies'},
                     {'name': '3. Spongebob ve Filmu: Houba Na Suchu [CZ Dabing] [2015]',
                      'thumb': 'https://i.ibb.co/bzwL5b7/Spongebob-Sponge-Out-Of-Water.jpg',
                      'video': 'https://files.fm/down.php?i=etgfyb5uy',
                      'genre': 'Movies'},
                      {'name': '4. Spongebob ve Filmu  [CZ Dabing] [2004]',
                      'thumb': 'https://i.ibb.co/Sn2HkJc/Spongebob-Ve-Filmu-2004.jpg',
                      'video': 'https://files.fm/down.php?i=k8mpkg7kd',
                      'genre': 'Movies'},
                     {'name': '5. The Windermere Children [EN + CZ Tit] [2020]',
                      'thumb': 'https://i.ibb.co/zN1MPXj/The-Windermere-Children.jpg',
                      'video': 'https://files.fm/down.php?i=r6fpnuwrz',
                      'genre': 'Movies'}
                     ],
            '4. Check For Updates': [{'name': 'Check For Updates',
                      'thumb': 'https://github.com/ParrotDevelopers/Parrot-TV-Kodi/raw/main/Updates/Matrix/2.0.0/Main.jpg',
                      'video': 'https://github.com/ParrotDevelopers/Parrot-TV-Kodi/raw/main/Updates/Matrix/2.0.0/Main.jpg',
                      'genre': 'Updates'}
                     ]}


def get_url(**kwargs):
    return '{0}?{1}'.format(_url, urlencode(kwargs))


def get_categories():
    return VIDEOS.keys()


def get_videos(category):
    return VIDEOS[category]


def list_categories():
    # Set plugin category. It is displayed in some skins as the name
    # of the current section.
    xbmcplugin.setPluginCategory(_handle, 'My Video Collection')
    # Set plugin content. It allows Kodi to select appropriate views
    # for this type of content.
    xbmcplugin.setContent(_handle, 'videos')
    # Get video categories
    categories = get_categories()
    # Iterate through categories
    for category in categories:
        # Create a list item with a text label and a thumbnail image.
        list_item = xbmcgui.ListItem(label=category)
        # Set graphics (thumbnail, fanart, banner, poster, landscape etc.) for the list item.
        # Here we use the same image for all items for simplicity's sake.
        # In a real-life plugin you need to set each image accordingly.
        list_item.setArt({'thumb': VIDEOS[category][0]['thumb'],
                          'icon': VIDEOS[category][0]['thumb'],
                          'fanart': VIDEOS[category][0]['thumb']})
        # Set additional info for the list item.
        # Here we use a category name for both properties for for simplicity's sake.
        # setInfo allows to set various information for an item.
        # For available properties see the following link:
        # https://codedocs.xyz/xbmc/xbmc/group__python__xbmcgui__listitem.html#ga0b71166869bda87ad744942888fb5f14
        # 'mediatype' is needed for a skin to display info for this ListItem correctly.
        list_item.setInfo('video', {'title': category,
                                    'genre': category,
                                    'mediatype': 'video'})
        # Create a URL for a plugin recursive call.
        # Example: plugin://plugin.parrot.tv/?action=listing&category=Animals
        url = get_url(action='listing', category=category)
        # is_folder = True means that this item opens a sub-list of lower level items.
        is_folder = True
        # Add our item to the Kodi virtual folder listing.
        xbmcplugin.addDirectoryItem(_handle, url, list_item, is_folder)
    # Add a sort method for the virtual folder items (alphabetically, ignore articles)
    xbmcplugin.addSortMethod(_handle, xbmcplugin.SORT_METHOD_LABEL_IGNORE_THE)
    # Finish creating a virtual folder.
    xbmcplugin.endOfDirectory(_handle)


def list_videos(category):
    # Set plugin category. It is displayed in some skins as the name
    # of the current section.
    xbmcplugin.setPluginCategory(_handle, category)
    # Set plugin content. It allows Kodi to select appropriate views
    # for this type of content.
    xbmcplugin.setContent(_handle, 'videos')
    # Get the list of videos in the category.
    videos = get_videos(category)
    # Iterate through videos.
    for video in videos:
        # Create a list item with a text label and a thumbnail image.
        list_item = xbmcgui.ListItem(label=video['name'])
        # Set additional info for the list item.
        # 'mediatype' is needed for skin to display info for this ListItem correctly.
        list_item.setInfo('video', {'title': video['name'],
                                    'genre': video['genre'],
                                    'mediatype': 'video'})
        # Set graphics (thumbnail, fanart, banner, poster, landscape etc.) for the list item.
        # Here we use the same image for all items for simplicity's sake.
        # In a real-life plugin you need to set each image accordingly.
        list_item.setArt({'thumb': video['thumb'], 'icon': video['thumb'], 'fanart': video['thumb']})
        # Set 'IsPlayable' property to 'true'.
        # This is mandatory for playable items!
        list_item.setProperty('IsPlayable', 'true')
        # Create a URL for a plugin recursive call.
        # Example: plugin://plugin.parrot.tv/?action=play&video=http://www.vidsplay.com/wp-content/uploads/2017/04/crab.mp4
        url = get_url(action='play', video=video['video'])
        # Add the list item to a virtual Kodi folder.
        # is_folder = False means that this item won't open any sub-list.
        is_folder = False
        # Add our item to the Kodi virtual folder listing.
        xbmcplugin.addDirectoryItem(_handle, url, list_item, is_folder)
    # Add a sort method for the virtual folder items (alphabetically, ignore articles)
    xbmcplugin.addSortMethod(_handle, xbmcplugin.SORT_METHOD_LABEL_IGNORE_THE)
    # Finish creating a virtual folder.
    xbmcplugin.endOfDirectory(_handle)


def play_video(path):
    # Create a playable item with a path to play.
    play_item = xbmcgui.ListItem(path=path)
    # Pass the item to the Kodi player.
    xbmcplugin.setResolvedUrl(_handle, True, listitem=play_item)


def router(paramstring):
    # Parse a URL-encoded paramstring to the dictionary of
    # {<parameter>: <value>} elements
    params = dict(parse_qsl(paramstring))
    # Check the parameters passed to the plugin
    if params:
        if params['action'] == 'listing':
            # Display the list of videos in a provided category.
            list_videos(params['category'])
        elif params['action'] == 'play':
            # Play a video from a provided URL.
            play_video(params['video'])
        else:
            # If the provided paramstring does not contain a supported action
            # we raise an exception. This helps to catch coding errors,
            # e.g. typos in action names.
            raise ValueError('Invalid paramstring: {0}!'.format(paramstring))
    else:
        # If the plugin is called from Kodi UI without any parameters,
        # display the list of video categories
        list_categories()


if __name__ == '__main__':
    # Call the router function and pass the plugin call parameters to it.
    # We use string slicing to trim the leading '?' from the plugin call paramstring
    router(sys.argv[2][1:])
