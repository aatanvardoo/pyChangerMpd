from mpd import MPDClient
import time
from threading import Lock
current_milli_time = lambda: int(round(time.time() * 1000))

class ibusMpd(MPDClient):
    
    player = MPDClient()
    
    cdNumber = 1
    trackNumber = 1
    kodiTrNumbers = 60 #dummy value
    preDefPlaylist=['usb0/Dance','usb0/Nowe','usb0/DiscoPolo']
    numberOfPlaylist = 0 #[0:xx]
    elapsed = 0
    lock = Lock()
    def __init__(self, debug):
        self.debug = debug
        self.player.timeout = 10
        self.player.idletimeout = None

        self.pingMpd(40)
        self.connect()
        self.player.setvol(80)
        self.player.repeat(1)
        self.player.crossfade(2)
        self.player.close()
        self.disconnect()
        self.initPlaylists()
        self.setPlaylist()
        
    def connect(self):
        try:
            self.player.connect("localhost",6600)
        except:
            connected = False
            self.dbgPrint("Cannot connect")
        else:
            connected = True
            #self.dbgPrint("Connected")
        
        return connected
    
    def disconnect(self):
        try:
            self.player.disconnect()
        except:
            disconnected = False
            self.dbgPrint("Cannot disconnect")
        else:
            disconnected = True
            #self.dbgPrint("Disconnected")
            
        return disconnected 
    def pingMpd(self,timeout):
        sec = 0;
        while sec < timeout:
            try:
                out = self.player.connect("localhost",6600)
            except:
                self.dbgPrint("Cannot connect")
            else:
                self.dbgPrint("Connected " + str(out))
                break
            
            time.sleep(2)
            sec += 1
        self.player.close()
        self.disconnect()
    def playSong(self):
        self.lock.acquire()
        if self.connect():
            self.player.play(self.trackNumber - 1)      
            self.player.close()
        self.disconnect()
        self.lock.release()
        
    def stopPlay(self):
        self.lock.acquire()
        if self.connect():
            self.player.stop()
            self.player.close()
        self.disconnect()
        self.lock.release()
        
    def initPlaylists(self):
        self.numberOfPlaylist = len(self.preDefPlaylist)
        print("Number of playlists: " + str(self.numberOfPlaylist)) 
   
    def setPlaylist(self):
        self.lock.acquire()
        if self.connect():
            if self.cdNumber <= self.numberOfPlaylist and self.cdNumber > 0:
                now  = current_milli_time()
                result = self.player.clear()
    
                self.dbgPrint("Clear result: " + str(result))
                
                result = self.player.listall(self.preDefPlaylist[self.cdNumber - 1])
    
                self.dbgPrint("Add result: " + str(result[0]))
                
                items = len(result)#one item is reserved for path of dir
                self.dbgPrint("PLaylist track limits: " + str(items - 1))
                
                self.kodiTrNumbers = items - 1 #total tracks in current Playlist
                
                for i in range(1, items):
                    self.player.add(result[i]['file'])
                
                then = current_milli_time()
                then = then - now
                self.dbgPrint("Reading kodi playlist info took: " + str(then))
                
            else:
                print("ERROR cd number out of range! CD: " + str(self.cdNumber) + " playlists: " + str(self.numberOfPlaylist))
            self.player.close()
            self.disconnect()
        self.lock.release()
        
    def getStatus(self):
        out = None
        self.lock.acquire()
        if self.connect():
            out = self.player.status()
        self.disconnect()
        self.lock.release()
        return out
        
    def trackChanged(self):
        out = self.getStatus()
        if out != None:
            if out['state'] == 'play':
                elapsedNow = int(float(out['elapsed']))#current time of song
                trackNow = int(out['song']) #current song
                
                #if there is new song
                if self.trackNumber != trackNow +1 and elapsedNow < self.elapsed:
                    self.trackNumber = trackNow + 1
                    self.elapsed = elapsedNow
                    return True
    
                #song did not change
                self.elapsed = elapsedNow
        return False
            
    def dbgPrint(self, string):
        if self.debug:
            print(string)