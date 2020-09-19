__all__ = [
    'get_version'
]

from typing import Tuple as __Tuple

from getpw.__version__ import __author__
from getpw.__version__ import __author_email__
from getpw.__version__ import __license__
from getpw.__version__ import __version__
from getpw.__version__ import VERSION as __VERSION

from getpw import models
from getpw._getpw import getpw
from getpw._getpw import get_verification_code



def get_version() -> __Tuple[int]:
    return __VERSION
