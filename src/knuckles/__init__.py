from .subsonic import Subsonic
from .models import *

SUBSONIC_URL = "http://demo.navidrome.org"
USER = "demo"
PASSWORD = "demo"

foo = Subsonic(SUBSONIC_URL, USER, PASSWORD, "TEST")
bar = foo.get_song("44942f3661c50b698f7b6ee595f390d8")
bar.title = "LLLOOOOOOLLLL"
print(bar)
print(bar.generate(foo)())
