#!/usr/bin/env python3
import transcript
import config
import os
import os.path

def preview(i):
    path = config.HTML_DIR + '/%s/%s.html' % (i, i)
    transcript.semanticize(path)
    result = os.path.dirname(path).replace('HTML', 'HTM')+'.htm'
    os.system('open -a safari file://' + result)

preview('100006_1967329')
preview('100008_2457093')
preview('100026_945655')
preview('100093_945683')
preview('105460_1867393')
