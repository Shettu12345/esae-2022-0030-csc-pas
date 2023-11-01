Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def reverse_string(input_string):
...     reversed_string = ""
...     for char in input_string:
...         if not char.isdigit():
...             reversed_string = char + reversed_string
...     return reversed_string
...
>>> input_string="shettu2023"
>>> reverse_string(input_string)
'UTTEHS'