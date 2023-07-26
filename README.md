```python
subsonic: Subsonic = Subsonic('user', 'password', ')
subsonic.system.ping()
```

- Subsonic
  - System
  - Media Annotations
  - Jukebox
  - Chat

## Approach #1

- Subsonic
  - Params y make request
  - Chat(request: callback)

## Approach #2

- Subsonic _(API Publica)_
- API (Subsonic API)
- Chat

## Approach #3

```python
auth: Auth = Auth()
subsonic: Subsonic = Subsonic(auth)
subsonic.system.ping()
```
