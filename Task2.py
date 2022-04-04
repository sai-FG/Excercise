# =======================================================
# TASK 2
# =======================================================
# Our customer records are sometimes a little messy and contain duplicate entires.
# For instance, we might have two records like "Pfizer" and "Pfizer Incorporated (old DO NOT USE)".
# Please write a small basic function to merge these records together. We've provided a few example inputs below.
#
# We are aware this is a very difficult problem: we're looking for what you can do quickly as a basic case, not an ideal solution.
#
# Equipment ONLY - Saama Technologies
# Saama Technologies
# SaamaTech, Inc.
# Takeda Pharmaceutical SA - Central Office
# *** DO NOT USE *** Takeda Pharmaceutical
# Takeda Pharmaceutical, SA
# Ship to AstraZeneca
# AstraZeneca, gmbh Munich
# AstraZeneca (use AstraZeneca, gmbh Munich acct 84719482-A)
#
# Use your own interpretation of the question and feel free to provide a written explanation for your choices as well.


import pandas as pd
import numpy as np
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
import string
import re
#

document_list = ["Pfizer","Pfizer Incorporated (old DO NOT USE)","Equipment ONLY - Saama Technologies","Saama Technologies", "SaamaTech, Inc.", "Takeda Pharmaceutical SA - Central Office"
       ,"*** DO NOT USE *** Takeda Pharmaceutical", "Takeda Pharmaceutical, SA", "Ship to AstraZeneca",
       "AstraZeneca, gmbh Munich", "AstraZeneca (use AstraZeneca, gmbh Munich acct 84719482-A)"]



stop = set(stopwords.words('english'))
exclude = set(string.punctuation)
lemma = WordNetLemmatizer()
def clean(doc):
    stop_free = " ".join([i for i in doc.lower().split() if i not in stop])
    punc_free = ''.join(ch for ch in stop_free if ch not in exclude)
    normalized = " ".join(lemma.lemmatize(word) for word in punc_free.split())
    return normalized

doc_clean = [clean(doc).split() for doc in document_list]


print(doc_clean)


# tying some bruteforce methodology ,


doc_clean = [re.sub(r"[^a-zA-Z0-9\s]",'',doc.lower()) for doc in document_list ]


# find most occurances from doc_clean

List_words = []

for i in doc_clean:
    List_words.extend(i.split())

# remove unwanted words , adj, verbs

remove_list = ["a","an","the","munich","was","do","use","only","to","gmbh","not","Pharmaceutical","pharmaceutical","Technologies","Inc","in","technologies"]
doc_clean_1 = [i for i in List_words if i not in remove_list]

from collections import Counter

most_occur = dict(Counter(doc_clean_1))
most_occur_gt_2 = [i for i,j in most_occur.items() if j >= 2]

#  Now categorize the with the original description

def categorize(doc):
    x = doc.lower().split()
    x = [re.sub(r"[^a-zA-Z0-9]", '', word) for word in x]
    count = 0
    for i in x:
        if i in most_occur_gt_2:
            return i
    return "NA"

cat_dict = {i:categorize(i) for i in document_list}

# Out Put

# {'Pfizer': 'pfizer',
# 'Pfizer Incorporated (old DO NOT USE)': 'pfizer',
#  'Equipment ONLY - Saama Technologies': 'saama',
#  'Saama Technologies': 'saama',
#  'SaamaTech, Inc.': 'NA',
#  'Takeda Pharmaceutical SA - Central Office': 'takeda',
#  '*** DO NOT USE *** Takeda Pharmaceutical': 'takeda',
#  'Takeda Pharmaceutical, SA':
#  'takeda', 'Ship to AstraZeneca': 'astrazeneca',
#   'AstraZeneca, gmbh Munich': 'astrazeneca',
#  'AstraZeneca (use AstraZeneca, gmbh Munich acct 84719482-A)': 'astrazeneca'}















