#!/usr/bin/env python
import os
import sys

import pytest


def main():
    from pytest_watch.command import main as pt_main

    sys.path.append(os.path.dirname(__file__))


    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.testing")
    sys.path.insert(0, "src")
    sys.path.insert(0, "examples/simple")

    pt_main()
    # return pytest.main('-x')

if __name__ == '__main__':
    sys.exit(main())
