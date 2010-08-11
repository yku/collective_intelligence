import feedparser
import re

# RSS feed のタイトルと単語頻度のディクショナリを返す
def getwordcounts(url):
    d = feedparser.parse(url)
    wc = {}

    for e in d.entries:
        if 'summary' in e: summary = e.summary
        else: summary = e.description

        words = getwords(e.title + ' ' + summary)
        for word in words:
            wc.setdefault(word, 0)
            wc[word] += 1
    return d.feed.title, wc

def getwords(html):
    # htmlタグを取り除く
    txt = re.compile(r'<[^>]+>').sub('',html)
    # 非アルファベット文字で分割
    words = re.compile(r'[^A-Z^a-z]+').split(txt)
    return [word.lower() for word in words if word != '']

apcount = {}
wordcounts = {}
feedlist = [line for line in file('feedlist.txt')]
for feedurl in feedlist:
    try:
        title, wc = getwordcounts(feedurl)
        wordcounts[title] = wc
        for word, count in wc.items():
            apcount.setdefault(word, 0)
            if count > 1:
                # word が出現するblogの数をカウント
                apcount[word] += 1
    except:
        print 'Failed to parse feed %s' % feedurl

wordlist = []
for w, bc in apcount.items():
    frac = float(bc) / len(feedlist)
    if frac > 0.1 and frac < 0.5: wordlist.append(w)

out = file('blogdata', 'w')
out.write('Blog')
for word in wordlist: out.write('\t%s' % word)
out.write('\n')
for blog, wc in wordcounts.items():
    out.write(blog)
    for word in wordlist:
        if word in wc: out.write('\t%d' % wc[word])
        else: out.write('\t0')
    out.write('\n')
