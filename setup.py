#!/usr/bin/env python2.7
from glob import glob
import os
import re
import sys

from setuptools import setup, find_packages

# setup.py should not import non-stdlib modules, other than setuptools, at
# module level, since this requires them to be installed to run any setup.py
# command. (e.g. running 'setup.py sdist' should not require installing py2exe.)

# setup.py should not import from our local source (pip needs to be able to
# import setup.py before our dependencies have been installed)


NAME = 'tanks'

INSTALL_REQUIRES = [
    'colortuple==1.0.2',
    'py2d==0.1',
    'pyglet==1.2alpha1',
    'PyOpenGL==3.0.2a5',
    'Pyrex==0.9.9',
    'Rabbyt==0.8.3',
]



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



def get_package_data(topdir):
    return (
        os.path.join(dirname[len(NAME) + 1:], '*.*')
        for dirname, subdirs, files in os.walk(topdir)
    )


def get_data_files(dest, source):
    return [
        (
            os.path.join(dest, dirname[len(source) + 1:]),
            glob(os.path.join(dirname, '*.*'))
        )
        for dirname, subdirs, files in os.walk(source)
    ]


def get_sdist_config(data_dir):
    description, long_description = read_description('README.rst')
    return dict(
        name=NAME,
        version=find_value(
            read_file(os.path.join(NAME, '__init__.py')),
            '__version__'
        ),
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
        install_requires=INSTALL_REQUIRES,
        packages=find_packages(exclude=('*.tests',)),
        include_package_data=True,
        #package_data={
            #'package.subpackage': ['globs'],
            #NAME: get_package_data('data')
        #},
        #exclude_package_data={
            #'package.subpackage': ['globs']
        #},
        #data_files=get_data_files(data_dir, 'data'),
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
            'Topic :: Games/Entertainment',
        ],
        zip_safe=True,
    )


def create_manifest_in(data_dir):
    with open('MANIFEST.in', 'w') as fd:
        for dirname, subdirs, files in os.walk(data_dir):
            fd.write('include %s/*.*\n' % (dirname, ))
                
def main():
    data_dir = os.path.join(NAME, 'data')
    create_manifest_in(data_dir)

    config = get_sdist_config(data_dir)
    if '--verbose' in sys.argv:
        from pprint import pprint
        pprint(config)

    setup(**config)


if __name__ == '__main__':
    main()

