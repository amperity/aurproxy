# Aurproxy build file

default: dist

.PHONY: clean setup dist

version := $(shell date "+%Y%m%d")
platform := $(shell uname | tr '[A-Z]' '[a-z]')

# Clean up intermediate files.
clean:
	rm -rf venv dist aurproxy.pex

# Install Python dependencies in a local virtual environment.
setup: venv/bin/activate

venv/bin/activate: setup.py requirements_dev.txt
	test -d venv || virtualenv venv
	. venv/bin/activate; pip install -r requirements_dev.txt .
	touch venv/bin/activate

# Package up Aurproxy for distribution.
dist: dist/aurproxy-$(version)-$(platform).tar.gz

aurproxy.pex: setup.py $(shell find tellapart -type f -name \*.py)
	venv/bin/pex --build --entry-point tellapart.aurproxy.command \
		--output-file aurproxy.pex .

dist/aurproxy-$(version)-$(platform).tar.gz: aurproxy.pex templates
	@mkdir -p dist
	tar -cvzf $@ $^
