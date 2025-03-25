# pytest-doctest-bug

`uv run pytest -v --doctest-modules working.py` works.

`uv run pytest -v --doctest-modules failing.py` fails. 

The only difference is a rounded float in `failing.py`, even though `NUMBER` is enabled.