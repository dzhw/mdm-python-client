=========
Changelog
=========

Version 0.0.1
=============

- Quick implementation of an MDM client including caching

Version 0.0.2
=============

- Move cache to temp directory

Version 0.0.3
=============

- Try to detect directory with proper access rights for our CMS

Version 1.0.88
==============

First production release:

- Client uses persistent cache which is valid for 24 hours.
- It falls back to in-memory cache if the file for storing the cache cannot be written.
- In case of any (network) error the cached result (if present) is returned.
