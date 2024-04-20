# TODO
- [ ] Add missing model properties.
- [ ] Make a `model` class and add the following methods to it:
  - [ ] `_check_api_access()`
  - [ ] `_resource_not_found()`
- [ ] Should `CoverArt` be removed?
- [ ] Determine if video and non-ID3 endpoints will be supported.
  -  [ ] If not the Video and NonID3 checks in the `Song` model should be removed.
- [ ] Implement missing endpoints.
- [ ] Improve error handling:
- [ ] Add the `subsonic.system.check_subsonic_extension()` method.
- [ ] Check and rewrite all docstrings taking care about raising exceptions.
- [ ] Spin up a `MkDocs` documentation.

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
- [x] `getMusicFolders` REMOVE?
- [ ] `getIndexes` **[MISSING]**
- [ ] `getMusicDirectory` **[MISSING]**
- [x] `getGenres`
- [x] `getArtists`
- [x] `getArtist`
- [x] `getAlbum`
- [x] `getSong`
- [ ] `getVideos` **[MISSING]**
- [ ] `getVideoInfo` **[MISSING]**
- [ ] `getArtistInfo` **[MISSING]**
- [x] `getArtistInfo2`
- [ ] `getAlbumInfo` **[MISSING]**
- [x] `getAlbumInfo2`
- [ ] `getSimilarSongs` **[MISSING]**
- [ ] `getSimilarSongs2` **[MISSING]**
- [ ] `getTopSongs` **[MISSING]**

#### Album/song lists
- [ ] `getAlbumList` **[MISSING]**
- [ ] `getAlbumList2` **[MISSING]**
- [ ] `getRandomSongs` **[MISSING]**
- [ ] `getSongsByGenre` **[MISSING]**
- [ ] `getNowPlaying` **[MISSING]**
- [ ] `getStarred` **[MISSING]**
- [ ] `getStarred2` **[MISSING]**

#### Searching
- [x] `search` (Will never be implemented, deprecated)
- [ ] `search2` **[MISSING]**
- [x] `search3`

#### Playlists
- [x] `getPlaylists`
- [x] `getPlaylist`
- [x] `createPlaylist`
- [x] `updatePlaylist`
- [x] `deletePlaylist`

#### Media retrieval
- [x] `stream` *(Only URL handling)*
- [x] `download`
- [x] `hls` *(Only URL handling)*
- [x] `getCaptions`
- [x] `getCoverArt`
- [ ] `getLyrics` **[MISSING]**
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

### Missing model properties
#### Album
- [ ] `recordLabels`
- [ ] `musicBrainzId`
- [ ] `genres`
- [ ] `artists`
- [ ] `displayArtist`
- [ ] `releaseTypes`
- [ ] `moods`
- [ ] `sortName`
- [ ] `originalReleaseDate`
- [ ] `releaseDate`
- [ ] `isCompilation`
- [ ] `discTitles`

#### Artist
- [ ] `musicBrainzId`
- [ ] `sortName`
- [ ] `roles`

#### Song
- [ ] `bmp`
- [ ] `comment`
- [ ] `sortName`
- [ ] `musicBrainzId`
- [ ] `genres`
- [ ] `artists`
- [ ] `displayArtist`
- [ ] `albumArtists`
- [ ] `displayAlbumArtist`
- [ ] `contributors`
- [ ] `displayComposer`
- [ ] `moods`
- [ ] `replayGain`
