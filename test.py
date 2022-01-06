#!/usr/bin/env python3
import transcript
import config
import os
import os.path


def preview(stem):
    path = config.HTML_DIR + f'/{stem}/{stem}.html'
    transcript.semanticize(path)
    result = os.path.dirname(path).replace('HTML', 'HTM')+'.htm'
    os.system('open -a safari file://' + result)


for test in [
        'design-heavy',
        'report',
        'research-paper',
        'technical-2col',
        'vol2a',
        ]:
    preview(test)
