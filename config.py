from os import path

# This is your project root, configure your own path.
DATA_DIR = '/path/to/your/data/dir/'

# PDF folder within your project root. PDFs to convert come from here.
PDF_DIR  = path.join(DATA_DIR, 'PDF')

# HTML folder is where pdf2htmlEX outputs (non-semantic HTML) after running
# `./pdf2html.py`.
HTML_DIR = path.join(DATA_DIR, 'HTML')

# Used by ttf.py to access full original fonts to compare with the broken ones,
# e.g. /Users/f/SITES/etc/ttf or /usr/share/fonts or ~/.fonts.
FULL_FONTS_PATH  = '/path/to/truetype/fonts/'

# Remove mumbo-jumbo text strings before HTML processing (REGEXes or text)
REMOVE_BEFORE = (
    # r'The Office for Standards.*?www\.ofsted\.gov\.uk',
    # r'Any complaints.*?\@ofsted\.gov\.uk',
    # r'© Crown copyright 20\d\d',
    # r'Inspection grades:.*?inspection terms',
    # r'This letter.*?their school\.',
    # r'You can use Parent View.*?www\.ofsted\.gov\.uk'
)

# Find and replace after HTML processing is finished.
REPLACE_AFTER = (
    # (r'td>( )?Overall effectiveness j', 'td colspan=4>Overall effectiveness j'),
)

# Additional bullet point characters to be expected at start of line for <li>
# Copied out of the processsed PDF. Common bullets are pre-programmed.
BULLETS =  ('', '')
