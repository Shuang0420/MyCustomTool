# -*- coding: utf-8 -*-
import os
import argparse
from lxml import etree
import urllib2
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


def initialize():
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', action='store', dest='url', default='',
                        help='url you want to save')
    parser.add_argument('-t', action='store', dest='title', default='',
                        help='title you want to save')
    parser.add_argument('-newblock', action='store', dest='newblock', default='',
                        help='create a block')
    parser.add_argument('-b', action='store', dest='blockname', default='',
                        help='save under this block')
    parser.add_argument('-newfile', action='store', dest='newfile',
                        default='', help='generate a new file')
    parser.add_argument('-f', action='store', dest='filename', default='weeklyReading.html',
                        help='the file to write, default is weeklyReading.html')
    parser.add_argument('-c', action='store_true', dest='clean', default='false',
                        help='empty the file')
    return parser.parse_args()


def start(args):
    # initialize parameters and process file
    url = args.url
    title = args.title
    newblock = args.newblock
    blockname = args.blockname
    newfile = args.newfile
    filename = args.filename
    clean = args.clean

    if not (url or newfile or newblock or clean):
        print 'Please identify the url. Use the command "python saveUrl.py -u url"'
        exit(1)
    if newfile:
        newFile(newfile)
        if newblock:
            newBlock(newblock, newfile)
    if (not newfile) and newblock:
        newBlock(newblock, filename)
    if url and (not title):
        content = urllib2.urlopen(url).read()
        dom = etree.HTML(content)
        title = dom.xpath('//title/text()')[0].encode('utf8')
    if url:
        newRecord(filename, blockname, url, title)
    if clean==True:
        emptyFile(filename)


def newRecord(filename, blockname, url, title):
    filename = checkFile(filename)
    f = open(filename, 'r')
    content = f.readlines()
    writelist = []
    if (not blockname) or content[-1] == blockname:
        with open(filename, 'a') as fw:
            fw.write("<a href='" + url + "'>" + title + '</a><br>')
    else:
        fw = open(filename, 'w+')
        count = 0
        for line in content:
            count += 1
            if blockname in line:
                writelist = content[0:count]
                writelist.append("<a href='" + url + "'>" + title + '</a><br>')
                writelist.extend(content[count:])
                fw.writelines(writelist)
        fw.flush()


def newFile(filename):
    if os.path.isfile(filename):
        print "file already exists"
        exit(1)
    if not filename.endswith('.html'):
        filename += '.html'
    with open(filename, 'w') as f:
        f.write('<html>\n<head>\n<meta charset="UTF-8">\n</head>\n<body>')


def newBlock(newblock, filename):
    filename = checkFile(filename)
    with open(filename, 'a') as fw:
        fw.write('<h1>' + newblock + '</h1>')


def emptyFile(filename):
    filename = checkFile(filename)
    f = open(filename, 'w')

def checkFile(filename):
    if not os.path.isfile(filename):
        print "file not exists"
        exit(1)
    if not filename.endswith('.html'):
        filename += '.html'
    return filename

if __name__ == '__main__':
    args = initialize()
    start(args)
