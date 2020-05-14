|Build Status| |Documentation Status| |MIT License|

****
Home
****

General description
###################

PseuToPy is a Python library which defines a grammar for a pseudocode-based
pseudocode. With this grammar, PseuToPy is then able to take instructions
written in pseudocode and converts it into the equivalent Python instructions.

PseuToPy is designed for educational purposes. In that sense, PseuToPy is suited
to anyone embarking in the journey of learning Python programming by offering a
relaxed syntax and a grammar that very much resembles the grammar of a natural
language.

Currently, PseuToPy only exists in English, but more languages (French, Italian,
Spanish) will arrive soon.

Installation
############

Use the package manager `pip <https://pip.pypa.io/en/stable/>`__ to install
PseuToPy.

.. code-block:: shell

   pip install pseutopy

This will also install the following dependencies:

- `textX <http://textx.github.io/textX/stable/>`__
- `astor <https://astor.readthedocs.io/en/latest/>`__
- `pytest <https://docs.pytest.org/en/latest/>`__

Usage
#####

You can import PseuToPy and use it within your own project.

.. code-block:: none

   import astor
   from pseutopy.pseutopy import PseuToPy

   pseutopy = PseuToPy()

   # These two lines generate the AST of the pseudocode instructions
   convert_from_string = pseutopy.convert_from_string("""
       declare myVar
       set myVar to 3 plus 1
       """)
   convert_from_file = pseutopy.convert_from_file("./path/to/file")

   # You can then convert these AST into Python instructions with astor
   print(astor.to_source(convert_from_string))
   print(astor.to_source(convert_from_file))

   # For example, the result of print(astor.to_source(convert_from_string)) is:
   # myVar = None
   # myVar = 3 + 1

Or you can use the CLI utility that ships with this project.

.. code-block:: none

   python cli.py --help

   # This is the output of the help flag
   usage: pseutopy.py [-h] [-f | -s] [-a] [-q] input

   A pseudocode to Python converter written in Python using textX.

   positional arguments:
   input         Pseudocode input to be converted into Python

   optional arguments:
     -h, --help    show this help message and exit
     -f, --file    Input is now expected to be a file
     -s, --string  Input is now expected to be a string (default)
     -a, --ast     Prints out the generated Python AST
     -q, --quiet   Don't print the generated Python code


Testing
#######

To run unit tests, run ``pytest`` at the root of the project.

Authors and acknowledgment
##########################

I particularly wish to thank `@Houguiram <https://github.com/Houguiram>`__,
`@TheOnlyMrFlow <https://github.com/TheOnlyMrFlow>`__, and
`@EricSombroek <https://github.com/EricSombroek>`__ for their initial
contributions to this project, which greatly helped me in getting to this stage.

License
#######

`MIT <https://choosealicense.com/licenses/mit/>`__

.. |Build Status| image:: https://travis-ci.com/PseuToPy/PseuToPy.svg?branch=master
   :target: https://travis.com/PseuToPy/PseuToPy
.. |MIT License| image:: https://img.shields.io/apm/l/atomic-design-ui.svg?
   :target: https://github.com/tterb/atomic-design-ui/blob/master/LICENSEs 
.. |Documentation Status| image:: https://readthedocs.org/projects/pseutopy/badge/?version=latest 
   :target: https://pseutopy.readthedocs.io/en/latest/?badge=latest
