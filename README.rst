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

The client can be used to retrieve metadata from the public `REST API <https://metadata.fdz.dzhw.eu/swagger-ui.html>`_ of the MDM_. Currently it uses a cache which gets stale after 24 hours.

You can install the latest version of this client with

.. code:: bash

    pip install git+https://github.com/dzhw/mdm-python-client.git#v1.0.104

The previous version which depends on Python 2.7 can be installed with

.. code:: bash

    pip install git+https://github.com/dzhw/mdm-python-client.git#v1.0.88

The installation will also install a command line version which you can run with

.. code:: bash

    mdm --help

The following snippet demonstrates how to use the client programmatically:

.. code:: python

    from mdm_python_client.mdm_client import get_datapackage

    def test_get_datapackage():
        datapackage = get_datapackage("stu-gra2005$")
        if datapackage is not None:
            print("Pakettitel:", datapackage.title.de)
            print("DOI:", datapackage.doi)
            print("Veröffentlichungsjahr:", datetime.datetime.strptime(datapackage.release.firstDate,
                                                               '%Y-%m-%dT%H:%M:%S.%f').strftime("%Y"))
        else:
            print("Datenpaket mit id", args.datapackageId, "nicht gefunden!")

Having trouble?
===============

Please file an issue in the `issue tracker <https://github.com/dzhw/metadatamanagement/issues>`_ of the `MDM`_.
