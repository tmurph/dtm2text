============================
Convert DTM to text and back
============================

    :Author: Trevor Murphy
    :Contact: trevor.m.murphy@gmail.com

This command line tool dumps your Dolphin TAS Movie files to a plain text list of frame data (plus a header file).

.. code:: sh
    :name: DTM to plain text

    $ dtm2text YOUR_MOVIE

This will produce two files, ``YOUR_MOVIE_header`` and ``YOUR_MOVIE_frames.txt``, both in the current working directory.

Requirements
------------

Python 3.  Probably not a hard requirement, I just haven’t tested this tool with any earlier versions.

Install
-------

Just use `pip <https://pip.pypa.io/en/stable/>`_!

.. code:: sh

    $ pip install dtm2text

License
-------

Distributed under the terms of the `GPLv3 <https://www.gnu.org/licenses/gpl-3.0.en.html>`_ license.
