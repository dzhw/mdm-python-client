#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This is a skeleton file that can serve as a starting point for a Python
console script. To run this script uncomment the following line in the
entry_points section in setup.cfg:

    console_scripts =
     mdm = mdm_python_client.main:run

Then run `python setup.py install` which will install the command `fibonacci`
inside your current environment.
Besides console scripts, the header (i.e. until _logger...) of this file can
also be used as template for Python modules.
"""
from __future__ import division, print_function, absolute_import

import argparse
import datetime
import sys
import logging

from mdm_python_client import __version__
from mdm_python_client.mdm_client import get_study, get_instrument

__author__ = "René Reitmann"
__copyright__ = "DZHW GmbH"
__license__ = "AGPL-3.0"

_logger = logging.getLogger(__name__)


def parse_args(args):
    """Parse command line parameters

    Args:
      args ([str]): command line parameters as list of strings

    Returns:
      :obj:`argparse.Namespace`: command line parameters namespace
    """
    parser = argparse.ArgumentParser(
        description="Just a MDM Rest API Client")
    parser.add_argument(
        '--version',
        action='version',
        version='mdm-python-client {ver}'.format(ver=__version__))
    parser.add_argument(
        '--study',
        dest="studyId",
        help="The id of a study of the MDM (e.g. stu-gra2005$)",
        type=str,
        metavar="studyId")
    parser.add_argument(
        '--instrument',
        dest="instrumentId",
        help="The id of an instrument of the MDM (e.g. ins-gra2005-ins1$)",
        type=str,
        metavar="instrumentId")
    parser.add_argument(
        '--endpoint',
        dest="endpoint",
        help="The API endpoint of the MDM (e.g. https://metadata.fdz.dzhw.eu/api)",
        type=str,
        metavar="url",
        default="https://metadata.fdz.dzhw.eu/api")
    parser.add_argument(
        '-v',
        '--verbose',
        dest="loglevel",
        help="set loglevel to INFO",
        action='store_const',
        const=logging.INFO)
    parser.add_argument(
        '-vv',
        '--very-verbose',
        dest="loglevel",
        help="set loglevel to DEBUG",
        action='store_const',
        const=logging.DEBUG)
    return parser.parse_args(args)


def setup_logging(loglevel):
    """Setup basic logging

    Args:
      loglevel (int): minimum loglevel for emitting messages
    """
    logformat = "[%(asctime)s] %(levelname)s:%(name)s:%(message)s"
    logging.basicConfig(level=loglevel, stream=sys.stdout,
                        format=logformat, datefmt="%Y-%m-%d %H:%M:%S")


def main(args):
    """Main entry point allowing external calls

    Args:
      args ([str]): command line parameter list
    """
    args = parse_args(args)
    setup_logging(args.loglevel)
    _logger.debug("Starting MDM Rest API Client...")
    if args.studyId is not None:
        _logger.debug("Fetching study", args.studyId)
        study = get_study(args.studyId, args.endpoint)
        if study is not None:
            print("Studientitel:", study.title.de)
            print("DOI:", study.doi)
            print("Veröffentlichungsjahr:", datetime.datetime.strptime(study.release.firstDate,
                                                               '%Y-%m-%dT%H:%M:%S.%f').strftime("%Y"))
        else:
            print("Studie mit id", args.studyId, "nicht gefunden!")
    if args.instrumentId is not None:
        _logger.debug("Fetching instrument", args.instrumentId)
        instrument = get_instrument(args.instrumentId, args.endpoint)
        if instrument is not None:
            print("Instrumenttitel:", instrument.title.de)
        else:
            print("Instrument mit id ", args.instrumentId, "nicht gefunden!")
    _logger.info("MDM REST API Client finished")


def run():
    """Entry point for console_scripts
    """
    main(sys.argv[1:])


if __name__ == "__main__":
    run()
