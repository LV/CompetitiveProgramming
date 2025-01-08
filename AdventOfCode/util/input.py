import pathlib

def get_input_string(year: int, day: int) -> str:
    file_path: pathlib.Path = pathlib.Path(__file__).parent.parent.resolve() / "inputs" / f"{year}" / f"day{day:02}.txt"
    return file_path.read_text(encoding="utf-8")
