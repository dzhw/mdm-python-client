.. image:: https://travis-ci.org/dzhw/mdm-python-client.svg?branch=master
    :target: https://travis-ci.org/dzhw/mdm-python-client
.. image:: https://img.shields.io/badge/python-2.7-blue

=================
MDM Python Client
=================

This project contains a REST API client for `MDM <https://metadata.fdz.dzhw.eu>`_  (`Metadatamanagement System <https://github.com/dzhw/metadatamanagement>`_) of the Research Data Center of the DZHW.

Description
===========

The client can be used to retrieve metadata from the public `REST API <https://metadata.fdz.dzhw.eu/swagger-ui.html>`_ of the MDM_. Currently it uses a cache which gets stale after 24 hours. The module currently depends on Python 2.7 cause it is developed for our CMS which is currently based on this Python version.

Note
====

This project has been set up using PyScaffold 2.5.11. For details and usage
information on PyScaffold see http://pyscaffold.readthedocs.org/.
