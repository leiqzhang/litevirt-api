#!/usr/bin/python

import utils

class Volume(object):
    def __init__(self, 
                datastore, 
                capacity, 
                desc = '', 
                name = '',
                thin = True):
        self._guid = utils.uuidgen()
        self._grp = None
        self._capacity = capacity
        self._datastore = datastore
        self._desc = desc
        self._name = name
        self._thin = thin

    def join_to_group(self, grp):
        # guaranttee group type is valid
        if not isinstance(self._grp, VolumeGroup):
            return

        # move self out of an existing group
        if self._grp:
            self.remove_from_group()

        # add to the new group
        self._grp = grp
        self._grp.add(self)

    def remove_from_group(self):
        if self._grp and self in self._grp:
            self._grp.remove(self)

    def capacity(self):
        return self._capacity

    def guid(self):
        return self._guid

    def name(self):
        return self._name

    def description(self):
        return self._desc

    def thin_provisioning(self):
        return self._thin

        

class SnapshotVolume(Volume):
    def __init__(self, 
                base,
                datastore,
                desc = '',
                name = '',
                thin = True):
        Volume.__init__(self, datastore, base.capacity(), desc, name, thin)
        self._base = base

class MetadataVolume(Volume):
    pass

class Datastore(object):
    def __init__(self, pool, name = '', desc = ''):
        self._guid = utils.uuidgen()
        self._pool = pool
        self._capacity = 0
        self._available = 0
        self._used = 0
        self._volumes = set()
        self._volgrps = set()
        self._name = name
        self._desc = desc

    def enumerate_volumes(self):
        pass

    def create_volume(self):
        pass

    def delete_volume(self, vol):
        pass

    def clone_volume(self, vol):
        pass

    def enumerate_volume_groups(self):
        pass

    def create_volume_group(self):
        pass

    def delete_volume_group(self, vg):
        pass

    def create_snapshot(self, vol):
        pass

    def delete_snapshot(self, vol):
        pass

    def name(self):
        return self._name

    def description(self):
        return self._desc

    def guid(self):
        return self._guid


class StoragePool(object):
    def __init__(self, name = "", desc = ""):
        self._guid = utils.uuidgen()
        self._name = name
        self._desc = desc

    def probe_local_storage(self):
        pass

    def probe_remote_storage(self, url):
        pass

    def probe_block_storage(self, dev):
    

    def name(self):
        return self._name

    def guid(self):
        return self._guid

    def description(self):
        return self._desc


class VolumeGroup(set):
    def __init__(self):
        set.__init__(self, name = "", desc = "")
        self._guid = utils.uuidgen()
        self._name = name
        self._desc = desc

    def name(self):
        return self._name

    def description(self):
        return self._desc

    def guid(self):
        return self._guid


if __name__ == '__main__':
    pass    
