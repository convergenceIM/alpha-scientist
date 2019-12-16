#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

#AUTHOR = 'Chad Gray'
SITENAME = 'The Alpha Scientist'
SITEURL = 'https://alphascientist.com'

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

LOCALE = ('usa', 'jpn',      # On Windows
           'en_US', 'ja_JP'   # On Unix/Linux
)

# Feed generation is usually not desired when developing
FEED_ATOM = 'feeds/atom.xml'
FEED_RSS = 'feeds/rss.xml'

# Blogroll
LINKS = (('Quantocracy', 'http://quantocracy.com/'),
         ('Robot Wealth', 'https://robotwealth.com/blog/'),
         ('QuantStart', 'https://www.quantstart.com/articles'),
         ('Simon Ouellette', 'http://www.simonouellette.com/'),
         ('Marcos Lopez de Prado', 'http://www.quantresearch.info/'),
         ('Financial Hacker', 'http://www.financial-hacker.com'),
         ('Ex Machina', 'http://www.mov37.com/ex-machina/'),
         )

# Social widget
SOCIAL = (('Linkedin', 'https://www.linkedin.com/in/chadgraycfa/'),
          ('Twitter', 'https://twitter.com/data2alpha'),)

#SOCIAL_IMAGE = 'content/images/logo.jpg'
SOCIAL_IMAGE = 'images/logo.jpg'

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

OUTPUT_PATH = 'docs/'

MARKUP = ('md', 'ipynb')

PLUGIN_PATHS = ['./plugins']
PLUGINS = ['ipynb.markup']

STATIC_PATHS = ['images']

THEME = 'themes/octopress'
SITEIMAGE = '/images/profile.jpg width=400 height=250'
SITESUBTITLE = 'Discovering alpha in the stock market using data science'

HIDE_AUTHORS = True

DISQUS_SITENAME = 'alphascientist-com'

DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False
MENUITEMS = (
    ('Blogs', '/index.html'),
    ('Authors', '/authors.html'),
    )

FAVICON_FILENAME = 'images/favicon.png'

FACEBOOK_LIKE = True
TWITTER_USER = 'data2alpha'

TWITTER_WIDGET_ID = ('data2alpha')
TWITTER_TWEET_BUTTON = True # show twitter tweet button
TWITTER_FOLLOW_BUTTON = True # show twitter follow button
#TWITTER_TWEET_COUNT: 3 number of latest tweets to show
#TWITTER_SHOW_REPLIES: 'false' whether to list replies among latest tweets
#TWITTER_SHOW_FOLLOWER_COUNT: 'true' show number of followers

#GOOGLE_ANALYTICS = "UA-121434821-1"
#GOOGLE_UNIVERSAL_ANALYTICS = "UA-121434821-1"
