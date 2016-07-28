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

- before http://reports.ofsted.gov.uk/provider/files/875315/urn/100006.pdf
- after http://schooletc.co.uk/report/96989#reports


Install
--------
Get Python 3 installed along with latest pdf2htmlEX.
e.g. with Homebrew:

    brew install python3 pdf2htmlEX

Install lxml under python3 ``pip3 install lxml`` or just run the following and get freetype-py too.
    
    pip3 install -r requirements.txt

Configure
---------
Configure your project path in ``config.py`` **most importantly the DATA_DIR on top**.
This can be any folder let's say ``/Users/[your username]/Desktop/transcript-data``.
Go ahead create it.

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
