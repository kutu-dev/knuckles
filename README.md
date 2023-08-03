Partially implemented

- setRating -> Album(Non ID3), Artist(Non ID3)
- scrobble -> Video

Should be implemented

- Refactor "if \* else None" to use oneliners
- POST Support

To think more...

- Normalized variable names in tests
- Checks if the model method can be executed (Avoid server side errors?)
- Singular method for getMusicFolder(s)
- Capitalized model names (E.g. Song vs song)
- Value vs Name in Genre model

Not implemented

- Audio transcoding
- Video
- Open Subsonic Extensions
- CA Certs
- Non ID3

Problematic

- Update the songs in a playlist inside the Playlist class
