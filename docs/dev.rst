Development Setup
=================

Initial setup on Arch Linux
---------------------------

.. code-block:: bash

   pyenv virtualenv 3.7.4 fundoshi
   pyenv activate fundoshi
   poetry install


Routine stuff
-------------

.. code-block:: bash

   make test
   make realtest
   make docs
   ... (see Makefile)
