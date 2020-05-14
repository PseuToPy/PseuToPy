=======
.. toctree::
   :maxdepth: 2
=======

********
Features
********

Grammar
#######

Types of instructions
*********************

The grammar of the pseudocode is defined thanks to
`textX <http://textx.github.io/textX/stable/>`__. In the current version, we
only support pseudocode based on English words. This is why there is currently
just a single ``pseudocode.tx`` grammar file.

The pseudocode grammar is based on the Python 3.8 grammar specification, which
can be found `here <https://docs.python.org/3/reference/grammar.html>`__,
completed with the definition of pseudocode keywords. This means that PseuToPy
would consider some Python instructions to be valid pseudocode instructions.
**More precisely, every instruction written in pseudocode and accepted by PseuToPy
will also be accepted if written in Python.**

The grammar currently allows to write the following types of instructions:

* Variable declaration, assignment, and manipulations (primitive variable or
  composite data types, except for classes).
* Common algebraic operations.
* Common comparison and boolean operations.
* Control structures.
* Function declarations and calls.
* Standard ``print`` and ``input`` functions, with the possibility to cast the
  latter with ``int()`` or ``float()``.

For a more detailed view of the grammar, see :ref:`grammar_specification`.

Grammar flexibility
*******************

The grammar is defined to be flexible in its syntax. Indeed, the somewhat rigid
syntax of programming languages is a difficulty commonly encountered by
programming beginners. As a consequence, we authorize some instructions to
accept multiple spellings. For example, the following instructions are all valid
pseudocode instructions.

.. code-block:: none

   set a to 1 minus 2
   b = 1 + 3
   if a is lower than b then
       print "Hello, world!"
   else if a > b then:
       display("Hello again!")
   else:
       show ("Hello once more!")
   end


Note that the instructions do not need to be indented or to start on a new line.
The example above could have been written on a single line, and the instructions
would still be valid.

To better understand the possibilities provided with this grammar, we highly
suggest that you take a look at the ``pseudocode.tx`` grammar specification file
and at `textX <http://textx.github.io/textX/stable/>`__.

Transpiler
##########

Apart from the grammar file, this package is composed of the following elements:

* ``pseutopy.py``, which contains the ``PseuToPy`` module that reads the
  grammar file and transpiles pseudocode into the equivalent Python
  instructions.
* ``generators/*.py``, which contains all the class definitions which mirror the
  grammar specifications. These class also implement a ``to_node()`` methode
  which is used to generate the corresponding AST node.


CLI commands
############

If you have cloned this repository from GitHub, you can see that the project
contains a CLI utility which allows you to quickly try out PseuToPy. Open your
terminal, go to the location of your repository, and type the following
instruction to learn how to use this CLI tool.

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

For example, you can type the following instruction and see the results:

.. code-block:: none

   python cli.py -a "declare a"

   # The output will be:
   Module(body=[Assign(targets=[Name(id='a', ctx=<class '_ast.Store'>)], value=NameConstant(value=None))])
   a = None



What's coming up next?
######################

There are lots of improvements that can be made on PseuToPy. Currently, the
following items are the ones I wish to develop in priority. Ordering does not
necessarily represent level of importance and the list of ideas is not limited
to the following elements:

* Internationalization: Programming languages almost exclusively use English
  words. But that is a big obstacle to all the non-native English speakers that
  with to initiate themselves to Computer Science and programming. This is an
  even bigger issue considering the current trend of introducing programming in
  middle and high schools, where we cannot expect pupils to have strong English
  skills.
* Data structures: The need for data structures comes quite quickly when
  teaching and learning to program. Currently, PseuToPy only has a very light
  support of data structures (i.e., we can create lists, tuples, sets, and
  dictionaries, but not on objects). More work is necessary before being able to
  use methods on data structures (or on objects as well).
* Python Standard Library: The pseudocode grammar allows to write simple
  instructions commonly encountered when learning to program. When the learner
  advances into more complex concepts, it might be useful to make use of
  functions provided by the Python Standard Library. This means being able to
  import packages.
