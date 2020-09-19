"""Classes and constants

Attributes:
    radices: All guaranteed binary encodings
    functions: All guaranteed hash functions

"""
from __future__ import annotations

import base64
import hashlib
from enum import Flag, auto

_encoders = {
    64: base64.b64encode,
    85: base64.b85encode,
}

try:
    import base58
    _encoders[58] = base58.b58encode
except ImportError:
    pass

radices   = set(_encoders.keys())
functions = hashlib.algorithms_guaranteed

# Byte conversions for SS64 parity.
ss64_translation_table = bytes.maketrans(b'+/', b'Ea')


class PropsErrors(Flag):
    NONE              = 0
    INVALID_FUNCTION  = auto()
    INVALID_RADIX     = auto()
    INVALID_SS64      = auto()
    ALL = INVALID_FUNCTION | INVALID_RADIX | INVALID_SS64


class Props(object):

    DEFAULTS = {
        'function': 'sha256',
        'max_chars': 20,
        'radix': 64,
        'use_ss64': True
    }

    @classmethod
    def from_defaults(cls) -> Props:
        return cls(**cls.DEFAULTS)

    def validate(self) -> PropsErrors:
        result = PropsErrors.NONE
        if self.function not in functions:
            result |= PropsErrors.INVALID_FUNCTION
        if self.radix not in radices:
            result |= PropsErrors.INVALID_RADIX
        if self.use_ss64 and self.radix != 64:
            result |= PropsErrors.INVALID_SS64
        return result

    def __init__(self, function:str, max_chars:int, radix:int, use_ss64:bool):
        self.function = function
        self.max_chars = max_chars
        self.radix = radix
        self.use_ss64 = use_ss64
