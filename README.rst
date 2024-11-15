PDF to semantic HTML conversion
===============================

Transcript contains Python programs whose job is to transcribe PDF into sematic HTML.

`transcript.py <transcript.py>`_
    Get semantic HTML from PDFs converted by pdf2htmlEX.

`ttf.py <ttf.py>`_
    Recover lost text from PDFs
    where characters are nothing more than images of themselves.

`pdf2html.py <pdf2html.py>`_
    Batch process a folder full of PDFs ready for transcript.py

Read the docstrings for more information.

Example
-------

`PDF before <https://fmalina.github.io/unilex-transcript/tests/PDF/report-1967329.pdf>`_ and
`semantic HTML after <https://fmalina.github.io/unilex-transcript/tests/HTM/report-1967329.htm>`_

Install
--------
Get Python 3 installed along with latest pdf2htmlEX.
e.g. with Homebrew:

    brew install python3 pdf2htmlEX

Docker install of pdf2htmlEX is also supported (brew one started failing as of late).
This particular image is tested and used in the default config via ``DOCKER_IMG_TAG``.

    docker pull pdf2htmlex/pdf2htmlex:0.18.8.rc2-master-20200820-ubuntu-20.04-x86_64

Install lxml under python3 ``pip3 install lxml`` or just run the following and get freetype-py too.

    pip3 install -r requirements.txt

Configure
---------
Configure your project path in your ``.env`` file and ``config.py``
**most importantly the DATA_DIR**.
This can be any folder let's say ``DATA_DIR=/path/to/unilex-transcript/tests``.
If you use a docker install of pdf2htmlEX, you'll need to set ``DOCKER_INSTALL=1``
This will mount your data dir to Docker path. ``DOCKER_IMG_TAG`` is also
`configurable <config.py>`_.
Go ahead create your ``.env`` file and add ``DATA_DIR=...``

Your DATA_DIR should end up containing 3 folders: PDF, HTML and HTM if you
otherwise stick with default configuration. Create a 'PDF' folder inside and
drop your PDFs there.

* PDF is a folder where your PDFs are.
* HTML is where pdf2htmlEX output (non-semantic HTML) ends up after running
  ``./pdf2html.py``, which just runs pdf2htmlEX with suitable options.
* HTM is the final destination where semantic HTML gets born after running
  ``./transcript.py``.

Run
---
``./pdf2html.py``

``./transcript.py``

When you change configuration within ``./transcript.py`` or tweak some code.
You only need to run ``./transcript.py``

Development process
-------------------
Set expected (hand-adjusted) output to aim for and
improve codebase to get transcript output closer to the ideal semantic output.
Make sure your changes don't make output worse for other tests. Use `ruff`.
