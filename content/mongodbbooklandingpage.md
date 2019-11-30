Title: Making a landing page for MongoDB The Definitive Guide 
Slug: mongodb-book-landing-page
Author: Eoin Brazil
Date: 2019-11-30
Category: Blog/MongoDB
Tags: mongodb, writing, book, website

In advance of the book launch later in December I've been doing a little preparation. It turns out that Github is proving not just a useful location for the [source code](https://github.com/mongodb-the-definitive-guide-3e/) but that it also is an excellent place to host the book's [website/landing page](https://mongodbbook.info/).

I owe a lot of thanks to [Michael Hausenblas](https://twitter.com/mhausenblas) and his own excellent book on [Programming Kubernetes](https://programming-kubernetes.info/) which served as the inspiration and guide for my own landing page.

This used Github Pages and Jekyll with the ['minimal' theme](https://github.com/orderedlist/minimal) by [Steve Smith](https://github.com/orderedlist). I also choose to use this approach for my landing page.

I turned to [gandi.net](https://gandi.net) for my domain registration and in keeping with several other O'Reilly authors, I chose a *.info* domain. I decided on the short, simple, and available [mongodbbook.info](https://mongodbbook.info/) domain name.

After adding the content to the landing page, including a soon to be active Twitter account at ["MongodbT"](https://twitter.com/MongodbT). I made some minor tweaks to the [_config.yml](https://github.com/mongodb-the-definitive-guide-3e/mongodbbook.info/blob/master/_config.yml) file, specifically:

    :::yaml
	author:
	  twitter: eoinbrazil
	url: "https://mongodbbook.info/"
	plugins:
	  - jekyll-sitemap
	  - jekyll-feed


This minor additions allow for attribution to my twitter handle as well as providing a [sitemap xml file](https://mongodbbook.info/sitemap.xml) and a [atom feed file](https://mongodbbook.info/feed.xml). The Sitemap file allowed me to submit it to Bing, Google, and Yandex to allow it to be crawled a little sooner than if left to the automated crawler searches.


