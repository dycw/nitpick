from __future__ import annotations

from dycw_nitpick import __version__


def test_main() -> None:
    assert isinstance(__version__, str)
