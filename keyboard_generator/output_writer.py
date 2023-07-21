import json
import typing
import sys
from pathlib import Path
from keyboard_generator.structures import RenderedKeyboard


class OutputWriter:
    def __init__(self, output_type: str = "scad") -> None:
        self._path: Path | None = None
        match output_type:
            case "scad":
                self._write_func = self._write_scad
            case "json":
                self._write_func = self._write_json

    def set_path(self, path: Path):
        self._path = path

    def write(self, keyboard: RenderedKeyboard):
        if self._path is None:
            self._write_func(sys.stdout, keyboard)
            return

        with self._path.open("w") as fd:
            self._write_func(fd, keyboard)

    def _write_json(self, fd: typing.TextIO, keyboard: RenderedKeyboard):
        json.dump({
            "keys": [
                {
                    "x": key.x,
                    "y": key.y,
                    "rot": key.rotation_angle
                }
                for key in keyboard.keys
            ]
        }, fd)

    def _write_scad(self, fd: typing.TextIO, keyboard: RenderedKeyboard):
        fd.write("keys = [\n")
        fd.write(
            ",\n".join(
                f"    [{k.x}, {k.y}, {k.rotation_angle}]"
                for k in keyboard.keys
            )
        )
        fd.write("\n];\n")
