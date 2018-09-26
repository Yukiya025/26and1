# -*- coding: utf-8 -*-
from nltk import FreqDist
import pymorphy2
import csv
import re
import del_words
"""
1. open 26and1.txt
2. read 26and1.txt
3. replace period etc. into space ' '
4. split()
5. lemma words into normal normal_form
   lemma_list has normal_form russian words
6. write lemma_list into csv
"""
downloadtxt = open('26and1.txt', 'r', encoding = 'utf-8-sig')
texts = downloadtxt.read()
texts = re.sub('[.,?!()\'—]', ' ', texts)
texts = texts.split()

analyzer = pymorphy2.MorphAnalyzer()

lemma_list = []
for text in texts:
    lemma = analyzer.parse(text)[0].normal_form
    lemma_list.append(lemma)

lemma_list = list(filter(lambda d: d not in (del_words.del_w), lemma_list))
freqdist = FreqDist(lemma_list)
freqdist_list = freqdist.most_common(900)
with open('26and1.csv', 'w', encoding = 'utf-8-sig') as file:
    writer = csv.writer(file, lineterminator = '\n')
    for n in range(0, len(freqdist_list)):
        writer.writerows([freqdist_list[n]])
