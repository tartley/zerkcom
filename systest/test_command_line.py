from subprocess import PIPE, Popen
from unittest import TestCase


def assert_output(actual, expecteds):
    if isinstance(expecteds, str):
        assert actual == expecteds, actual
    else:
        for expected in expecteds:
            assert expected in actual, \
                '"%s" not found in:\n%s' % (expected, actual)


def call_process(command, expected_out='', expected_err=''):
    process = Popen(
        command, shell=True,
        stdout=PIPE, stderr=PIPE,
    )
    out, err = process.communicate()
    out = out.decode('unicode_escape')
    err = err.decode('unicode_escape')
    assert process.returncode == 0, '\n%s\n%s' % (err, out)
    assert_output(err, expected_err)
    assert_output(out, expected_out)


class CommandLineArgsTest(TestCase):

    def test_help(self):
        call_process('zerkcom --help', ['usage:', 'zerkcom version '])

    def test_version(self):
        call_process('zerkcom --version', expected_err=['zerkcom version '])

