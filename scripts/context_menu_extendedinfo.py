# -*- coding: utf-8 -*-

import xbmc
import xbmcgui
import sys


def main():
    info = sys.listitem.getVideoInfoTag()
    dbid = info.getDbId()
    db_type = info.getMediaType()
    remote_id = sys.listitem.getProperty("id")
    BASE = "RunScript(script.extendedinfo,info="
    if not dbid:
        dbid = sys.listitem.getProperty("dbid")
    if db_type == "movie":
        xbmc.executebuiltin("%sextendedinfo,dbid=%s,id=%s,name=%s)" % (BASE, dbid, remote_id, info.getTitle()))
    elif db_type == "tvshow":
        xbmc.executebuiltin("%sextendedtvinfo,dbid=%s,id=%s)" % (BASE, dbid, remote_id))
    elif db_type == "season":
        xbmc.executebuiltin("%sseasoninfo,tvshow=%s,season=%s)" % (BASE, info.getTVShowTitle(), info.getSeason()))
    elif db_type in ["actor", "director"]:
        xbmc.executebuiltin("%sextendedactorinfo,name=%s)" % (BASE, sys.listitem.getLabel()))

home = xbmcgui.Window(10000)
skin = home.getProperty("CurrentSkin")
if skin == "skin.estuary2-extended":
    main()
else:
    pass
