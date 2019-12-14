# -*- coding: utf-8 -*-

import xbmc
import xbmcgui
import sys


home = xbmcgui.Window(10000)
skin = home.getProperty("CurrentSkin")
if skin == "skin.estuary2-extended-s":
    xbmc.executebuiltin("RunPlugin(plugin://script.simpleplaylists/?mode=addCurrentUrl)")
else:
    pass
