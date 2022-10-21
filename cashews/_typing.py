from datetime import timedelta
from typing import Any, Callable, Dict, Optional, Tuple, Union

TTL = Union[int, str, timedelta, Callable[[Any], Union[int, str, timedelta, None]]]
CallableCacheCondition = Callable[[Any, Tuple, Dict, Optional[str]], bool]
CacheCondition = Union[CallableCacheCondition, str, None]
