SUBDIRS = \
	LitevirtAPI 


pylibdir = $(pythondir)
pylib_PYTHON = \
  mimerender.py

pyoptdir = /opt/litevirt/sbin
pyopt_PYTHON = \
	litevirt-api-server.py


EXTRA_DIST = \
	litevirt-api.spec

rpms: dist
	rpmbuild -ta --clean $(distdir).tar.gz


srpms: dist
	rpmbuild -ts --clean $(distdir).tar.gz

