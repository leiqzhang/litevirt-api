#!/usr/bin/python

import os

import utils


class Volume(object):
    def __init__(self, datastore, grp = None, name):
        self._grp = None
        self._capacity = capacity
        self._datastore = datastore
        self._name = name
        self._is_thin = 

    def capacity(self):
        return self._capacity

    def name(self):
        return self._name

    def is_thin(self):
        return self._thin


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


class Datastore(object):
    """Datastore structure:
        /datastore
            /guid
                /__anonym__  (dir to put anonymous volumes)
                /__vm_xxx__  (vm group)
                    /__vol1
                    /__vol2
                    /__vmspec
                    /__snapshot1
                    /__snapshot2
            /alias           (a symlink to a datastore guid)
            /.metadata       (datastore metadata)
    """
    def __init__(self, guid, alias = "", desc = ""):
        self._guid = guid
        self._root = os.path.join("/datastore", self._guid)
        self._alias = alias
        self._desc = desc

    def enumerate_groups(self):
        ret = list()

        try:
            ret = [g[6:] for g in os.listdir(self._root) \
                    if g != "__anonym__" and g.startswith("__vm__")]
        except IOError:
            pass

        return ret

    def enumerate_volumes(self, grp):
        pass

    def enumerate_anonymous_volumes(self):
        ret = list()

        try: 
            anonym_dir = os.path.join(self._root, "__anonym__")
            ret = [Volume(self._guid, v) for v in os.listdir(anonym_dir) \
                    if os.path.exists(anonym_dir)]
        except IOError:
            pass

        return ret

    def create_vmspec(self, grp):
        pass

    def delete_vmspec(self, grp):
        pass
        
    def create_volume(self, grp = None):
        pass

    def delete_volume(self, vol, grp = None):
        pass

    def clone_volume(self, vol, grp_from = None, grp_to = None):
        pass

    def create_group(self):
        pass

    def delete_group(self, grp):
        pass

    def create_snapshot(self, vol, grp = None):
        pass

    def delete_snapshot(self, vol, grp = None):
        pass
  
    @property
    def alias(self):
        return self._alias

    @property
    def description(self):
        return self._desc

    @property
    def guid(self):
        return self._guid

    @property
    def capacity(self):
        pass

    @property
    def used(self):
        pass

    @property
    def available(self):
        pass

if __name__ == '__main__':
    ds = Datastore("/tmp")
    print ds.enumerate_groups()
