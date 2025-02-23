# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
#from typing_extensions import TypeAlias
from .._models import BaseModel
from typing import Any, Dict

#from .config_register import ConfigRegister

__all__ = ["ConfigurationRegisterResponse"]

class ConfigurationRegisterResponse(BaseModel):
    data: List[Dict[str, Any]]

