# speedportEntry2i - Python Plugin for SpeedPort Entry 2i ADSL/VDSL Router
#
# Author: ycahome, 2018
#
#  version 1.0.0 (2018-02-23): Initial Version
#
#
#
"""
<plugin key="speedportEntry2i" name="SpeedPort Entry 2i ADSL/VDSL Routers" author="ycahome" version="1.0.0" externallink="https://www.domoticz.com/forum/viewtopic.php?f=65&t=22339">
    <description>
    		<h2>SpeedPort Entry 2i ADSL/VDSL Routers v.1.0.0</h2><br/>
    </description>
    <params>
        <param field="Address" label="Router IP" width="200px" required="true" default="192.168.1.1"/>
        <param field="Mode5" label="Notifications" width="75px">
            <options>
                <option label="Enabled" value="Notify"/>
                <option label="Disable" value="Disable"  default="true" />
            </options>
        </param>
        <param field="Mode6" label="Debug" width="75px">
            <options>
                <option label="True" value="Debug"/>
                <option label="False" value="Normal"  default="true" />
            </options>
        </param>
    </params>
</plugin>
"""

import Domoticz
import os
import subprocess
import sys

import time
import urllib
import urllib.request
import urllib.error

#from urllib2 import urlopen
from datetime import datetime, timedelta


class BasePlugin:
    enabled = False
    pluginState = "Not Ready"
    sessionCookie = ""
    privateKey = b""
    socketOn = "FALSE"

    def __init__(self):
        self.debug = False
        self.error = False
        self.nextpoll = datetime.now()
        self.pollinterval = 60  #Time in seconds between two polls
        
        self.plugindata = {
            # Sensor No:            [Name,                  repository,                     plugin key]
            "2":                    ["Speed(Down)",         "SNMPreader",                   "SNMPreader"],
            "3":                    ["Speed(Up)",           "SNMPreader",                   "SNMPreader"],
            "4":                    ["Noise(Down)",         "NUT_UPS",                      "NUT_UPS"],
            "5":                    ["Noise(Up)",           "Mi_Flower_mate_plugin",        "Mi_Flower_mate_plugin"],
            "6":                    ["CRC Errors(Down)",    "sonos",                        "Sonos"],
            "7":                    ["CRC Errors(Up)",      "Dummy_Plugin",                 "Dummy_Plugin"],
            "8":                    ["Atten(Down)",         "Dummy_Plugin",                 "Dummy_Plugin"],
            "9":                    ["Atten(Up)",           "Dummy_Plugin",                 "Dummy_Plugin"],
            "8":                    ["FEC Errors(Down)",    "Dummy_Plugin",                 "Dummy_Plugin"],
            "9":                    ["FEC Errors(Up)",      "Dummy_Plugin",                 "Dummy_Plugin"],
        }        
        
        return

    def onStart(self):

        Domoticz.Debug("onStart called")

        if Parameters["Mode6"] == 'Debug':
            self.debug = True
            Domoticz.Debugging(1)
            DumpConfigToLog()
        else:
            Domoticz.Debugging(0)


        
        if 1 not in Devices:
            try:
                Domoticz.Device(Name="Status", Unit=1, TypeName="Custom",Options={"Custom": "1;Phase"},Used=1).Create()
            except:
                Domoticz.Error("Device 1 Creation Error.")
            else:
                Domoticz.Log("Device created.")

        for x in range (2,3,4,5,6,7,8,9)
            if x not in Devices:
                try:
                    Domoticz.Device(Name="Status", Unit=x, TypeName="Custom",Options={"Custom": "1;Phase"},Used=1).Create()
                except:
                    Domoticz.Error("Device " + x + " Creation Error.")
                else:
                    Domoticz.Log("Device " + x + " created.")
                
                
                
                DumpConfigToLog()
            
        #Domoticz.Heartbeat(int(Parameters["Mode1"]))


    def onStop(self):
        Domoticz.Log("Plugin is stopping.")
        Domoticz.Debugging(0)

    def onHeartbeat(self):

        Domoticz.Debug("onHeartbeat called")




global _plugin
_plugin = BasePlugin()

def onStart():
    global _plugin
    _plugin.onStart()

def onStop():
    global _plugin
    _plugin.onStop()

def onHeartbeat():
    global _plugin
    _plugin.onHeartbeat()


# Generic helper functions
def DumpConfigToLog():
    for x in Parameters:
        if Parameters[x] != "":
            Domoticz.Debug( "'" + x + "':'" + str(Parameters[x]) + "'")
    Domoticz.Debug("Device count: " + str(len(Devices)))
    for x in Devices:
        Domoticz.Debug("Device:           " + str(x) + " - " + str(Devices[x]))
        Domoticz.Debug("Device ID:       '" + str(Devices[x].ID) + "'")
        Domoticz.Debug("Device Name:     '" + Devices[x].Name + "'")
        Domoticz.Debug("Device nValue:    " + str(Devices[x].nValue))
        Domoticz.Debug("Device sValue:   '" + Devices[x].sValue + "'")
    return






#
# Parse an int and return None if no int is given
#

def parseIntValue(s):

        try:
            return int(s)
        except:
            return None


def mid(s, offset, amount):
    return s[offset:offset+amount]
    
    
