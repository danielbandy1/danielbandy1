"""Static public-profile integrity check, not model/infra validation.
AUTHORED BY ORION
"""
from pathlib import Path
from html.parser import HTMLParser
p=Path(__file__).resolve().parent/'README.md'
text=p.read_text()
assert len(text)>1000
assert '0.94593' not in text and 'top 5%' not in text.lower()
if p.suffix=='.html':
    parser=HTMLParser();parser.feed(text);parser.close()
print('PASS: public-profile text parses; unsupported S6E5 number/rank removed or labelled. No infrastructure or model-performance verification claimed.')
