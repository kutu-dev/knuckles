# Contributing
Any contribution is welcomed, don't be ashamed to send them!

## Reporting
If you see any undesired behaviour, mismatches with the [OpenSubsonic API Spec](https://opensubsonic.netlify.app/) or any sort of bug, please report them at the [issue tracker](https://github.com/kutu-dev/knuckles/issues).

## Development
### The Toolchain
To start making development contribution you will need the `just` command (installation info at [its manual](https://just.systems/man/en/chapter_4.html)) and Python 3.11.0 (you can set it with [pyenv](https://github.com/pyenv/pyenv)).

Then you should be able to spin up the development environment:
```sh title="Command Line"
just setup
```
You can now run the test suit, check if you will the pass the CI check (and fix everything that can be done automatically) and spin up a docs instance with ease:
```sh title="Command Line"
just test
just check
just docs
```

A git pre-commit hook that will run `just check` at every commit and block it if something is wrong can be installed with:
```sh title="Command Line"
just install-hook
```

You can uninstall it with:
```sh title="Command Line"
just uninstall-hook
```

See more recipes with:
```sh title="Command Line"
just help
```

### The Project
The project works around the [OpenSubsonic API Spec](https://opensubsonic.netlify.app/), with models (at `src/knuckles/_models`) that tries to match the [different responses](https://opensubsonic.netlify.app/docs/responses/) request can make.

The user access the API with the `Subsonic` object inside of it there are objects that acts as categories that roughly resembles the [categories in the spec](https://opensubsonic.netlify.app/categories/).

Everything should be private using the leading underscore convention and exposed the public parts of the package with the `__init__.py` file using the `__all__` variable.

!!! Warning

    Making exceptions, methods or extra behaviour to support functionalities or bugs caused by non compliant server is not planned, nonetheless new generic systems to catch and avoid crashing in this situations are welcomed to be contributed.

### Notes
Technical notes about unconventional decisions in the project:

- Some parts of the CI with GitHub Actions uses the `24.04` version of Ubuntu instead of the `latest` tag (currently at `22.04`), this is due to the `just` command only being available in this version onwards. This is also the reason why this jobs uses Python 3.11.9 as it has a more limited range of installable version with the `actions/setup-python` action.
- Unfortunately due to limitations with [`mkdocstrings-python`](https://mkdocstrings.github.io/python/usage/configuration/docstrings/), when documenting the attributes of a class (like with all the models) the times can be determined at runtime and needs to be retyped in the docstring.
