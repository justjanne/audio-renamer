# Audio-Renamer

## Usage 

```
usage: audio-renamer.py [-h] [--dry-run] folders [folders ...]

positional arguments:
  folders     Folders to run the task on

optional arguments:
  -h, --help  show this help message and exit
  --dry-run   Simulate renames
```

## Format

The hardcoded default format in Amarok syntax is

```
%albumartist%/%album%{ (%originalyear%)}/{{%disc%-}%track%. }%title%.%extension%
```
