# TODO
- [ ] Check and rewrite all docstrings taking care about raising exceptions.
- [ ] Spin up a `MkDocs` documentation.
  - [ ] Add the URL in the GitHub page.
- [ ] Decide if use `Subsonic/OpenSubsonic`, `(Open)Subsonic` or `OpenSubsonic`.

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
- [x] `getVideos`
- [x] `getVideoInfo`
- [x] `getArtistInfo`
- [x] `getArtistInfo2`
- [x] `getAlbumInfo`
- [x] `getAlbumInfo2`
- [x] `getSimilarSongs`
- [x] `getSimilarSongs2`
- [x] `getTopSongs`

#### Album/song lists
- [x] `getAlbumList`
- [x] `getAlbumList2`
- [x] `getRandomSongs`
- [x] `getSongsByGenre`
- [x] `getNowPlaying`
- [x] `getStarred`
- [x] `getStarred2`

#### Searching
- [x] `search` _(Will never be implemented, deprecated)_
- [x] `search2`
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
