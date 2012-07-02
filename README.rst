Tanks
=====

A remake of the tanks from Atari 2600 Combat.

Description
-----------

Single player game, use arrow keys or WASD, and space.

See 'tanks -h' for command-line options.


Dependencies
------------

Python 2.7.
Tested on OSX, ought to work on others.

For dependencies see requirements.txt

Install
-------

For programmers::

    pip install tanks

For real people:  Wait for 'double-click to run' binaries, not available yet.

Known Problems
--------------

Still in progress.

Hacking
-------

To modify the code, create a Python 2.7 virtualenv::

    mkvirtualenv -p python2.7 tanks

On OSX, requires pyglet 1.2 (so that it works on 32 and 64 bit Python, and
removes dependency on pyobjc) At time of writing this is still in devlopment,
so checkout pyglet source and install manually::

    hg clone https://code.google.com/p/pyglet/
    cd pyglet
    python setup.py install

Install all other runtime requirements::

    pip install -r requirements.txt

Install the requirements needed to develop, e.g. to run tests::

    pip install -r requirements-dev.txt

Then don't forget to run::

    python setup.py develop

Run tests::

    make test

Run the program::

    tanks

See the Makefile for other handy reminders of commands I use a lot.

Thanks
------

The circus of genius game creators at Nolan Bushnell's original Atari.

Contact
-------

:Documentation & download:
    http://pypi.python.org/pypi/tanks/

:Souce code and issues:
    https://github.com/tartley/tanks/

:Contact the author:
    Jonathan Hartley, email: tartley at domain tartley.com, Twitter: @tartley.
