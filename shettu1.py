Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import re
>>> def find_and_replace(pattern, replace, string):
...     match = re.search(pattern, string)
...     if match:
...         return re.sub(pattern, replace, string)
...     else:
...         return "No match found."
... 
...     
>>> string = "The quick brown fox jumps over the lazy cat."
>>> pattern = r"\b\w{5}\b"
>>> replace = "cat"
>>> print(find_and_replace(pattern, replace, string))
The dog dog fox cat over the lazy cat.