from dataclasses import dataclass


@dataclass
class RenderedKey:
    x: float
    y: float
    width: float
    height: float
    rotation_angle: float


@dataclass
class RenderedKeyboard:
    keys: list[RenderedKey]
