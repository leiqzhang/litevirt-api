#
# Copyright 2012 - 2013 Litevirt.com.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA
#
# Refer to the README and COPYING files for full details of the license
#

#!/usr/bin/python

import os
import utils


class Volume(object):
    def __init__(self, grp, guid, alias = None):
        self._grp = grp
        self._alias = alias
        self._guid = guid
        self._path = os.path.join(self.group.path, guid)

    @property
    def alias(self):
        return self._alias

    @property
    def name(self):
        return "__vol__" + self._alias

    @property
    def group(self):
        return self._grp

    @property
    def guid(self):
        return self._guid

    @property
    def path(self):
        return self._path


class VolumeGroup(object):
    def __init__(self, datastore, guid, alias = ""):
        self._name = name
        self._datastore = datastore
        self._guid = guid
        self._path = os.path.join(self.datastore.path, guid)

    @property
    def alias(self):
        return self._alias

    @property
    def name(self):
        return "__vm__" + self.alias

    @property
    def guid(self):
        return self._guid

    @property
    def datastore(self):
        return self._datastore

    @property
    def path(self):
        return self._path

    def enumerate_volumes(self):
        ret = list()
        path = os.path.join(self._datastore.path, self.guid)

        try:
            ret = [Volume(self, f) for f in os.listdir(path) \
                    if f.startswith("__vol__")]
        except IOError:
            pass

        return ret

    def create_vmspec_volume(self, profile = None):
        pass

    def create_vm_volume(self, profile = None):
        pass

    def create_snapshot_volume(self, profile = None):
        pass
            
    def delete_volume(self, vol):
        pass

class Datastore(object):
    """Datastore structure:
        /datastore
            /guid            (datastore identified by guid)
                /guid        (group identified by guid)
                /__anonym__  (a symlink to the anonymous group)
                /__vm_xxx__  (a symlink to a naming group)
                    /guid            (volume)
                    /__vol__alias    (a symlink to a volume)
            /__datastore__alias      (a symlink to a datastore)
            /.metadata               (datastore metadata)
    """

    @staticmethod
    def create(alias = "", desc = ""):
        if not alias:
            alias = os.tempnam("/datastore")

        name = "__datastore__" + alias
        if os.path.exists(os.path.join("/datastore", name)):
            return None

        for retry in range(3):
            guid = utils.uuidgen()
            path = os.path.join("/datastore", guid)
            if not os.path.exists(path):
                os.mkdirs(path, 0755)
                os.symlink(path, os.path.join("/datastore", name))

                # initialize anonymous group 
                anonym_grp = os.path.join(path, utils.uuidgen())
                os.mkdirs(anonym_grp, 0755)
                os.symlink(anonym_grp, "__anonym__")

                return Datastore(guid, alias, desc) 

        return None

    @staticmethod
    def enumerate_host():
        pass
            
    def __init__(self, guid, alias = "", desc = ""):
        self._guid = guid
        self._path = os.path.join("/datastore", self.guid)
        self._alias = alias
        self._desc = desc

    def enumerate_groups(self):
        ret = list()

        try:
            ret = [VolumeGroup(self, grp) for grp in os.listdir(self.path) \
                    if grp == "__anonym__" and grp.startswith("__vm__")]
        except IOError:
            pass

        return ret


    def clone_volume(self, source, target):
        pass

    def migrate_volume(self, source, target):
        pass

    def create_group(self, alias = None):
        if not alias:
            alias = os.tempnam(self.path)

        name = "__vm__" + alias
        if os.path.exists(os.path.join(self.path, name)):
            return None

        for retry in range(3):
            guid = utils.uuidgen()
            path = os.path.join(self.path, guid)
            if not os.path.exists(path):
                os.mkdirs(path, 0755)
                os.symlink(path, os.path.join(path, name))
                return VolumeGroup(self, guid, alias)

        return None

    def delete_group(self, grp):
        pass
 
    @property
    def path(self):
        return self._path

    @property
    def alias(self):
        return self._alias

    @property
    def name(self):
        return "__datastore__" + self._alias

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
