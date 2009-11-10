#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
ngram_wrapper.py:
This is a wrapper for ngram.py that guess a language from a text
This module use language model from Perl module Lingua::LanguageGuesser
'''
import os
import ngram
from ConfigParser import ConfigParser

conf_file = '.ngramrc'
confname = 'lingua'
lm = 'LM'
lm_utf8 = 'LM_utf8'

## load the path of language model.
def load_path():
    path = os.path.join(os.environ['HOME'],conf_file)
    config = ConfigParser()
    config.read([path])

    result = {}
    result[lm] = os.path.join(config.get(confname,'path'),lm)
    result[lm_utf8] = os.path.join(config.get(confname,'path'),lm_utf8)
    return result

def guess(text):
    conf = load_path()

    ## classify the text's encode ( utf-8 or not )
    model_path = conf[lm_utf8]
    try:
        text.decode('UTF-8') 
    except:
        model_path = conf[lm]
    
    ## guess language 
    l = ngram.NGram(model_path)
    lang = l.classify(text)

    return lang
    

