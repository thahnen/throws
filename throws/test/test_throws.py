#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import Optional
from throws import throws, ListEmptyException, InvalidRaisedException


@throws([])
def testEmptyThrowsList():
    """
    1. Testcase: empty list provided to decorator, should fail always with ListEmptyException
    """
    pass


@throws([ValueError, AssertionError])
def testIncompleteThrowsList(param: Optional[bool]):
    """
    2. Testcase: incomplete list provided to decorator, should fail when param is None
    """
    if param == True:
        raise ValueError
    elif param == False:
        raise AssertionError
    else:
        raise IOError


@throws([ValueError, AssertionError])
def testCompleteThrowsList(param: bool):
    """
    3. Testcase: complete list provided to decorater, should not fail even when param is None
    """
    if param:
        raise ValueError
    else:
        raise AssertionError


if __name__ == "__main__":
    # 1. Testcase: testEmptyThrowsList -> ListEmptyException
    try:
        testEmptyThrowsList()
        ran1 = True
    except ListEmptyException:
        ran1 = False
    
    assert(ran1 == False)
    
    # 2. Testcase: testIncompleteThrowsList ~> InvalidRaisedException
    try:
        testIncompleteThrowsList(True)
        ran2 = True
    except ValueError:
        ran2 = False

    assert(ran2 == False)

    try:
        testIncompleteThrowsList(False)
        ran3 = True
    except AssertionError:
        ran3 = False

    assert(ran3 == False)

    try:
        testIncompleteThrowsList(None)
        ran4 = True
    except InvalidRaisedException:
        ran4 = False
    
    assert(ran4 == False)

    # 3. Testcase: testCompleteThrowsList -> None
    try:
        testCompleteThrowsList(True)
        ran5 = True
    except ValueError:
        ran5 = False

    assert(ran5 == False)

    try:
        testCompleteThrowsList(False)
        ran6 = True
    except AssertionError:
        ran6 = False

    assert(ran6 == False)

    try:
        testCompleteThrowsList(None)
        ran7 = True
    except AssertionError:
        ran7 = False

    assert(ran7 == False)
