import argparse
from pathlib import Path
from keyboard_generator.renderer import KeyboardRenderer
from keyboard_generator.output_writer import OutputWriter


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="Input JSON file path", type=Path)
    parser.add_argument("--output", help="Output file path", type=Path)
    parser.add_argument("--format", help="Output file format", type=str, choices=("json", "scad"), default="scad")
    return parser.parse_args()


def main():
    args = parse_args()
    output_writer = OutputWriter(args.format)
    if args.output is not None:
        output_writer.set_path(args.output)
    
    renderer = KeyboardRenderer.load_from_kle(args.input)
    keyboard = renderer.render()
    output_writer.write(keyboard)


if __name__ == "__main__":
    main()
