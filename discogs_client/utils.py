from __future__ import unicode_literals

from datetime import datetime
import re

try:
    # python2
    from urllib2 import quote
    to_str = unicode
except ImportError:
    # python3
    from urllib.parse import quote
    to_str = str


def parse_timestamp(timestamp):
    """Convert an ISO 8601 timestamp into a datetime."""

    #sometimes it seems discogs does send the TimeZone: ignore it
    #by removing it
    ts = timestamp
    search_obj = re.search("\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}", ts)
    if search_obj:
        ts = search_obj.group()

    return datetime.strptime(ts, '%Y-%m-%dT%H:%M:%S')


def update_qs(url, params):
    """A not-very-intelligent function to glom parameters onto a query string."""
    joined_qs = '&'.join('='.join((str(k), quote(to_str(v).encode('utf8'))))
                         for k, v in params.items())
    separator = '&' if '?' in url else '?'
    return url + separator + joined_qs


def omit_none(dict_):
    """Removes any key from a dict that has a value of None."""
    return dict((k, v) for k, v in dict_.items() if v is not None)
