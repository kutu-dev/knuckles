class ScanStatus:
    """Representation of all the data related to the status
    of a library scan in Subsonic.
    """

    def __init__(self, scanning: bool, count: int) -> None:
        """Representation of all the data related to the status
        of a library scan in Subsonic.

        :param scanning: The status of the scan.
        :type scanning: bool
        :param count: Scanned item count.
        :type count: int
        """

        self.scanning: bool = scanning
        self.count: int = count
