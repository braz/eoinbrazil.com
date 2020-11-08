Date: 2015-03-21
Title: Machine Learning of Machines with R
Tagline: Dublin R User Group
Slug: machinemlwithr
Category: Blog/R
Tags: r, presentations, machine learning, rstats

Following my introduction presentation to the [Dublin R User Group](http://www.meetup.com/DublinR/) on machine learning, I again had the pleasure of being invited to talk on more machine learning. My talk source and examples are in a [Github repo](https://github.com/braz/DublinR-ML-machine). The talk was more intermediate than my [previous introductory talk](https://github.com/braz/DublinR-ML-treesandforests/). It used two datasets focusing on computing cluster job usage statistics (e.g. similar to data from a HPC job scheduler) and machine level application and host usage statistics (e.g. similar to those from host monitoring software such as Nagios).

[PDF version of this talk]({static}/extras/DublinR - Machine Learning - Machine Learnings on Machines.pdf)

### Overview

The techniques covered included:

* Background on large scale clusters (e.g. HPC) and rationale for ML of machine/cluster operational metrics
* Workflow for model building
* Data transformation
* Addressing feature selection
* Model assessment and selection
* Interpreting a confusion matrix
* Interpreting a ROC plot
* Approaches to handling prediction errors
* Boosting and Bagging
* Data set 1 - Job scheduling data
* Data set 2 - Machine metrics data
* Summary / recap
* (Unused) A review of various ML techniques:
	* Decision trees
	* Random forests
	* k Nearest Neighbors
	* Support vector machines

### Background

This talk focused on the two datasets as well as highlightly how the business context was important to consider when developing the models. The talk looking at using machine learning to improvie the utilisation and scheduling of large scale clusters (significant hardware resources). It recapped some earlier material and focused a little more on feature selection and feature generation as well as applied domain expertise from the data set. It provides two datasets showing examples of how to use R to select, assess and create the models.

### Talk slides

<script async class="speakerdeck-embed" data-id="8afe1177b3be4840980b2f252a428b81" data-ratio="0.707182320441989" src="//speakerdeck.com/assets/embed.js"></script>