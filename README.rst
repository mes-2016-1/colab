.. -*- coding: utf-8 -*-

.. highlight:: rest

.. _colab_software:

=================================
Colab, a Software for Communities
=================================

.. image:: https://travis-ci.org/colab/colab.svg?branch=master
    :target: https://travis-ci.org/colab/colab

.. image:: https://coveralls.io/repos/colab/colab/badge.png?branch=master
          :target: https://coveralls.io/r/colab/colab?branch=master


What is Colab?
==============

Application that integrates existing systems to represent the contributions of the members through:

* The amendments to the Wiki trac system.

* Changes to the trac system code.

* Discussions at the mailman list.

* And other systems in the community.



Features
========

* Developed by Interlegis Communities http://colab.interlegis.leg.br/

* Written in Python http://python.org/

* Built with Django Web Framework https://www.djangoproject.com/

* Search engine with Solr https://lucene.apache.org/solr/



Installation
============

First install the dependencies and than the project it self:

.. code-block::

  pip install -e .

Development environment
-----------------------

You must install vagrant to set up the development environment. With vagrant available you should run:

.. code-block::

  vagrant up

During the process you should choose the vagrant box that you want to use. In the end you should have a virtual machine with development environment set up.



Running Colab
=============

To run Colab with development server you will have to:

1- Log in virtual machine:

.. code-block::

  vagrant ssh
  
2- Use colab virtualenv:

.. code-block::

  workon colab
  
3- Run the development server: 

.. code-block::

  colab-admin runserver 0.0.0.0:8000

Now you can access colab in your browser via http://localhost:8000

**NOTE**: In case you want to keep the configuration file else where just set the 
desired location in environment variable **COLAB_SETTINGS**.

About test
==========

How to write a test
--------------------
Inside of each folder on /vagrant/colab/<folder> you can create a folder called
"tests" and inside of it implements the code for test each file. Remember that you should create __init__.py file.
 
How to run the tests
--------------------

Follow the steps below:

1- Log in virtual machine:

.. code-block::

  vagrant ssh

2- Use colab virtualenv:

.. code-block::

  workon colab

3- Enter into colab source code directory:

.. code-block::

  cd /vagrant

4- Run tests with setup.py:

.. code-block::

  python setup.py test

How to run Acceptance Tests
---------------------------

Follow the steps below to run the acceptance tests. Perharps you may want to run the install commands with 'sudo'.

1- Log in virtual machine:

.. code-block::

  vagrant ssh

2- Use colab virtualenv:

.. code-block::

  workon colab

3- Install 'behave_django':

.. code-block::

  pip install behave_django

4- Add 'behave_django' to the django project INSTALED_APPS list, on settings.py.

5- Install selenium:

.. code-block::

  pip install selenium

6- Make sure you have the web browser Firefox installed on your VM. You can simply install it by typing:

CentOS

.. code-block::

  yum install firefox

Ubuntu

.. code-block::

  apt-get install firefox

7- Make sure that you have the X11 installed on your VM. You can install it by typing:

CentOS

.. code-block::

  yum groupinstall x11

Ubuntu

.. code-block::

  apt-get install xorg

8- Exit the VM and then enter again using this, to give the VM access to your graphic interface:

.. code-block::

  vagrant ssh -- -X

9- Use colab virtualenv:

.. code-block::

  workon colab

10- Enter into colab source code directory:

.. code-block::

  cd /vagrant

11- Run all the acceptance tests with:

.. code-block::

  colab-admin behave

To run a specific feature:

.. code-block::

  colab-admin behave /path/to/features/file.feature

12- If you try to run the behave tests and stumble in some errors because of static files (css, js, etc), try running the following to fix it:

.. code-block::

  sudo `which colab-admin` collectstatic