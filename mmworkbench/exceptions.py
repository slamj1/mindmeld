# -*- coding: utf-8 -*-
"""This module contains exceptions used by the mmworkbench package."""


class BadWorkbenchRequestError(Exception):
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        obj = dict(self.payload or ())
        obj['error'] = self.message
        return obj


class ClassifierLoadError(Exception):
    pass
