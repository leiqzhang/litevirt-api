SUBDIRS = \
    mimerender \
	pamauth

pywebappdir = /var/www/litevirt
pywebapp_PYTHON = \
	server.py

pemdir = /etc/ssl/private
dist_pem_DATA = \
	lighttpd.cert \
	litevirt.pem \
	litevirt.cert
	

EXTRA_DIST = \
	litevirt-api.spec

rpms: dist
	rpmbuild -ta --clean $(distdir).tar.gz


srpms: dist
	rpmbuild -ts --clean $(distdir).tar.gz

