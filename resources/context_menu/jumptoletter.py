# -*- coding: utf-8 -*-

import xbmc
import xbmcgui

home = xbmcgui.Window(10000)
skin = home.getProperty("CurrentSkin")
if skin == "skin.estuary2-extended-s":
    xbmc.executebuiltin("SetFocus(8000)")
else:
    pass
