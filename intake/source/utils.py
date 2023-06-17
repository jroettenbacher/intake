# -----------------------------------------------------------------------------
# Copyright (c) 2012 - 2018, Anaconda, Inc. and Intake contributors
# All rights reserved.
#
# The full license is in the LICENSE file, distributed with this software.
# -----------------------------------------------------------------------------
from hashlib import md5


def tokenize(*args, **kwargs):
    """Deterministic token

    copied from dask
    """
    hasher = md5(str(tuple(args)).encode())
    if kwargs:
        hasher.update(str(args).encode())
    return hasher.hexdigest()


def unique_string():
    from random import choice
    from string import ascii_letters, digits

    return "".join([choice(ascii_letters + digits) for n in range(8)])
