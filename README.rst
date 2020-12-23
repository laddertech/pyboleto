========
pyboleto - Fork mantido por Ladder Tecnologia
========

pyboleto é um projeto python para gerar boletos de cobrança.

O projeto original pode ser encontrado aqui:
https://github.com/eduardocereto/pyboleto
e a origem deste fork aqui:
https://github.com/Trust-Code/python-boleto


.. contents::
    :local:

.. _pyboleto-implemented-bank:

Bancos implementados
=================

You can help writing code for more banks or printing and testing current
implementations.

For now here's where we are.

 +----------------------+----------------+-----------------+------------+
 | **Banco**            | **Carteira /** | **Implementado**| **Testado**|
 |                      | **Convenio**   |                 |            |
 +======================+================+=================+============+
 | **Banco do Brasil**  | 18             | Yes             | Yes        |
 +----------------------+----------------+-----------------+------------+
 | **Banrisul**         | x              | Yes             | Yes        |
 +----------------------+----------------+-----------------+------------+
 | **Bradesco**         | 06, 03         | Yes             | Yes        |
 +----------------------+----------------+-----------------+------------+
 | **Cresol**           | 09, 4950705    | Yes             | Yes        |
 +----------------------+----------------+-----------------+------------+
 | **Caixa Economica**  | SR             | Yes             | No         |
 +----------------------+----------------+-----------------+------------+
 | **HSBC**             | CNR, CSB       | Yes             | No         |
 +----------------------+----------------+-----------------+------------+
 | **Itau**             | 157            | Yes             | Yes        |
 +----------------------+----------------+-----------------+------------+
 | **Itau**             | 175, 174, 178, | Yes             | No         |
 |                      | 104, 109       |                 |            |
 +----------------------+----------------+-----------------+------------+
 | **Santander**        | 102            | Yes             | Yes        |
 +----------------------+----------------+-----------------+------------+
 | **Santander**        | 101, 201       | Yes             | No         |
 +----------------------+----------------+-----------------+------------+
 | **Sicoob**           | 1              | Yes             | Yes        |
 +----------------------+----------------+-----------------+------------+
 | **Cecred**           | 1              | Yes             | Yes        |
 +----------------------+----------------+-----------------+------------+

.. _pyboleto-docs:

Documentation
=============


.. _pyboleto-installation:

Installation
============

You can install pyboleto from source.

To install using pip,::

    $ pip install -e git://github.com/fabiothz/pyboleto.git#egg=pyboleto


.. _pyboleto-installing-from-source:

Downloading and installing from source
--------------------------------------

Download the latest version of pyboleto from
http://github.com/fabiothz/pyboleto/

You can install it by doing the following,::

    $ tar xvfz pyboleto-0.0.0.tar.gz
    $ cd pyboleto-0.0.0
    $ python setup.py build
    # python setup.py install # as root

.. _pyboleto-installing-from-hg:

Using the development version
-----------------------------

You can clone the repository by doing the following::

    $ git clone https://github.com/fabiothz/pyboleto.git

.. _pyboleto-unittests:

Executing unittests
===================

You need either setuptools or distribute in order to execute the tests. Chances are you already have one or another. You also need `pdftohtml`_.::

    $ cd pyboleto
    $ python setup.py test


.. _pdftohtml: http://poppler.freedesktop.org/

.. _pyboleto-license:

License
=======

This software is licensed under the `New BSD License`. See the ``LICENSE``
file in the top distribution directory for the full license text.

.. vim:tw=0:sw=4:et
