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
    """Detect ethernet link status by ethtool

    :returns: whether the link is up or down
    """
        pass

    def flash_light(self):
    """
    Attempt to flash the ethernet light 

    :returns: None
    """
        pass

    def interface(self):
    """
    Get the interface name of the device

    :returns: interface name like eth0  
    """
        pass

    def vendor(self):
    """
    Get the vendor name of the device

    :returns: vendor name  
    """
        pass

    def driver(self):
    """
    Get the driver name of the device

    :returns: driver name
    """
        pass

    def path(self):
    """
    Get the device path under sysfs of the device

    :returns: sysfs path
    """
        pass

    def macaddr(self):
    """
    Get the mac address of the device

    :returns: mac address
    """
        pass

class EthernetManager(object):
    """
    Managing ethernet devices on the host.
    """
    def __init__(self):
        self._devs = self.enum_devs()

    def enumerate(self):
    """
    Enumerate all network adapters on the host

    :returns: a tuple contains all ethernet objects 
    """
        pass

    def get_devs(self):
    """
    Get all network adapters managed by manager

    :returns: a tuple contains all ethernet objects 
    """
        pass

    def find_devs(self,                 
                iface = None,
                vendor = None,
                driver = None,
                macaddr = None,
                path = None):
    """
    Find network adapters meet the query condition

    :returns: a tuple contains adapters meet the condition
    """
        pass

