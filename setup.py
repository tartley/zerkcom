#!/usr/bin/env python2.7
from glob import glob
import os
from os.path import join
import re
import sys

from setuptools import setup, find_packages

# setup.py should not import non-stdlib modules, other than setuptools, at
# module level, since this requires them to be installed to run any setup.py
# command. (e.g. running 'setup.py sdist' should not require installing py2exe.)

# setup.py should not import from our local source (pip needs to be able to
# import setup.py before our dependencies have been installed)


NAME = 'tanks'


def read_description(filename):
    '''
    Read given textfile and return (2nd_para, 3rd_para to end)
    '''
    with open(filename) as fp:
        text = fp.read()
    paras = text.split('\n\n')
    return paras[1], '\n\n'.join(paras[2:])


def read_file(filename):
    with open(filename, "rt") as filehandle:
        return filehandle.read()

def find_value(source, identifier):
    '''
    Manually parse the given source, looking for lines of the form:
        <identifier> = '<value>'
    Returns the value. We do this rather than import the file directly because
    its dependencies will not be present when setuptools runs this setup.py
    before installing our dependencies, to find out what they are.
    '''
    regex =r"^%s\s*=\s*['\"]([^'\"]*)['\"]$" % (identifier,)
    match = re.search(regex, source, re.M)
    if not match:
        raise RuntimeError(
            "Can't find '%s' in source:\n%s" % (identifier, source)
        )
    return match.group(1)


def get_package_data(topdir, excluded=set()):
    retval = []
    for dirname, subdirs, files in os.walk(join(NAME, topdir)):
        for x in excluded:
            if x in subdirs:
                subdirs.remove(x)
        retval.append(join(dirname[len(NAME) + 1:], '*.*'))
    return retval


def get_data_files(dest, source):
    retval = []
    for dirname, subdirs, files in os.walk(source):
        retval.append(
            (join(dest, dirname[len(source)+1:]), glob(join(dirname, '*.*')))
        )
    return retval


def get_sdist_config():
    description, long_description = read_description('README')

    install_requires = []
    if sys.version_info < (2, 7):
        install_requires.append("argparse >= 1.2.1")

    return dict(
        name=NAME,
        version=find_value(read_file(join(NAME, '__init__.py')), '__version__'),
        description=description,
        long_description=long_description,
        url='http://pypi.python.org/pypi/%s/' % (NAME,),
        author='Jonathan Hartley',
        author_email='tartley@tartley.com',
        keywords='TODO space separated words TODO',
        entry_points = {
            'console_scripts': ['{0} = {0}.main:main'.format(NAME)],
            'gui_scripts': [],
        },
        install_requires=install_requires,
        packages=find_packages(exclude=('*.tests',)),
        #include_package_data=True,
        #package_data={
            #'package.subpackage': ['globs'],
            #NAME: get_package_data('data')
        #},
        #exclude_package_data={
            #'package.subpackage': ['globs']
        #},
        #data_files=[
            # ('install-dir', ['files-relative-to-setup.py']),
        #], 
        # see classifiers:
        # http://pypi.python.org/pypi?:action=list_classifiers
        classifiers=[
            #'Development Status :: 1 - Planning',
            'Development Status :: 2 - Pre-Alpha',
            #'Development Status :: 3 - Alpha',
            #'Development Status :: 4 - Beta',
            #'Development Status :: 5 - Production/Stable',
            #'Development Status :: 6 - Mature',
            #'Development Status :: 7 - Inactive',
            #'Environment :: Console',
            #'Environment :: MacOS X',
            #'Environment :: No Input/Output (Daemon)',
            #'Environment :: Web Environment',
            #'Environment :: Win32 (MS Windows)',
            #'Environment :: X11 Applications',
            #'Intended Audience :: Developers',
            #'Intended Audience :: End Users/Desktop',
            'License :: OSI Approved :: BSD License',
            'Natural Language :: English',
            'Operating System :: Microsoft :: Windows :: Windows 7',
            'Operating System :: MacOS :: MacOS X',
            'Operating System :: POSIX :: Linux',
            'Operating System :: OS Independent',
            'Programming Language :: Python :: 2',
            'Programming Language :: Python :: 2.7',
            #'Programming Language :: Python :: 3',
            #'Programming Language :: Python :: 3.2',
            'Programming Language :: Python :: Implementation :: CPython',
            #'Topic :: Games/Entertainment',
        ],
        zip_safe=True,
    )


def get_py2app_config():
    # This doesn't work. When I run the resulting application, it
    # barfs due to missing stdlib packages 'platform' and 'ctypes'. Adding
    # 'platform' to 'options.py2app.packages' (below) fixes that error, but
    # adding 'ctypes' does not. :-(
    return dict(
        app=[join(NAME, 'main.py')],
        options=dict(
            py2app=dict(
                argv_emulation=True,
                packages=['platform', 'ctypes'],
            ),
        ),
    )


def main():
    config = {}
    config.update(get_sdist_config())
    if 'py2app' in sys.argv:
        config.update(get_py2app_config())
    setup(**config)


if __name__ == '__main__':
    main()

