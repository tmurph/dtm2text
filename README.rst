============================
Convert DTM to text and back
============================

    :Author: Trevor Murphy
    :Contact: trevor.m.murphy@gmail.com

This command line tool dumps your Dolphin TAS Movie files to a plain text list of frame data (plus a header file).

.. code:: sh
    :name: DTM to plain text

    # creates YOUR_MOVIE_header and YOUR_MOVIE_frames.txt
    $ dtm2text YOUR_MOVIE

Alternatively, you can piece together some plain text lists (plus a header file) into a DTM.

.. code:: sh
    :name: Plain text to DTM

    # creates NEW_MOVIE
    $ text2dtm NEW_MOVIE header_file frames.txt

    # you can also supply several frames files
    $ text2dtm NEW_MOVIE header_file frames_01.txt frames_02.txt

    # if you have very many frames files, you can supply a from-file instead
    $ cat frames_from_file
    frames_01.txt
    frames_02.txt
    frames_03.txt
    $ text2dtm NEW_MOVIE header_file @frames_from_file

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
