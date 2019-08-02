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
import logging
import sys

from mdm_python_client import __version__, mdm_client

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
        '--question',
        dest="questionId",
        help="The id of an question of the MDM (e.g. que-gra2005-ins1-1.1$)",
        type=str,
        metavar="questionId")
    parser.add_argument(
        '--survey',
        dest="surveyId",
        help="The id of an survey of the MDM (e.g. sur-gra2005-sy1$)",
        type=str,
        metavar="surveyId")
    parser.add_argument(
        '--dataset',
        dest="datasetId",
        help="The id of a dataset of the MDM (e.g. dat-gra2005-ds1$)",
        type=str,
        metavar="dataSetId")
    parser.add_argument(
        '--variable',
        dest="variableId",
        help="The id of a variable of the MDM (e.g. var-gra2005-ds1-astu011a$)",
        type=str,
        metavar="variableId")
    parser.add_argument(
        '--publication',
        dest="publicationId",
        help="The id of a publication of the MDM (e.g. pub-Kratz.2016$)",
        type=str,
        metavar="publicationId")
    parser.add_argument(
        '--concept',
        dest="conceptId",
        help="The id of a concept of the MDM (e.g. con-personality$)",
        type=str,
        metavar="conceptId")
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
        _logger.debug("Fetching study %s", args.studyId)
        study = mdm_client.get_study(args.studyId, args.endpoint)
        if study is not None:
            print("Studientitel:", study.title.de)
            print("DOI:", study.doi)
            print("Veröffentlichungsjahr:", datetime.datetime.strptime(study.release.firstDate,
                                                               '%Y-%m-%dT%H:%M:%S.%f').strftime("%Y"))
        else:
            print("Studie mit id", args.studyId, "nicht gefunden!")
    if args.surveyId is not None:
        _logger.debug("Fetching survey %s", args.surveyId)
        survey = mdm_client.get_survey(args.surveyId, args.endpoint)
        if survey is not None:
            print("Erhebungstitel:", survey.title.de)
        else:
            print("Erhebung mit id ", args.surveyId, "nicht gefunden!")
    if args.instrumentId is not None:
        _logger.debug("Fetching instrument %s", args.instrumentId)
        instrument = mdm_client.get_instrument(args.instrumentId, args.endpoint)
        if instrument is not None:
            print("Instrumenttitel:", instrument.title.de)
        else:
            print("Instrument mit id ", args.instrumentId, "nicht gefunden!")
    if args.questionId is not None:
        _logger.debug("Fetching question %s", args.questionId)
        question = mdm_client.get_question(args.questionId, args.endpoint)
        if question is not None:
            print("Fragetext:", question.questionText.de)
        else:
            print("Frage mit id ", args.questionId, "nicht gefunden!")
    if args.datasetId is not None:
        _logger.debug("Fetching dataset %s", args.datasetId)
        dataset = mdm_client.get_dataset(args.datasetId, args.endpoint)
        if dataset is not None:
            print("Datensatzbeschreibung:", dataset.description.de)
        else:
            print("Datensatz mit id ", args.datasetId, "nicht gefunden!")
    if args.variableId is not None:
        _logger.debug("Fetching variable %s", args.variableId)
        variable = mdm_client.get_variable(args.variableId, args.endpoint)
        if variable is not None:
            print("Variablenlabel:", variable.label.de)
        else:
            print("Variable mit id ", args.variableId, "nicht gefunden!")
    if args.publicationId is not None:
        _logger.debug("Fetching publication %s", args.publicationId)
        publication = mdm_client.get_publication(args.publicationId, args.endpoint)
        if publication is not None:
            print("Publikationstitel:", publication.title)
        else:
            print("Publikation mit id ", args.publicationId, "nicht gefunden!")
    if args.conceptId is not None:
        _logger.debug("Fetching concept %s", args.conceptId)
        concept = mdm_client.get_concept(args.conceptId, args.endpoint)
        if concept is not None:
            print("Konzepttitel:", concept.title.de)
        else:
            print("Konzept mit id ", args.conceptId, "nicht gefunden!")
    _logger.info("MDM REST API Client finished")


def run():
    """Entry point for console_scripts
    """
    main(sys.argv[1:])


if __name__ == "__main__":
    run()
