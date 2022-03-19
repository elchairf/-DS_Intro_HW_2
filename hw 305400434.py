# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 22:28:18 2022

@author: Elchai Refoua
"""

def reverse(sentence , reverse_word) :
   words = sentence.split()
  # if (reverse_word not in enumerate(words)) :
    #   return ("The word was not found")
   if (isinstance(reverse_word, str) == False):
       return("invalid input")
   for word in words:
       if word == reverse_word:
           words[word]=word[::-1]
           break

   return words

#sentence=input ("enter sentence :")   
#reverse_word=input ("enter reverse_word :")

#print(reverse(sentence, reverse_word))
#print(reverse_word)

print(reverse("I like apples and I also like bananas", "also"))