# pynormalizer
Replace a space or another char in directories and files by underscore or
another char

```
usage: pynormalizer [-h] [-v] [-r] [-o ORIGIN] [-d DEST] target

positional arguments:
  target                file or directory to rename

optional arguments:
  -h, --help            show this help message and exit
  -v, --verbose         print every file or directories renamed
  -r, --recursive       rename files recursively
  -o ORIGIN, --origin ORIGIN
                        The origin char to find. A space by default
  -d DEST, --dest DEST  The dest char to susbtitute. An underscore by default
```
