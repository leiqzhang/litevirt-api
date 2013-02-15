SUBDIRS = \
    mimerender

pywebappdir = /var/www/litevirt
pywebapp_PYTHON = \
	server.py


EXTRA_DIST = \
	litevirt-api.spec

rpms: dist
	rpmbuild  -ta $(distdir).tar.gz


srpms: dist
	rpmbuild  -ts $(distdir).tar.gz

