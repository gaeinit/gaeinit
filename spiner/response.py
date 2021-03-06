# -*- coding: utf-8 -*-
from json import dumps as json_dumps
from . import env

_intent = None
_separators = None
if env.is_debug_mode():
    _intent = 4
    _separators = (',', ': ')


def json(response, data, code=200):
    response.content_type = 'application/json'
    response.status = code
    response.write(json_dumps(
        data, sort_keys=True, indent=_intent, separators=_separators))
