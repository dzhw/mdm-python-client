.. image:: https://img.shields.io/badge/python-2.7-blue

.. image:: https://travis-ci.org/dzhw/mdm-python-client.svg?branch=master
    :target: https://travis-ci.org/dzhw/mdm-python-client

.. image:: https://codecov.io/gh/dzhw/mdm-python-client/branch/master/graph/badge.svg
  :target: https://codecov.io/gh/dzhw/mdm-python-client

.. image:: https://readthedocs.org/projects/mdm-python-client/badge/?version=latest
    :target: https://mdm-python-client.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

=================
MDM Python Client
=================

This project contains a REST API client for `MDM <https://metadata.fdz.dzhw.eu>`_  (`Metadatamanagement System <https://github.com/dzhw/metadatamanagement>`_) of the Research Data Center of the DZHW.

Description
===========

The client can be used to retrieve metadata from the public `REST API <https://metadata.fdz.dzhw.eu/swagger-ui.html>`_ of the MDM_. Currently it uses a cache which gets stale after 24 hours. The module currently depends on Python 2.7 cause it is developed for our CMS which is currently based on this Python version.

You can install the latest version of this client with

.. code:: bash

    pip install git+https://github.com/dzhw/mdm-python-client.git

This will also install a command line version which you can run with

.. code:: bash

    mdm --help

The following snippet demonstrates how to use the client programmatically:

.. code:: python

    from mdm_python_client.mdm_client import get_study

    def test_get_study():
        study = get_study("stu-gra2005$")
        if study is not None:
            print("Studientitel:", study.title.de)
            print("DOI:", study.doi)
            print("Veröffentlichungsjahr:", datetime.datetime.strptime(study.release.firstDate,
                                                               '%Y-%m-%dT%H:%M:%S.%f').strftime("%Y"))
        else:
            print("Studie mit id", args.studyId, "nicht gefunden!")

Note
====

This project has been set up using PyScaffold 2.5.11. For details and usage
information on PyScaffold see http://pyscaffold.readthedocs.org/.
