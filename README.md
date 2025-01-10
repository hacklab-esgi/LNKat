# LNKat

```
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

```

The goal to develop LNKat is to get a versatil tool which can be used for :  
- Malware triage : read and analyse LNK files  
- Offensive tactics : generate malicious `.lnk` payloads  

And it would be create to provide an API to be integred with other tools.

## Why

Couldn't find any viable tool on Linux to generate malicious LNK files.  
And I wanna play with the `construct` library and the `rye` tooling.

The generator capability would be useful to build any kind of LNK-related attacks.

## Installation

The recommanded way is to use `pipx` :
```sh
pipx install git+https://github.com/hacklab-esgi/LNKat
```

## Usage

Once installed on your system, use the following command to analyse:
```sh
lnkat <file_path>
```

### Example
Test with our samples :  
```sh
lnkat samples/calc.exe.lnk
```

## Roadmap

First milestone for parsing ability :
- [x] Read `SHELL_LINK_HEADER`
- [ ] Read `LINKTARGET_IDLIST`
    - [x] Documented structures
    - [ ] Undocumented structures
- [ ] Read `LINKINFO`
- [ ] Read `STRING_DATA`
- [ ] Read `EXTRA_DATA`
- [ ] Provide an initial clean output

Second milestone for generation ability:
- [ ] Generate a file with "default" values
- [ ] Custom target path
- [ ] Custom icon path
- [ ] More to come

Third milestone for QoL :
- [ ] Python API to use LNKat as a library
- [ ] Generate HTML reports
- [ ] Modify existing file as `cat input.lnk | lnkat.py > output.lnk`
- [ ] Configuration files
- [ ] More to come

## Contributing

This project is using [`rye`](https://rye.astral.sh/) for project and package management.

All the parsing logic **must** be written inside `Construct`'s structs, mostly using the `Adapter` class.

Please review the contribution guide [`CONTRIBUTION.md`](.github/CONTRIBUTION.md).

## License

Distributed under the MIT License. See [`LICENSE`](LICENSE) for more information.

## Credits

- https://github.com/strayge/pylnk : For inspiration and undocumented structures
