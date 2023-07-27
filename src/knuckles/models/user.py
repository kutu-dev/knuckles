class User:
    def __init__(
        self,
        username: str,
        email: str,
        scrobblingEnabled: bool = False,
        adminRole: bool = False,
        settingsRole: bool = False,
        downloadRole: bool = False,
        uploadRole: bool = False,
        playlistRole: bool = False,
        coverArtRole: bool = False,
        commentRole: bool = False,
        podcastRole: bool = False,
        streamRole: bool = False,
        jukeboxRole: bool = False,
        shareRole: bool = False,
        videoConversionRole: bool = False,
    ) -> None:
        self.username = username
        self.email = email
        self.scrobbling_enabled = scrobblingEnabled
        self.admin_role = adminRole
        self.settings_role = settingsRole
        self.download_role = downloadRole
        self.upload_role = uploadRole
        self.playlist_role = playlistRole
        self.cover_art_role = coverArtRole
        self.comment_role = commentRole
        self.podcast_role = podcastRole
        self.stream_role = streamRole
        self.jukebox_role = jukeboxRole
        self.share_role = shareRole
        self.video_conversion_role = videoConversionRole
