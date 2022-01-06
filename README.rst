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

Not a flattening example with fine tuned options, but a realistic default output to expect with no scripting.

`PDF before <tests/PDF/report.pdf>`_ and
`semantic HTML after <tests/HTM/report.htm>`_

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
Add expected (hand-adjusted) output to aim for to the test suite and
improve codebase to get transcript output closer to the ideal semantic output.

Dual Licensing
--------------

Commercial license
~~~~~~~~~~~~~~~~~~
If you want to use Transcript to develop and run commercial projects and applications, the Commercial license is the appropriate license. With this option, your source code is kept proprietary.

Once purchased, you will be granted a commercial BSD style license and all set to use Transcript in your business.

`Small Team License (£1200) <https://fmalina.github.io/pay.html?amount=1200&msg=Transcript_Team_License>`_
Small Team License for up to 8 developers

`Organization License (£3200) <https://fmalina.github.io/pay.html?amount=3200&msg=Transcript_Organisation_License>`_
Commercial Organization License for Unlimited developers

Open source license
~~~~~~~~~~~~~~~~~~~
If you are creating an open source application under a license compatible with the GNU GPL license v3, you may use Transcript under the terms of the GPLv3.
