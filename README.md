# getpw.py

> **AKA** 'How many more years will I be forced to rewrite this before I decide to stop deleting the repository'.py

Generate (repeatable) passwords given a site and a master passphrase.

## Requirements

- Click
- Pyperclip
    - xclip (_*nix only_)

Optional:

- Base58 (for b58encode support)

## Installation

```
pip install "git+https://github.com/aislingdailey/getpw"
```

Append `#egg=getpw[Base58]` to enable Base 58 encoding.

## Usage

The following encodings are supported:

- b58 (**optional**) is good for readable passwords;
- b64 (**default**) is good for general use; and
- b85 is good for passwords requiring special characters.

By default: all passwords are 20 characters long and compatible with the [SS64 password generator](https://ss64.com/passwords).

See `getpw --help` for more info.
