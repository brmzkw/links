#!/usr/bin/env python

import argparse
import json
import os


DEFAULT_LINKSFILE = os.path.join(os.path.dirname(__file__), 'links.json')


def markdownify(linksfile):
    data = json.loads(linksfile.read())
    ret = '''
| Date | Keywords | URL |
|------|----------|-----|
'''
    for link in data:
        ret += '| %s | %s | %s |\n' % (
            link['date'],
            ' '.join(link['keywords']),
            link['url']
        )
    return ret


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--linksfile', type=file, default=DEFAULT_LINKSFILE)
    parser.add_argument('--markdownify', action='store_true', default=False)
    args = parser.parse_args()

    if args.markdownify:
        print(markdownify(args.linksfile))
    

if __name__ == '__main__':
    main()
