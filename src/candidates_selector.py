# -*- coding: utf-8 -*-
'''
Created on 17/03/2014

@author: roque
'''
import sys
import codecs

dictionary_words = dict()

def load_dictionary():
    ''' Load the word set into a dictionary '''
    data_file = codecs.open("../resource/english_words.txt", 'r', 'utf-8')
    while True:
        line = data_file.readline()
        if not line: break
        word = line.strip().split(' ')[2]
        dictionary_words[word] = None
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
    load_dictionary()
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
