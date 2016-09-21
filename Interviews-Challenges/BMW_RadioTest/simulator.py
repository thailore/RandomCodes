'''HW simulation class
'''
class RadioEmulation(object):
    '''This class emulates basic radio behavior
    '''
    STATIONS = ["DW1", "DW2", "DW3"]
    def __init__(self):
        self.station = None
        self.favorite = None
        self.current_volume = None
        self.default_volume = 0
        self.mute_volume = None
        self.volumes = xrange(10)
        self.status = None
        self.traffic_report_station = "DW3"
        return None
     
    def set_station(self, station):
        '''Set radio station
        '''
        if station in self.STATIONS:
            self.station = station
        else:
            raise Exception("Wrong station name: [{}]".format(station))
        if station == "DW3":
            self.current_volume += 3
 
    def get_station(self):
        '''Get radio staion
        '''
        return self.station
     
    def favorite_station(self, station=None):
        '''Save the station to be default station in the future
        '''
        if station:
            self.favorite = station
        else:
            return self.favorite
     
    def restore_station(self):
        '''Restore the saved station
        '''
        return self.favorite_station
     
    def set_volume(self, volume):
        '''Set the volume level
        '''
        if volume in self.volumes:
            self.current_volume = volume
        else:
            raise Exception("Volume out of the scope!")
     
    def get_volume(self):
        '''Get curent volume from the radio
        '''
        return self.current_volume
     
    def mute_on(self):
        '''Mute the radio
        '''
        self.mute_volume = self.get_volume()
        self.current_volume = 0
     
    def mute_off(self):
        '''Turn off the mute
        '''
        self.set_volume(self.default_volume)
     
    def power(self, status="on"):
        '''Set on/off the radio
        '''
        if status == "on":
            self.station = "DW1"
            self.status = "on"
        else:
            self.status = "off"
