.. toctree::
   :caption: Installation
   :maxdepth: 2

************
Installation
************

The easiest way to install PseuToPy is to use ``pip``:

.. code-block:: none

   pip install pseutopy

This should install the latest version of PseuToPy and its dependencies.
PseuToPy relies on the following Python packages:

* `textX <http://textx.github.io/textX/stable/>`__
* `astor <https://astor.readthedocs.io/en/latest/>`__
* `pytest <https://docs.pytest.org/en/latest/>`__

PseuToPy uses ``pytest`` to run unit tests. PseuToPy is tested for Python
versions 3.5+.

To check that the installation worked correctly, you can type the following
command in your terminal. The output should inform you of the version you have
installed on your machine.

.. code-block:: none

   pip show pseutopy
