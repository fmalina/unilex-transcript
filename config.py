# This is your project root, configure your own path.
DATA_DIR = '/Users/f/DATA/OFSTED/'

# PDF folder within your project root. PDFs to convert come from here.
PDF_DIR  = DATA_DIR+'PDF'
# HTML folder is where pdf2htmlEX outputs (non-semantic HTML) after running `./pdf2html.py`.
HTML_DIR = DATA_DIR+'HTML'
# used by ttf.py to access full original fonts to compare with the broken ones
FULL_FONTS_PATH  = '/Users/f/SITES/etc/ttf'
# remove mumbo-jumbo TEXT strings before HTML processing (REGEXes or text)
REMOVE_BEFORE = (
    r'The Office for Standards.*?www\.ofsted\.gov\.uk',
    r'Any complaints.*?\@ofsted\.gov\.uk',
    r'© Crown copyright 20\d\d',
    r'Inspection grades:.*?inspection terms',
    r'This letter.*?their school\.',
    r'You can use Parent View.*?www\.ofsted\.gov\.uk'
)
# find and replace after HTML processing finished
REPLACE_AFTER = (
    (r'td>( )?Overall effectiveness j', 'td colspan=4>Overall effectiveness j'),
)
# Additional bullet point characters to be expected at start of line for <li>
# Copied out of the processsed PDF. Common bullets are pre-programmed.
BULLETS =  ('', '')
