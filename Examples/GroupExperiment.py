#!/usr/bin/env python

import datetime
import time
import wx

# Where can we find the ObjectListView module?
import sys
sys.path.append("..")

from ObjectListView import ObjectListView, ColumnDefn, ListGroup

# We store our images as python code
import ExampleImages

class Track(object):
    """
    Simple minded object that represents a song in a music library
    """
    def __init__(self, title, artist, album, sizeInBytes, lastPlayed, rating):
        self.title = title
        self.artist = artist
        self.album = album
        self.lastPlayed = datetime.datetime(*(time.strptime(lastPlayed, "%d/%m/%Y %I:%M %p")[0:6]))
        self.sizeInBytes = sizeInBytes
        self.rating = rating

    def GetSizeInMb(self):
        return self.sizeInBytes / (1024.0*1024.0)

class EmptyRow(object):
    def title(self): return ""
    def artist(self): return ""
    def sizeInBytes(self): return -1
    def lastPlayed(self): return None
    def rating(self): return ""

class MyFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        wx.Frame.__init__(self, *args, **kwds)
        self.Init()

    def Init(self):
        self.InitModel()
        self.InitWidgets()
        self.InitObjectListView()

    def InitModel(self):
        self.songs = [
            Track("Shiver", "Natalie Imbruglia", "Counting Down the Days", 8.6*1024*1024*1024, "9/03/2008 9:51 PM", 80),
            Track("Who's Gonna Ride Your Wild Horses", "U2", "Achtung Baby", 6.3*1024*1024, "9/10/2007 11:32 AM", 80),
            Track("So Cruel", "U2", "Achtung Baby", 6.9*1024*1024, "9/10/2007 11:38 AM", 60),
            Track("The Fly", "U2", "Achtung Baby", 5.4*1024*1024, "9/10/2007 11:42 AM", 60),
            Track("Tryin' To Throw Your Arms Around The World", "U2", "Achtung Baby", 4.7*1024*1024, "9/10/2007 11:46 AM", 60),
            Track("Ultraviolet (Light My Way)", "U2", "Achtung Baby", 6.6*1024*1024, "9/10/2007 11:52 AM", 60),
            Track("Acrobat", "U2", "Achtung Baby", 5.4*1024*1024, "9/10/2007 11:56 AM", 60),
            Track("Love Is Blindness", "U2", "Achtung Baby", 5.3*1024, "9/10/2007 12:00 PM", 60),
            Track("Elevation", "U2", "All That You Can't Leave Behind", 459, "25/01/2008 11:46 PM", 60),
            Track("Walk On", "U2", "All That You Can't Leave Behind", 5.8*1024*1024, "18/03/2008 11:39 PM", 100),
            Track("Kite", "U2", "All That You Can't Leave Behind", 5.2*1024*1024, "23/01/2008 10:36 PM", 40),
            Track("In A Little While", "U2", "All That You Can't Leave Behind", 4.3*1024*1024, "20/01/2008 7:48 PM", 60),
            Track("Wild Honey", "U2", "All That You Can't Leave Behind", 4.5*1024*1024, "13/04/2007 11:50 AM", 40),
            Track("Peace On Earth", "U2", "All That You Can't Leave Behind", 5.6*1024*1024, "22/12/2007 2:51 PM", 40),
            Track("When I Look At The World", "U2", "All That You Can't Leave Behind", 5.1*1024*1024, "22/12/2007 2:55 PM", 40),
            Track("New York", "U2", "All That You Can't Leave Behind", 6.4*1024*1024, "22/12/2007 3:01 PM", 60),
            Track("Grace", "U2", "All That You Can't Leave Behind", 6.5*1024*1024, "22/12/2007 3:06 PM", 40),
            Track("The Ground Beneath Her Feet(Bonus Track)", "U2", "All That You Can't Leave Behind", 4.4*1024*1024, "22/12/2007 3:10 PM", 40),
            Track("Follow You Home", "Nickelback", "All The Right Reasons", 6*1024*1024, "6/03/2008 10:42 PM", 40),
            Track("Fight For All The Wrong Reason", "Nickelback", "All The Right Reasons", 5.2*1024*1024, "15/03/2008 5:04 PM", 60),
            Track("Photograph", "Nickelback", "All The Right Reasons", 6*1024*1024, "15/03/2008 5:08 PM", 60),
            Track("Animals", "Nickelback", "All The Right Reasons", 4.3*1024*1024, "16/02/2008 12:12 AM", 40),
            Track("Savin' Me", "Nickelback", "All The Right Reasons", 5.1*1024*1024, "24/03/2008 10:41 AM", 80),
            Track("Far Away", "Nickelback", "All The Right Reasons", 5.5*1024*1024, "15/03/2008 5:30 PM", 40),
            Track("Next Contestant", "Nickelback", "All The Right Reasons", 5*1024*1024, "24/03/2008 9:47 AM", 80),
            Track("Side Of A Bullet", "Nickelback", "All The Right Reasons", 4.2*1024*1024, "6/03/2008 11:00 PM", 40),
            Track("If Everyone Cared", "Nickelback", "All The Right Reasons", 5*1024*1024, "6/03/2008 11:03 PM", 60),
            Track("Someone That You're With", "Nickelback", "All The Right Reasons", 5.6*1024*1024, "16/02/2008 12:34 AM", 40),
            Track("Rockstar", "Nickelback", "All The Right Reasons", 5.9*1024*1024, "16/02/2008 12:38 AM", 60),
            Track("Lelani", "Hoodoo Gurus", "Ampology", 5.9*1024*1024, "22/10/2007 8:45 PM", 60),
            Track("Tojo", "Hoodoo Gurus", "Ampology", 4.1*1024*1024, "22/10/2007 8:48 PM", 60),
            Track("My Girl", "Hoodoo Gurus", "Ampology", 3.3*1024*1024, "12/11/2007 7:57 PM", 80),
            Track("Be My Guru", "Hoodoo Gurus", "Ampology", 3.3*1024*1024, "20/03/2008 12:15 PM", 100),
            Track("I Want You Back", "Hoodoo Gurus", "Ampology", 3.9*1024*1024, "12/11/2007 7:42 PM", 80),
            Track("I Was A Kamikaze Pilot", "Hoodoo Gurus", "Ampology", 3.9*1024*1024, "22/10/2007 9:00 PM", 60),
            Track("Bittersweet", "Hoodoo Gurus", "Ampology", 4.7*1024*1024, "22/10/2007 9:04 PM", 60),
            Track("Poison Pen", "Hoodoo Gurus", "Ampology", 5*1024*1024, "22/10/2007 9:11 PM", 60),
            Track("In The Wild", "Hoodoo Gurus", "Ampology", 3.9*1024*1024, "22/10/2007 9:14 PM", 60),
            Track("Whats My Scene?", "Hoodoo Gurus", "Ampology", 4.6*1024*1024, "12/11/2007 7:51 PM", 100),
            Track("Heart Of Darkness", "Hoodoo Gurus", "Ampology", 3.8*1024*1024, "22/10/2007 9:21 PM", 60),
            Track("Good Times", "Hoodoo Gurus", "Ampology", 3.7*1024*1024, "20/03/2008 12:18 PM", 80),
            Track("Cajun Country", "Hoodoo Gurus", "Ampology", 4.9*1024*1024, "22/10/2007 9:28 PM", 60),
            Track("Axegrinder", "Hoodoo Gurus", "Ampology", 4.2*1024*1024, "22/10/2007 9:32 PM", 60),
            Track("Another World", "Hoodoo Gurus", "Ampology", 4*1024*1024, "20/03/2008 12:21 PM", 80),
            Track("Meant To Live", "Switchfoot", "The Beautiful Letdown", 4*1024*1024, "3/03/2008 1:46 PM", 100),
            Track("This Is Your Life", "Switchfoot", "The Beautiful Letdown", 4*1024*1024, "3/03/2008 2:11 PM", 100),
            Track("More than fine", "Switchfoot", "The Beautiful Letdown", 4.9*1024*1024, "3/03/2008 2:16 PM", 60),
            Track("Ammunition", "Switchfoot", "The Beautiful Letdown", 4.4*1024*1024, "3/03/2008 1:58 PM", 40),
            Track("Dare you to move", "Switchfoot", "The Beautiful Letdown", 4.9*1024*1024, "3/03/2008 2:20 PM", 80),
            Track("Redemption", "Switchfoot", "The Beautiful Letdown", 3.6*1024*1024, "19/03/2008 5:19 PM", 80),
            Track("The beautiful letdown", "Switchfoot", "The Beautiful Letdown", 6.2*1024*1024, "3/03/2008 2:29 PM", 60),
        ]

    def InitWidgets(self):
        panel = wx.Panel(self, -1)
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_1.Add(panel, 1, wx.ALL|wx.EXPAND)
        self.SetSizer(sizer_1)

        self.myOlv = ObjectListView(panel, -1, style=wx.LC_REPORT|wx.SUNKEN_BORDER)
        sizer_2 = wx.BoxSizer(wx.VERTICAL)
        sizer_2.Add(self.myOlv, 1, wx.ALL|wx.EXPAND, 4)
        panel.SetSizer(sizer_2)

        self.Layout()

    def InitObjectListView(self):
        groupImage = self.myOlv.AddImages(ExampleImages.getGroup16Bitmap(), ExampleImages.getGroup32Bitmap())
        userImage = self.myOlv.AddImages(ExampleImages.getUser16Bitmap(), ExampleImages.getUser32Bitmap())
        musicImage = self.myOlv.AddImages(ExampleImages.getMusic16Bitmap(), ExampleImages.getMusic32Bitmap())
        self.myOlv.AddNamedImages("collapsed", ExampleImages.getCollapsedBitmap())
        self.myOlv.AddNamedImages("expanded", ExampleImages.getExpandedBitmap())

        def trackImageGetter(track):
            if isinstance(track, (ListGroup, EmptyRow)):
                return -1
            else:
                return musicImage

        soloArtists = ["Nelly Furtado", "Missy Higgins", "Moby", "Natalie Imbruglia",
                       "Dido", "Paul Simon", "Bruce Cockburn"]
        def artistImageGetter(track):
            if isinstance(track, (ListGroup, EmptyRow)):
                return -1
            if track.artist in soloArtists:
                return userImage
            else:
                return groupImage

        def sizeToNiceString(byteCount):
            """
            Convert the given byteCount into a string like: 9.9bytes/KB/MB/GB
            """
            if byteCount < 0:
                return ""

            for (cutoff, label) in [(1024*1024*1024, "GB"), (1024*1024, "MB"), (1024, "KB")]:
                if byteCount >= cutoff:
                    return "%.1f %s" % (byteCount * 1.0 / cutoff, label)

            if byteCount == 1:
                return "1 byte"
            else:
                return "%d bytes" % byteCount

        def isExpanded(modelObject):
            if isinstance(modelObject, ListGroup):
                if modelObject.isExpanded:
                    return "expanded"
                else:
                    return "collapsed"
            else:
                return -1

        def rowFormatter(listItem, model):
            if isinstance(model, ListGroup):
                listItem.SetFont(wx.FFont(9, wx.FONTFAMILY_SWISS, wx.FONTFLAG_BOLD, "MS Sans Serif"))

        self.myOlv.SetColumns([
            ColumnDefn("", "left", 24, None, imageGetter=isExpanded),
            ColumnDefn("Title", "left", 120, "title", imageGetter=trackImageGetter),
            ColumnDefn("Artist", "left", 120, "artist", imageGetter=artistImageGetter),
            ColumnDefn("Size", "center", 100, "sizeInBytes", stringConverter=sizeToNiceString),
            ColumnDefn("Last Played", "left", 100, "lastPlayed"),
            ColumnDefn("Rating", "center", 100, "rating")
        ])
        songsAndGroups = list()
        for (i, x) in enumerate(self.songs):
            if i % 5 == 0:
                if i > 0:
                    songsAndGroups.append(EmptyRow())
                songsAndGroups.append(ListGroup(i, "Group #%d" % i))
            songsAndGroups.append(x)

        self.myOlv.rowFormatter = rowFormatter
        self.myOlv.SetObjects(songsAndGroups)

if __name__ == '__main__':
    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    frame_1 = MyFrame(None, -1, "ObjectListView Simple Example 2")
    app.SetTopWindow(frame_1)
    frame_1.Show()
    app.MainLoop()
