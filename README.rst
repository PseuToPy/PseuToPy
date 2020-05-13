|Build Status| |Documentation Status| |MIT License|

Home
========

General description
-------------------

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
------------

Use the package manager `pip <https://pip.pypa.io/en/stable/>`__ to install
PseuToPy.

.. code-block:: shell

   pip install pseutopy

This will also install the following dependencies:

- `textX <http://textx.github.io/textX/stable/>`__
- `astor <https://astor.readthedocs.io/en/latest/>`__
- `pytest <https://docs.pytest.org/en/latest/>`__

Usage
_____

You can import PseuToPy and use it within your own project.

Testing
_______

To run unit tests, run ``pytest`` at the root of the project.

Authors and acknowledgment
__________________________

I particularly wish to thank `@Houguiram <https://github.com/Houguiram>`__,
`@TheOnlyMrFlow <https://github.com/TheOnlyMrFlow>`__, and
`@EricSombroek <https://github.com/EricSombroek>`__ for their initial
contributions to this project, which greatly helped me in getting to this stage.

License
_______

`MIT <https://choosealicense.com/licenses/mit/>`__

.. |Build Status| image:: https://travis-ci.com/PseuToPy/PseuToPy.svg?branch=master
   :target: https://travis.com/PseuToPy/PseuToPy
.. |MIT License| image:: https://img.shields.io/apm/l/atomic-design-ui.svg?
   :target: https://github.com/tterb/atomic-design-ui/blob/master/LICENSEs 
.. |Documentation Status| image:: https://readthedocs.org/projects/pseutopy/badge/?version=latest 
   :target: https://pseutopy.readthedocs.io/en/latest/?badge=latest
