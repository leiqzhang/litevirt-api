SUBDIRS = \
    mimerender

pywebappdir = /var/www/litevirt
pywebapp_PYTHON = \
	server.py


EXTRA_DIST = \
	litevirt-api.spec

rpms: dist
	rpmbuild -ta --clean $(distdir).tar.gz


srpms: dist
	rpmbuild -ts --clean $(distdir).tar.gz

