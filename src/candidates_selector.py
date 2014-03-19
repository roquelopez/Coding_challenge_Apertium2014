# -*- coding: utf-8 -*-
'''
Created on 17/03/2014

@author: roque
'''
import sys
import codecs

dictionary_words = dict()
languages = {'en':'english_words.txt', 
             'es':'spanish_words.txt', 
             'pt':'portuguese_words.txt'}

def load_dictionary(language='en'):
    ''' Load the word set into a dictionary '''
    if language not in languages:
        print("'%s' Not recognize, using English language." % language)
        language = 'en'
    
    data_file = codecs.open("../resource/languages/%s" % languages[language], 'r', 'utf-8')
    
    while True:
        line = data_file.readline()
        if not line: break
        dictionary_words[line.strip()] = None
    data_file.close()


def correct(word, candidates):
    ''' Verify and return the candidate that is in the dictionary, otherwise return the original word '''
    for candidate in candidates:
        if candidate in dictionary_words:
            return candidate
    return word

def output_format(original_word, correct_word):
    ''' Return the output format string '''
    return "^%s/%s$" % (original_word, correct_word)

def main():
    ''' The main function '''
    if len(sys.argv) != 2:
        print ("Incorrect number of arguments.")
        return
    
    load_dictionary(sys.argv[1])
    correct_words = list()

    for line in sys.stdin.readlines():
        tmp_list = line.replace('$\n', '').split('/')
        original_word = tmp_list[0][1:]
        candidates = tmp_list[1:]
        correct_word = correct(original_word, candidates)
        correct_words.append(correct_word)
        print(output_format(original_word, correct_word))   
    
    print(" ".join(correct_words))    
        
if __name__ == '__main__':
    main()
