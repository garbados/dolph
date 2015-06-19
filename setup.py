#!/usr/bin/env python

from distutils.core import setup, Command

class PyTest(Command):
    user_options = []
    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        import subprocess
        import sys
        errno = subprocess.call([sys.executable, 'runtests.py'])
        raise SystemExit(errno)

setup(name='Dolph',
      version='1.0',
      description='Automatic translator between dolphin and human languages',
      author='Diana Thayer',
      author_email='garbados@gmail.com',
      packages=['dolph'],
      cmdclass = {'test': PyTest}
     )