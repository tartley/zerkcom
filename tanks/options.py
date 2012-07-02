import argparse

from . import __doc__ as DOC, __name__, __version__


VERSION = '%s version %s' % (__name__, __version__)

EPILOG = '''
Documentation & downloads: http://pypi.python.org/pypi/%s/

%s
''' % (__name__, VERSION,)


def create_parser():
    parser = argparse.ArgumentParser(
        description=DOC,
        prog=__name__,
        epilog=EPILOG,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument('--version', action='version', version=VERSION)
    parser.add_argument('--fullscreen', action='store_true', default=False)
    parser.add_argument('--vsync', action='store_true', default=False)
    parser.add_argument('--exit', action='store_true', default=False)
    return parser

