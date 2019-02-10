#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Eoin Brazil'
SITENAME = u'Insights'
SITEURL = u'http://eoinbrazil.com'
TIMEZONE = 'Europe/Dublin'
# THEME = 'themes/modded_syte'
THEME = 'themes/responsive'
PLUGIN_PATHS = ['/Users/braz/Desktop/website/pelican-plugins/']
PLUGINS = ['assets', 'neighbors', 'share_post', 'sitemap', 'related_posts', 
'yuicompressor', 'optimize_images']
RELATED_POSTS_MAX = 5

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

LOCALE = 'C' # en_IE
DEFAULT_LANG = u'en'
DEFAULT_DATE_FORMAT = '%a %d %b %Y'
TYPOGRIFY = True

FEED_DOMAIN = SITEURL
FEED_ALL_RSS = 'feeds/all.rss.xml'
FEED_ALL_ATOM = 'feeds/all.atom.xml'

GOOGLE_ANALYTICS = 'UA-45182755-1'

PDF_GENERATOR = False
REVERSE_CATEGORY_ORDER = True
DEFAULT_PAGINATION = False
STATIC_PATHS = [
    'CNAME',
	'images',
	'pdfs',
	'theme/img/avatar.png'
]

# options for syte theme
ABOUT = u'Joining the dots from experience to product...'
SITE_DESCRIPTION = u'Personal blog of Eoin Brazil'
SITE_KEYWORDS = u'blog eoin braz brazil mongodb computer scientist data science datascience java analysis r rstats python node ruby consulting dublin machine learning cuda gpgpu ux hci parallel'
DISPLAY_HOME_ON_MENU = True
TWITTER_INTEGRATION_ENABLED = False
TWITTER_USERNAME = 'eoinbrazil'
GITHUB_INTEGRATION_ENABLED = False
GITHUB_USERNAME = 'braz'

MINI_BIO = u"Creating ideas and insights."
BIO = u'<strong>Eoin Brazil</strong> is a computer scientist, UX architect, technical services engineer (similar to SRE) and data scientist. He leads the Proactive Technical Services team within MongoDB Engineering.</br>A range of his work can be found on <a href="https://github.com/braz">Github</a>. You can find his <a href="https://slideshare.net/eoinbrazil">talks</a> online as well as his <a href="http://eoinbrazil.com/extras/vitae-eoinbrazil-feb-2019-dev.pdf">CV</a>.'

# Feeds

ALL_FEEDS = {
	'RSS': 'feeds/all.rss.xml',
	'ATOM': 'feeds/all.atom.xml'
}

# Blogroll
LINKS =  (
	('Python Ireland', 'http://python.ie/'),
    ('Dublin R Users', 'http://www.meetup.com/DublinR/'),
    ('Dublin Scala Users', 'http://www.meetup.com/Dublin-Scala-users-group//'),
    ('Dublin Ruby Users', 'http://www.meetup.com/rubyireland/'),
    ('Dublin NodeJS Users', 'http://www.nodejsdublin.com/'),
    ('Pub Standards', 'http://pubstandards.ie/'),
)

# Social widget
SOCIAL = (
	('Twitter', 'http://www.twitter.com/eoinbrazil', '&#xe086;'),
	('LinkedIn','http://ie.linkedin.com/in/eoinbrazil', '&#xe052;'),
	('Foursquare','https://foursquare.com/eoinbrazil', '&#xe032;'),
	('GitHub', 'http://www.github.com/braz', '&#xe037;'),
	('RSS', 'http://eoinbrazil.com/feeds/all.rss.xml', '&#xe071;'),
	('ATOM', 'http://eoinbrazil.com/feeds/all.atom.xml', '&#xe011;')
)

STATIC_PATHS = [
    'extras',
    'theme/img'
    ]

EXTRA_PATH_METADATA = {
	'extras/CNAME': {'path':'CNAME'},
	'extras/msc_thesis.pdf': {'path':"pdfs/msc_thesis.pdf"},
	'extras/phd_thesis.pdf': {'path':"pdfs/phd_thesis.pdf"},
	'extras/pgdip_dissertation.pdf': {'path':"pdfs/pgdip_dissertation.pdf"},
	'extras/PyCon2015-PythonMongoDBDataPipelines-Keynote.pdf': {'path':"pdfs/PyCon2015-PythonMongoDBDataPipelines-Keynote.pdf"},
	'extras/PyCon2016-IntroductionToGradientBoosting-powerpoint.pdf': {'path:':"pdfs/PyCon2016-IntroductionToGradientBoosting-powerpoint.pdf"},
	'extras/PyCon2017-TwoApproachesToScaleYourProcessing.pdf': {'path':"pdfs/PyCon2017-TwoApproachesToScaleYourProcessing.pdf"},
	'extras/DublinR - Beyond the Single Instance - Leveraging the Public Cloud for Large Computations.pdf': {'path':"pdfs/DublinR - Beyond the Single Instance - Leveraging the Public Cloud for Large Computations.pdf"},
	'extras/DublinR - Machine Learning - Machine Learnings on Machines.pdf': {'path':"pdfs/DublinR - Machine Learning - Machine Learnings on Machines.pdf"},
	'extras/DublinR - Machine Learning 101 - Introduction with Examples.pdf': {'path':"pdfs/DublinR - Machine Learning 101 - Introduction with Examples.pdf"},
	'extras/avatar.png': {'path':"img/avatar.png"},
	'theme/img/favicon.ico': {'path':"favicon.ico"}
}

SITEMAP = {
	'exclude': ['tag/', 'category/'],
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}
