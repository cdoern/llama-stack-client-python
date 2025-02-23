# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .config_info import ConfigInfo

__all__ = ["ConfigurationInspectResponse"]

ConfigurationInspectResponse: TypeAlias = List[ConfigInfo]
