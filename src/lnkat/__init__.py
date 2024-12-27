import sys

from . import analyzer


ASCII_ART = r"""
  ,-.       _,---._ __  / \
 /  )    .-'       `./ /   \
(  (   ,'            `/    /|
 \  `-"             \'\   / |
  `.              ,  \ \ /  |
   /`.          ,'-`----Y   |
  (            ;        |   '
  |  ,-.    ,-'         |  /
  |  | (   |      LNKat | /
  )  |  \  `.___________|/
  `--'   `--'

"""


def main() -> int:
    print(ASCII_ART)

    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <FILE>")
        return

    analyzer.analyse(sys.argv[1])
    return 0
