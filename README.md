# pynormalizer
Normalize filenames replacing conflictive characters

## Install
```sh
sudo pip3 install https://github.com/alex-left/pynormalizer/archive/v0.2.tar.gz
```

## Usage

```
usage: pynormalizer [-h] [-v] [-r] [-o ORIGIN] [-d DEST] target [target ...]

positional arguments:
  target                file or directory to rename

optional arguments:
  -h, --help            show this help message and exit
  -v, --verbose         print every file or directories renamed
  -r, --recursive       rename files recursively
  -o ORIGIN, --origin ORIGIN
                        The origin char to find. Common undesiderable chars by
                        default
  -d DEST, --dest DEST  The destination char to susbtitute. An underscore by default
```
