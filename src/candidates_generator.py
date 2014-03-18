# -*- coding: utf-8 -*-
'''
Created on 17/03/2014

@author: roque
'''
import sys
import re

def create_candidates(word):
    ''' Create the possible candidates for a word with repeated letters'''
    if re.match('\W', word):
        return [word]
    
    word = word.lower()
    candidates = list()
    candidates.append("")
    size = len(word)
    i = 0
    
    while i < size:
        repetitions = 1
        while i < size - 1 and word[i] == word[i + 1]:
            i += 1
            repetitions += 1
            
        candidates = add_letter(candidates, word[i])
        min_repetitions = min(2, repetitions)
        
        if min_repetitions > 1:
            candidates = add_letter(candidates, word[i], True)

        i += 1
    
    return candidates
       
def add_letter(candidate_list, letter, duplicate=False):
    ''' Add the next letter to  the candidates '''
    tmp_list = list()
    for candidate in candidate_list:
        tmp_list.append(candidate + letter)
        if duplicate:
            tmp_list.append(candidate)

    return tmp_list

def output_format(original_word, candidades):
    ''' Return the output format string ''' 
    return  "^" + original_word + "/" + "/".join(candidades) + "$"

def main():
    ''' The main function '''
    for line in sys.stdin.readlines():
        for word in re.split('\s+', line):
            original_word = word.strip()
            if original_word != "":
                data = re.match('(\w+)(\W+)', original_word)
                if data:
                    candidates = create_candidates(data.group(1))
                    print("%s" % output_format(data.group(1), candidates))  
                    print("%s" % output_format(data.group(2), [data.group(2)]))  
                else:
                    candidates = create_candidates(original_word)
                    print("%s" % output_format(original_word, candidates))   

if __name__ == '__main__':
    main()

