from .structures import ShellLink


def analyse(file_path: str) -> None:
    with open(file_path, "rb") as f:
        file_content = f.read()

    lnk = ShellLink.parse(file_content)
    print(lnk)
