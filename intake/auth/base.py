

class BaseAuth(object):
    """Base class for authorization

    This basic class allows all access.
    """

    def __init__(self, *args):
        self.args = args

    def allow_connect(self, header):
        """Is the requests header given allowed to talk to the server

        Parameters
        ----------
        header: dict
            The HTTP header from the incoming request
        """
        return True

    def allow_access(self, header, source):
        """Is the given HTTP header allowed to access given data source

        Parameters
        ----------
        header: dict
            The HTTP header from the incoming request
        source: CatalogEntry
            The data source the user wants to access.
        """
        return True

    def get_case_insensitive(self, dictionary, key, default=None):
        """Case-insensitive search of a dictionary for key.

        Returns the value if key match is found, otherwise default.
        """
        lower_key = key.lower()
        for k, v in dictionary.items():
            if lower_key == k.lower():
                return v
        else:
            return default


class BaseClientAuth(object):
    """Base class for client-side setting of authorization headers

    This basic class adds no headers to remote catalog reqests
    """

    def __init__(self, *args):
        self.args = args

    def get_headers(self):
        """Returns a dictionary of HTTP headers to add to the remote catalog request.
        """
        return {}
