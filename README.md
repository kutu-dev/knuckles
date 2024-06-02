# Knuckles
> A [OpenSubsonic](https://opensubsonic.netlify.app/) API wrapper for Python 3.11.0+.

## Compatiblity
Knuckles **only** works with servers compatible with the REST API version 1.4.0 onwards (Subsonic 4.2+).
It follows strictly the [OpenSubsonic API Spec](https://opensubsonic.netlify.app/docs/opensubsonic-api/), being fully retro-compatible with the original [Subsonic API](https://subsonic.org/pages/api.jsp).

## Getting Started

### Make It Available
First install the package:

```sh title="Command line"
python3 -m pip install knuckles
```

Or add it to your project:

```toml title="pyproject.toml"
project = [
    "knuckles>=1.0.0"
]
```

### Using It

```python3 title="__main__.py"
import knuckles

server = knuckles.subsonic(
    # Adding https:// is done automatically,
    # /rest should never be added to the URL
    url = "example.com",
    user = "kutu",
    password = "caisopea",
    client = "knuckles client"
)

ping = server.ping()

# Print the supported version of the OpenSubsonic REST API
print(ping.version)
```

### Learning More
To start making more complex interactions with the API make use of [the reference](https://kutu-dev.github.io/knuckles/reference/Api/). Enjoy coding and good luck!

## Acknowledgements
Created with :heart: by [Jorge "Kutu" Dobón Blanco](https://dobon.dev).
