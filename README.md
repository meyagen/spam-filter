# Spam Filter

## Description

Machine problem for CS 180: Introduction to Artificial Intelligence. The filter uses Naive Bayes to classify emails into spam or ham and is implemented in Python.

### Note on the Training Set and Test Data

Training set and test data are not included in the repository. Should they be added, the emails are assumed to be pre-processed and in *.txt format. Refer to the directory hardcoded in MP.py, or change them.

It is assumed that in each individual email, non-words (such as numbers and punctuation marks) and common english words that have no bearing on the Bayes model (e.g. "the", "is", "of") have been removed. All words are to be lemmatized and converted to lowercase. Whitespaces are to be trimmed to a single space character.

## Instructions

Run MP.py to train machine. Classification (ham or spam) is recorded in results/output.txt. Classification and value computed using Bayes' formula are recorded in results/bayes_output.txt.

Run accuracy.py to check accuracy of output. Correct results can be found in results/correct/results.txt.