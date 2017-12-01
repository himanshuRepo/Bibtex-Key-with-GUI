#!/usr/bin/env python

"""
Code for generating the bibtex key from Google Scholar for the list of papers, whose names are stored
    in the excel sheet.

Referred: https://github.com/venthur/gscholar
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
Library to query Google Scholar.

Call the method query with a string which contains the full search
string. Query will return a list of citations.
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
"""

try:
    # python 2
    from urllib2 import Request, urlopen, quote
except ImportError:
    # python 3
    from urllib.request import Request, urlopen, quote

try:
    # python 2
    from htmlentitydefs import name2codepoint
except ImportError:
    # python 3
    from html.entities import name2codepoint


import logging
import contextlib



GOOGLE_SCHOLAR_URL = "https://scholar.google.com"
HEADERS = {'User-Agent': 'Mozilla/5.0'}

FORMAT_BIBTEX = 4
FORMAT_ENDNOTE = 3
FORMAT_REFMAN = 2
FORMAT_WENXIANWANG = 5


logger = logging.getLogger(__name__)


def query(searchstr, outformat=FORMAT_BIBTEX, allresults=False):
    """Query google scholar.

    This method queries google scholar and returns a list of citations.

    Parameters
    ----------
    searchstr : str
        the query
    outformat : int, optional
        the output format of the citations. Default is bibtex.
    allresults : bool, optional
        return all results or only the first (i.e. best one)

    Returns
    -------
    result : list of strings
        the list with citations

    """
    logger.debug("Query: {sstring}".format(sstring=searchstr))
    searchstr = '/scholar?q='+quote(searchstr)
    url = GOOGLE_SCHOLAR_URL + searchstr
    header = HEADERS
    header['Cookie'] = "GSP=CF=%d" % outformat
    request = Request(url, headers=header)
    with contextlib.closing(urlopen(request)) as response:
        # response = urlopen(request)
        html = response.read()
        html = html.decode('utf8')

        # grab the links
        tmp = get_links(html, outformat)


        # follow the bibtex links to get the bibtex entries
        result = list()
        if not allresults:
            tmp = tmp[:1]
        for link in tmp:
            url = GOOGLE_SCHOLAR_URL+link
            request = Request(url, headers=header)
            with contextlib.closing(urlopen(request)) as response:
                # response = urlopen(request)
                bib = response.read()
                bib = bib.decode('utf8')
            result.append(bib)
    return result

