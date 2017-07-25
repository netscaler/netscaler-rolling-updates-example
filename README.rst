Synopsis
--------

This repository contains a sample Ansible playbook that
demonstrates how to make a "rolling release" of a load
balanced service.

This example uses docker containers and Netscaler CPX 11.1
to demonstrate the process.

The examples are also applicable for other form factors of Netscaler.

All configuration and changes will happen on the local machine
that will run the playbooks.

The tutorial is hosted at `readthedocs`_.

.. _readthedocs: http://netscaler-ansible.readthedocs.io/en/latest/usage/rolling_upgrades.html

Dependencies
------------

Ansible
+++++++

Install `Ansible`_.

Module dependencies
+++++++++++++++++++

Install the `netscaler ansible modules`_


.. _Ansible: http://docs.ansible.com/ansible/intro_installation.html
.. _netscaler ansible modules: https://github.com/citrix/netscaler-ansible-modules
