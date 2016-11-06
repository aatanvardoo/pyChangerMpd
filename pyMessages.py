
phoneLedRed= [0xC8,0x04,0xF0,0x2B,0x01]
phoneLedGreen = [0xC8,0x04,0xF0,0x2B,0x10]
phoneLedYellow= [0xC8,0x04,0xF0,0x2B,0x04]


radioPollResp = [0x18,0x04,0xFF,0x02,0x00]#,0xE1]
startPlayResp= [0x18,0x0a,0x68,0x39,0x02,0x09,0x00,0x01,0x00,0x01,0x04,0x4c]
stopPlayingReq =  [0x68,0x05,0x18,0x38,0x01,0x00,0x4c]

#announcement message
announcementReq = [0x18,0x04,0xFF,0x02,0x01,0xE0]
pausePlayingReq = [0x68,0x05,0x18,0x38,0x02,0x00,0x4f]
startPlayReq =    [0x68,0x05,0x18,0x38,0x03,0x00]#,0x4e]
cdChangeReq =     [0x68, 0x05, 0x18, 0x38, 0x06, 0x02]#, 0x4a]
trackChangeNextReq = [0x68,0x05,0x18,0x38,0x0a,0x00]#,0x47] #Changes track/song to next
trackChangePrevReq = [0x68,0x05,0x18,0x38,0x0a,0x01]#,0x46] #Changes track/song to next

randomModeReq = [0x68, 0x5, 0x18, 0x38, 0x08, 0x01]#, 0x44]
introModeReq =  [0x68, 0x5, 0x18, 0x38, 0x07, 0x01]#, 0x4b]

scanTrackReq = [0x68, 0x05, 0x18, 0x38, 0x04, 0x01]#,0x48]
statReq =      [0x68, 0x05, 0x18,  0x38,0x00,0x00]# crc 0x4d]
cdpoll =       [0x68, 0x03, 0x18,  0x01, 0x72]
bmForwPush =   [0xF0, 0x04, 0x68, 0x48, 0x00, 0xD4] 
bmForwRel =    [0xF0, 0x04, 0x68, 0x48, 0x80, 0x54]
bmForwPress =  [0xF0, 0x04, 0x68, 0x48, 0x40, 0x94]

yatourPoll=    [0x18, 4, 255, 2, 0]#6

yatourPoll2=    [255, 0, 255, 2, 0]
stopPlayingReq2 =  [0x68,0x00,0x18,0x38,0x01,0x00]
startPlayingReq2 =  [0x68,0x00,0x18,0x38,0x03,0x00]
pausePlayingReq2 = [0x68,0x00,0x18,0x38,0x02,0x00]
statReq2 =         [0x68,0x00,0x18,0x38,0x00,0x00]
trackChangeNextReq2 = [0x68,0x00,0x18,0x38,0x0a,0x00]
trackChangePrevReq2 = [0x68,0x05,0x18,0x38,0x0a,0x01]

randomModeReq2 = [0x68, 0x0, 0x18, 0x38, 0x08]

introModeReq2 =  [0x68, 0x0, 0x18, 0x38, 0x07]

cdChangeReq2 =     [0x68, 0x00, 0x18, 0x38, 0x06]
cdPollReq =        [0x68, 0x00, 0x18, 0x01]
scanTrackReq2 = [0x68, 0x00, 0x18, 0x38, 0x04]

statReqCDCD = [0x68,0x05,0x76,0x38,0x00,0x00]
statReqCDCD2 = [0x68,0x00,0x76,0x38,0x00,0x00]
oldtrackChangeNextReq2 = [0x68,0x00,0x18,0x38,0x05,0x00]
oldtrackChangeNextReq = [0x68,0x05,0x18,0x38,0x05,0x00]

oldtrackChangePrevReq2 = [0x68,0x00,0x18,0x38,0x05,0x01]
oldtrackChangePrevReq = [0x68,0x05,0x18,0x38,0x05,0x01]

testStat =     [0x18, 0x0a, 0x68, 0x39]
testStat2 =    [0x18, 0x00, 0x68, 0x39]
msgList = [[statReq2,6,0,0],
           [statReqCDCD2,6,0,0],
           [stopPlayingReq2,6,0,0],
           [startPlayingReq2,6,0,0],
           [pausePlayingReq2,6,0,0],
           [trackChangeNextReq2,6,0,0],
           [trackChangePrevReq2,6,0,0],
           [oldtrackChangeNextReq2,6,0,0],
           [oldtrackChangePrevReq,6,0,0],
           [cdChangeReq2,5,0,0],
           [randomModeReq2,5,0,0],
           [introModeReq2,5,0,0],
           [scanTrackReq2,5,0,0],
           [testStat2,  4,0,0],
           [cdPollReq,  4,0,0]]