# plugins/filter/mapping.py
# =========================
#
# Copying
# -------
#
# Copyright (c) 2023 universe.common authors and contributors.
#
# This file is part of the *universe.common* project.
#
# *universe.common* is a free software project. You can redistribute it and/or
# modify it following the terms of the MIT License.
#
# This software project is distributed *as is*, WITHOUT WARRANTY OF ANY KIND;
# including but not limited to the WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
# PARTICULAR PURPOSE and NONINFRINGEMENT.
#
# You should have received a copy of the MIT License along with
# *universe.common*. If not, see <http://opensource.org/licenses/MIT>.
#
import typing as ty

from collections.abc import Mapping

from jinja2.filters import pass_environment
from jinja2.environment import Environment


def get(_input: Mapping, *key: ty.Hashable, default: ty.Any = None) -> ty.Any:
    """Return the value for *key* if *key* is found in the object, else
    *default*. Multiple keys can be provided and only the value of the first
    matching key is returned.

    If no default is provided and no key matches, ``None`` is returned.


    :param _input: The object to try mapping a key from.
    :type _input: ~collections.abc.Mapping

    :param key: The key to look for into the object. Multiple keys can be
                provided and the value of the first matching key is returned.
    :type key: ~typing.Hashable

    :param default: A value to be returned when no matching key is found.
    :type default: ~typing.Any


    :return: The value is the first key found into the object.
    :rtype: ~typing.Any

    """
    for k in key:
        try:
            return _input[k]
        except KeyError:
            if isinstance(k, str):
                try:
                    return getattr(_input, k)
                except AttributeError:
                    continue
    return default


class FilterModule(object):
    """Map functions to Jinja2 filters."""

    def filters(self):
        return {
            "get": get,
        }
