import json
from pathlib import Path
from keyboard_generator import pykle_serial, math
from keyboard_generator.structures import RenderedKey, RenderedKeyboard


class KeyboardRenderer:
    def __init__(self, *, unit_size: float = 19.05):
        self._keyboard: pykle_serial.Keyboard | None = None
        self._unit_size = unit_size

    @classmethod
    def load_from_kle(cls, file_path: Path, *_, **kwargs) -> "KeyboardRenderer":
        self = cls(**kwargs)
        with file_path.open("r") as file:
            keyboard_data = json.load(file)
        self._keyboard = pykle_serial.deserialize(keyboard_data)
        return self

    def render(self) -> RenderedKeyboard:
        if not self._keyboard:
            raise ValueError("Keyboard isn't loaded.")
        keys = list(map(self._render_key, self._keyboard.keys))
        return RenderedKeyboard(keys=keys)
        
    def _render_key(self, key: pykle_serial.Key) -> RenderedKey:
        half_w, half_h = key.width / 2., key.height / 2.
        x0, y0 = key.x - key.rotation_x + half_w, key.y - key.rotation_y + half_h
        x, y = math.rotate(x0, y0, key.rotation_angle)
        x, y = x + key.rotation_x, y + key.rotation_y

        return RenderedKey(
            x=x*self._unit_size,
            y=y*self._unit_size,
            width=key.width*self._unit_size,
            height=key.height*self._unit_size,
            rotation_angle=key.rotation_angle,
        )
        