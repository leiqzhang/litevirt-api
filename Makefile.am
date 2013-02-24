SUBDIRS = \
    mimerender \
	LitevirtAPI 

dist_libexec_SCRIPTS = \
	litevirt-api-server.py

dist_sbin_SCRIPTS = \
	litevirt-make-cert

pemdir = /etc/ssl/litevirt
dist_pem_DATA = \
	litevirt-api.pem \
	litevirt-api.crt
	

EXTRA_DIST = \
	litevirt-api.spec

install-exec-hook:
	mv $(DESTDIR)$(libexecdir)/litevirt-api-server.py $(DESTDIR)$(libexecdir)/litevirt-api-server

rpms: dist
	rpmbuild -ta --clean $(distdir).tar.gz


srpms: dist
	rpmbuild -ts --clean $(distdir).tar.gz

