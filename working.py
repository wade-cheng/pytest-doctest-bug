import copy
import itertools
from collections.abc import Iterable
import math


class DistsAngle:
    """
    immutable. represents an angle and some points at given distances to that angle

    >>> d = DistsAngle(range(4), math.pi / 4)
    >>> for x, y in d.get_offsets(0):
    ...     print(f"({x},{y})")
    ...
    (0.0,0.0)
    (0.707,0.707)
    (1.414,1.414)
    (2.121,2.121)

    >>> d = DistsAngle(itertools.count(step=1), math.pi / 8)
    >>> for x, y in d.get_offsets(0):
    ...     print(f"({x},{y})")
    ...     if abs(x) > 20 or abs(y) > 20:
    ...         break
    ...
    (0.0,0.0)
    (0.9238795325112867,0.3826834323650898)
    (1.8477590650225735,0.7653668647301796)
    (2.77163859753386,1.1480502970952693)
    ...
    (20.325349715248308,8.419035512031975)
    """

    def __init__(self, distances: Iterable[float], angle: float):
        """locs must be iterable, angle in radians"""
        self.__distances = distances
        self.__angle = angle

    def get_distances(self):
        return self.__distances

    def get_angle(self):
        return self.__angle

    def get_offsets(self, angle: float) -> Iterable[tuple[float, float]]:
        """angle in radians is the offset angle"""
        return (
            self.get_point(d, self.__angle, angle) for d in copy.copy(self.__distances)
        )

    def get_point(
        self, distance: float, base_angle: float, offset_angle: float
    ) -> tuple[float, float]:
        """angle in radians"""
        angle = base_angle - offset_angle
        return (distance * math.cos(angle), distance * math.sin(angle))
