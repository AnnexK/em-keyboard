import math


def rotate(x: float, y: float, rot: float) -> tuple[float, float]: 
    rot_r = math.radians(rot)
    x2 = x * math.cos(rot_r) - y * math.sin(rot_r)
    y2 = x * math.sin(rot_r) + y * math.cos(rot_r)
    return x2, y2
