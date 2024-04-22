# TODO
- [ ] Implement missing endpoints.
- [ ] indexes mock data should use mock artist data.
- [ ] Add the `subsonic.system.check_subsonic_extension()` method.
- [ ] Improve error handling:
  - [ ] Check and rewrite all docstrings taking care about raising exceptions.
- [ ] Remove unnecessary packages installed in GitHub Actions `tests` job.
- [ ] Spin up a `MkDocs` documentation.
  - [ ] Add the URL in the GitHub page.

## Implementation status
The final objetive of Knuckles to be a fully compatible implementation wrapper around the [OpenSubsonic API Spec](https://opensubsonic.netlify.app/), a superset of the [Subsonic API Spec](https://subsonic.org/pages/api.jsp) that tries to improve and extend the API without breaking changes.

### Requests verbs
- [x] `GET` verb
- [x] `POST` verb

### Response format
- [x] `JSON`
- [ ] `XML`
- [ ] `JSONP`

### Authentication
- [ ] Clear text _(Should be tested globally like the verbs and not in test by itself)_
- [ ] Hex encoded
- [x] Authentication token

### Error handling
- [x] Error codes

### Endpoints
#### System
- [x] `ping`
- [x] `getLicense`
- [x] `getOpenSubsonicExtensions`

#### Browsing
- [x] `getMusicFolders`
- [x] `getIndexes`
- [x] `getMusicDirectory`
- [x] `getGenres`
- [x] `getArtists`
- [x] `getArtist`
- [x] `getAlbum`
- [x] `getSong`
- [ ] `getVideos` **[VIDEO]**
- [ ] `getVideoInfo` **[VIDEO]**
- [ ] `getArtistInfo` **[No ID3]**
- [x] `getArtistInfo2`
- [ ] `getAlbumInfo` **[No ID3]**
- [x] `getAlbumInfo2`
- [ ] `getSimilarSongs` **[No ID3]**
- [x] `getSimilarSongs2`
- [x] `getTopSongs`

#### Album/song lists
- [ ] `getAlbumList` **[No ID3]**
- [ ] `getAlbumList2` **[MISSING]**
- [ ] `getRandomSongs` **[MISSING]**
- [ ] `getSongsByGenre` **[MISSING]**
- [ ] `getNowPlaying` **[MISSING]**
- [ ] `getStarred` **[No ID3]**
- [ ] `getStarred2` **[MISSING]**

#### Searching
- [x] `search` _(Will never be implemented, deprecated)_
- [ ] `search2` **[No ID3]**
- [x] `search3`

#### Playlists
- [x] `getPlaylists`
- [x] `getPlaylist`
- [x] `createPlaylist`
- [x] `updatePlaylist`
- [x] `deletePlaylist`

#### Media retrieval
- [x] `stream` _(Only URL handling)_
- [x] `download`
- [x] `hls` _(Only URL handling)_
- [x] `getCaptions`
- [x] `getCoverArt`
- [x] `getLyrics`
- [x] `getAvatar`

#### Media annotation
- [x] `star`
- [x] `unstar`
- [x] `setRating`
- [x] `scrobble`

#### Sharing
- [x] `getShares`
- [x] `createShare`
- [x] `updateShare`
- [x] `deleteShare`

#### Podcast
- [x] `getPodcasts`
- [x] `getNewestPodcasts`
- [x] `refreshPodcasts`
- [x] `createPodcastChannel`
- [x] `deletePodcastChannel`
- [x] `deletePodcastEpisode`
- [x] `downloadPodcastEpisode`

#### Jukebox
- [x] `jukeboxControl`

#### Internet radio
- [x] `getInternetRadioStations`
- [x] `createInternetRadioStation`
- [x] `updateInternetRadioStation`
- [x] `deleteInternetRadioStation`

#### Chat
- [x] `getChatMessages`
- [x] `addChatMessage`

#### User management
- [x] `getUser`
- [x] `getUsers`
- [x] `createUser`
- [x] `updateUser`
- [x] `deleteUser`
- [x] `changePassword`

#### Bookmarks
- [x] `getBookmarks`
- [x] `createBookmark`
- [x] `deleteBookmark`
- [x] `getPlayQueue`
- [x] `savePlayQueue`

#### Media library scanning
- [x] `getScanStatus`
- [x] `startScan`
