# plugins/filter/sequence.py
# ==========================
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
from collections.abc import Sequence


def union_when(_input: Sequence, predicate: bool, other: Sequence) -> list:
    """Return a unique list of all the elements from two lists if the predicate
    is true. Otherwise, return the first list.

    .. warning::
        Duplicate entries are removed from each sequence object when merged
        otherwise, the input sequence is returned as is.


    :param _input: The original list to merge with.
    :type _input: ~collections.abc.Sequence

    :param predicate: A boolean value to decide whether both lists must be
                      merged.
    :type predicate: bool

    :param other: The other list to be merged.
    :type other: ~collections.abc.Sequence


    :return: A unique list of all the elements from two lists when ``predicate``
             is ``True``, the first list otherwise.
    :rtype: list

    """
    if predicate:
        return list(set(_input) | set(other))
    return _input


class FilterModule(object):
    """Map functions to Jinja2 filters."""

    def filters(self):
        return {
            "union_when": union_when,
        }
