"""No-op telemetry decorators.

This fork has all telemetry removed: no events, prompts, code, screenshots,
scene data, or trajectory data are recorded or sent anywhere. The decorators
are kept as identity pass-throughs so tool definitions are unchanged.
"""
from __future__ import annotations

import functools
import inspect
from typing import Any, Callable


def _passthrough(func: Callable) -> Callable:
    if inspect.iscoroutinefunction(func):
        @functools.wraps(func)
        async def async_wrapper(*args: Any, **kwargs: Any) -> Any:
            return await func(*args, **kwargs)
        return async_wrapper

    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        return func(*args, **kwargs)
    return wrapper


def telemetry_tool(tool_name: str):
    """Identity decorator - telemetry removed in this fork."""
    def decorator(func: Callable) -> Callable:
        return _passthrough(func)
    return decorator


def rich_telemetry_tool(tool_name: str, capture_code: bool = False):
    """Identity decorator - telemetry removed in this fork."""
    def decorator(func: Callable) -> Callable:
        return _passthrough(func)
    return decorator


def trajectory_tool(tool_name: str, capture_code: bool = False):
    """Identity decorator - telemetry removed in this fork."""
    def decorator(func: Callable) -> Callable:
        return _passthrough(func)
    return decorator


async def _consent_note(args, kwargs) -> str:
    return ""


def _record_observe_step(*args: Any, **kwargs: Any) -> None:
    """No-op - telemetry removed in this fork."""
    return None
