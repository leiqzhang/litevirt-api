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
from errors import NotFoundError

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
        self._datastore = datastore
        self._guid = guid
        self._path = os.path.join(self.datastore.path, guid)

    @property
    def alias(self):
        return self._alias

    @property
    def name(self):
        return self.alias

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
                /anonymous   (a symlink to the anonymous group)
                /vm          (a symlink to a naming group)
                    /guid            (volume)
                    /volume          (a symlink to a volume)
            /alias                   (a symlink to a datastore)
            /.litevirt               (datastore identifier)
    """

    # default datastore path
    _dsroot = "/datastore"

    # default anonymous group name
    _anonymous = "anonymous"

    # default datastore prefix
    _dsprefix = "datastore"

    # legal schemes
    _schemes = ("file", "nfs")

    @staticmethod
    def create(uri, alias = ""):
        # create datastore root dir if it does not exist
        if not os.path.exists(Datastore._dsroot):
            os.makedirs(Datastore._dsroot)

        from urlparse import urlparse
        ohash = urlparse(uri)

        if ohash.scheme not in Datastore._schemes:
            return None

        # return None if given uri is already created
        if os.path.exists(os.path.join(Datastore._dsroot, uri)):
            return None

        # fails to create the datastore if alias exists
        if alias and os.path.exists(os.path.join(Datastore._dsroot, alias)):
                return None

        # if alias not provided, then try to create a default one
        if not alias:
            for avail in range(1, 1024):
                if not os.path.exists(os.path.join(Datastore._dsroot, Datastore._dsprefix + str(avail))):
                    alias = Datastore._dsprefix + str(avail)
                    break

        # if alias not provided nor the default one created successfully,
        # return a failure.
        if not alias:
            return None

        uuid = utils.uuidgen()
        path = os.path.join(Datastore._dsroot, uuid)
        if ohash.scheme == "file":
            # only a link is required for a local dir
            os.symlink(ohash.path, path)
        else:
            os.mkdirs(path, 0755)

        cwd = os.getcwd()
        os.chdir(Datastore._dsroot)
        os.symlink(uri, alias)

        # create anonymous dir if it does not exist
        anonym = utils.uuidgen()
        if not os.path.exists(os.path.join(path, Datastore._anonymous)):
            os.makedirs(os.path.join(path, anonym), 0755)
            os.chdir(path)
            os.symlink(anonym, Datastore._anonymous)
        os.chdir(cwd)
        return Datastore(uri, alias) 

            
    def __init__(self, uri, alias):
        if uri and not os.path.exists(os.path.join(Datastore._dsroot, uri)):
            raise NotFoundError("%s not found" % uri)

        if not os.path.islink(os.path.join(Datastore._dsroot, alias)):
            raise NotFoundError("%s not found" % alias)

        self._uri = uri
        self._alias = alias

        if alias and not uri:
            cwd = os.getcwd()
            os.chdir(Datastore._dsroot)
            self._uri = os.readlink(self._alias)
            os.chdir(cwd)
        

    def mount(self):
        pass

    def enumerate_groups(self):
        ret = list()

        try:
            ret = [VolumeGroup(self, grp) for grp in os.listdir(self.path) \
                    if os.path.isdir(os.path.join(self.path, grp))]
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
    ds = Datastore.create("file:///tmp/test")
    print ds.enumerate_groups()
