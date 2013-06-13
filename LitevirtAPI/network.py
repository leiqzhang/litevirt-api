#!/usr/bin/python

class EthernetDevice(object):
    """Representative of an ethernet device. """

    def __init__(self, 
                iface = None,
                vendor = None,
                driver = None,
                macaddr = None,
                path = None):
        self._iface = iface
        self._vendor = vendor
        self._driver = driver
        self._path = path
        self._macaddr = macaddr

    def link_status(self):
        pass

    def flash_light(self):
        pass

    def interface(self):
        pass

    def vendor(self):
        pass

    def driver(self):
        pass

    def path(self):
        pass

    def macaddr(self):
        pass

class EthernetManager(object):
    def __init__(self):
        self._devs = self.enum_devs()

    def enumerate(self):
        pass

    def get_devs(self):
        pass

    def find_devs(self,                 
                iface = None,
                vendor = None,
                driver = None,
                macaddr = None,
                path = None):
        pass

