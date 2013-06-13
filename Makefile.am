SUBDIRS = \
    mimerender \
	LitevirtAPI 

dist_libexec_SCRIPTS = \
	litevirt-api-server.py


EXTRA_DIST = \
	litevirt-api.spec

install-exec-hook:
	mv $(DESTDIR)$(libexecdir)/litevirt-api-server.py $(DESTDIR)$(libexecdir)/litevirt-api-server

rpms: dist
	rpmbuild -ta --clean $(distdir).tar.gz


srpms: dist
	rpmbuild -ts --clean $(distdir).tar.gz

