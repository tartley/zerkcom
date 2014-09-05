# This Makefile is just a cheatsheet to remind me of some commonly used
# commands. I'm generally executing these on OSX with up-to-date gnu binaries
# on the PATH, or on Ubuntu, or on WindowsXP/7 with Cygwin binaries foremost on
# the PATH.

SHELL=/bin/bash

# Development

test:
	python -m unittest discover
.PHONY: test

pylint:
	pylint *.py
.PHONY: pylint

tags:
	ctags -R --languages=python .
.PHONY: tags

deps:
	# on Ubuntu 14.04
	# For Rabbyt, install OpenGL header files GL/gl.h & GL/glu.h
	sudo apt-get install mesa-common-dev freeglut3-dev
	. ~/.bashrc.virtualenvwrapper ; \
	rmvirtualenv zerkcom ; \
	mkvirtualenv -p `which python2.7` zerkcom ; \
	which pip ; \
	virtualenvwrapper_verify_active_environment ; \
	# To find GL/gl.h & GL/glu.h
	CFLAGS='-I/usr/include' \
	  pip install \
	    -r requirements.txt \
	    --find-links pypackages/ \
	    --allow-external Pyrex \
	    --allow-unverified Pyrex

clean:
	rm -rf build dist MANIFEST tags
	find . -name '*.py[oc]' -exec rm {} \;
.PHONY: clean


# Packaging

develop:
	# create executable entry points in our python or virtualenv's bin dir
	python setup.py develop
.PHONY: develop

sdist: clean
	python setup.py sdist --formats=zip,gztar
.PHONY: sdist

register: clean
	python setup.py sdist --formats=zip,gztar register 
.PHONY: register
 
upload: clean
	python setup.py sdist --formats=zip,gztar register upload
.PHONY: upload

