Zerkcom
=======

A retro videogame mashup of Atari 2600 Combat tanks and Bezerk.
Status: Displays moving tanks, but isn't a game yet.

Description
-----------

Single player game, use arrow keys or WASD, and space.

See 'zerkcom -h' for command-line options.

Screenshot
----------

.. image:: screenshots/latest.png

Dependencies
------------

Python 2.7.
Developed on OSX until 2014-09, might still work there.
Developed on Ubuntu 14.04 currently.

For dependencies see setup.py.

Install
-------

For programmers::

    pip install zerkcom

Run the game::

    zerkcom

Use --help to list options.

For real people:  Wait for 'double-click to run' binaries, not available yet.

Known Problems
--------------

Nothing works yet.
See TODO.rst

Hacking
-------

To install dependencies, run 'make deps' on Ubuntu. Elsewhere, you'll have
to transcribe those commands into your own dialect. This will also install
executable script 'zerkcom' into your virtualenv bin dir, in "setup.py develop"
mode.

Requires pyglet 1.2 (so that it works on 32 and 64 bit Python, and on OSX,
removes dependency on pyobjc) At time of writing this is not released to PyPI,
so we use a local copy saved in pypackages/.

To install the extra requirements needed to develop, e.g. to run tests::

    pip install -r requirements-dev.txt

Run tests::

    make test

See the Makefile for other handy reminders of commands I use a lot.

Thanks
------

Pyglet-users mailing list participants Richard, Andy, for invaluable advice,
corrections and reassurance.
The circus of genius game creators at Nolan Bushnell's original Atari.

Contact
-------

:Download & Documentation (for users):
    http://pypi.python.org/pypi/zerkcom
    (actually, not uploaded yet.)

:Souce code and issues (for hackers):
    https://github.com/tartley/zerkcom

:Contact the author:
    Jonathan Hartley, email: tartley at domain tartley.com, Twitter: @tartley.

