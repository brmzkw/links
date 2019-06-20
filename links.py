#!/usr/bin/env python

import argparse
import datetime
import json
import os
import sys

import PyRSS2Gen

# Fix: basestring is not defined with Python3
# http://www.rfk.id.au/blog/entry/preparing-pyenchant-for-python-3/
if sys.version_info.major == 3:
        PyRSS2Gen.basestring = (str, bytes)


DEFAULT_LINKSFILE = os.path.join(os.path.dirname(__file__), 'links.json')
DEFAULT_RSSFILE = os.path.join(os.path.dirname(__file__), 'links.rss')


def markdownify(links):
    ret = '''
| Date | Keywords | URL |
|------|----------|-----|
'''
    for link in links:
        ret += '| %s | %s | %s |\n' % (
            link['date'],
            ' '.join(link['keywords']),
            link['url']
        )
    return ret


def build_rss(links, rssfile):
    rss = PyRSS2Gen.RSS2(
        title="brmzkw links feed",
        link="http://www.brmzkw.info",
        description="My tech readings",
        lastBuildDate=datetime.datetime.utcnow(),
        items=[
            PyRSS2Gen.RSSItem(
                title=item['url'],
                link=item['url'],
                description=' '.join(item['keywords']),
                guid=PyRSS2Gen.Guid(item['url']),
                pubDate=datetime.datetime.strptime(item['date'], '%Y/%m/%d')
            ) for item in links]
    )
    rss.write_xml(rssfile)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--linksfile', type=file, default=DEFAULT_LINKSFILE)
    parser.add_argument('--markdownify', action='store_true', default=False)
    parser.add_argument('--rss', type=argparse.FileType('w+'), default=DEFAULT_RSSFILE)
    args = parser.parse_args()

    links = json.loads(args.linksfile.read())

    if args.markdownify:
        print(markdownify(links))
    if args.rss:
        build_rss(links, args.rss)


if __name__ == '__main__':
    main()
