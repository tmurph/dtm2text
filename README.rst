============================
Convert DTM to text and back
============================

    :Author: Trevor Murphy
    :Contact: trevor.m.murphy@gmail.com

This command line tool dumps your Dolphin TAS Movie files to a plain text list of input data (plus a header file).

.. code:: sh
    :name: DTM to plain text

    $ dtm2text YOUR_MOVIE
    # creates YOUR_MOVIE_header and YOUR_MOVIE_inputs.txt

Alternatively, you can piece together some plain text lists (plus a header file) into a DTM.

.. code:: sh
    :name: Plain text to DTM

    $ text2dtm NEW_MOVIE header_file inputs.txt
    # creates NEW_MOVIE

    # you can supply several files of inputs
    $ text2dtm NEW_MOVIE header_file inputs_01.txt inputs_02.txt

    # if you have lots of input files, you can supply a from-file instead
    $ cat inputs_from_file
    inputs_01.txt
    inputs_02.txt
    inputs_03.txt
    $ text2dtm NEW_MOVIE header_file @inputs_from_file

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
