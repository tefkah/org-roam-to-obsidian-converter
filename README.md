# Org Roam to Obsidian Converter

Small Python CLI tool to convert org-roam `.org` (and other org files) to Obsidian `.md` files

## Usage

```
usage: converter.py [-h] [-d] [-o OUTPUT_DIRECTORY] [-r] PATH

Convert individual org files or directory to Obsidian.md format

positional arguments:
  PATH                  path to the file or directory

optional arguments:
  -h, --help            show this help message and exit
  -d, --directory       convert all the org-files in a specific directory
                        instead of a single file
  -o OUTPUT_DIRECTORY, --output_directory OUTPUT_DIRECTORY
                        directory where to place the new file(s), defaults to
                        same directory as the file
  -r, --recursive       recursively convert all files in a directory, requires
                        -d
```

## Description

Currently very limited.
Is able to convert single files or whole directories to `.md` files.

### Functionality

- Converts `.org` links to `.md` links.
- Converts `*` `.org` headlines to `#` `.md` headlines. 
- Convert `#+roam_tags` to normal hashtags
- Gets rid of all org comments (needs to be refined)

## TODO
- Converse conversion, so two databases could be kept in sync
- (https://github.com/org-roam/org-roam-bibtex)[orb] `cite:` links conversion (not sure how to do this
- Convert latex headers etc.
- Deal with `[[roam:]]` links
- Make recursive conversion retain file structure
- ...
