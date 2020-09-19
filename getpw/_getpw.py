
from typing import Tuple, Union

from hashlib import new
from getpw.models import (
    ss64_translation_table as _ss64tt,
    Props,
    PropsErrors,
    _encoders,
)

_T = Tuple[PropsErrors, Union[bytes, None]]


def encode(data:bytes, props:Props) -> _T:

    errors = props.validate()
    if ~errors is not PropsErrors.ALL:
        return (errors, None)

    b = _encoders[props.radix](new(props.function, data).digest())
    if props.use_ss64:
        b = b.translate(_ss64tt)[:-1]
    b = b[:props.max_chars]

    return (PropsErrors.NONE, b)


def getpw(master:str, site:str, props:Props) -> _T:
    s = f'{master}:{site}'.encode()
    return encode(s, props)


def get_verification_code(master:str) -> bytes:
    s = f':{master}:'.encode()
    return encode(s, Props.from_defaults())[1]
