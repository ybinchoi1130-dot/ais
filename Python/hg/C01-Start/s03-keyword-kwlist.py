# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 12:18:51 2026

@author: Solx
"""

# s03-keyword-kwlist.py

#%%

import sys
print(sys.version)

#%%

"""
3.13.14 | packaged by Anaconda, Inc. 
| (main, Jul  9 2026, 14:26:41) [MSC v.1942 64 bit (AMD64)]
"""

#%%

import keyword
print(keyword.kwlist)

#%%

# keyword : 35개
"""
['False',    'None',    'True',  'and',   'as', 
 'assert',   'async',   'await', 'break', 'class', 
 'continue', 'def',     'del',   'elif',  'else', 
 'except',   'finally', 'for',   'from',  'global', 
 'if',       'import',  'in',    'is',    'lambda', 
 'nonlocal', 'not',     'or',    'pass',  'raise', 
 'return',   'try',     'while', 'with',  'yield']
"""

