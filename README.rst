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

Dependencies
------------

Netscaler CPX
+++++++++++++

Download the 11.1 version of Netscaler CPX from `Citrix`_

Follow the instructions to have the image built on your local
machine.

The image will be utilized by the setup playbook to create a CPX
instance.

.. _Citrix: https://www.citrix.com/downloads

Ansible
+++++++

Install `Ansible`_.


Module dependencies
+++++++++++++++++++

Our playbooks utilize the `netscaler ansible modules`_ along with
the docker modules to setup the testbed.

To install the dependencies needed by these modules in a virtual environment
do the following.

.. code-block:: bash

    git clone https://github.com/citrix/netscaler-rolling-updates-example.git
    cd netscaler-rolling-updates-example/deps
    mkvirtualenv myenv
    pip install -r requirements.txt

After the execution of the above commands the ``myenv`` virtual environment
will have all dependencies needed to run the playbooks.


.. _Ansible: http://docs.ansible.com/ansible/intro_installation.html
.. _netscaler ansible modules: https://github.com/citrix/netscaler-ansible-modules


Docker image
++++++++++++

Also there is a custom docker image that bootstraps a simple http service
utilizing Flask to showcase the effects of the rolling update.

To create the image on your local machine change directory to the repo
check out and do the following:

.. code-block:: bash

    docker build -t myapp myapp

It is important to give the image the name ``myapp`` otherwise the plays
will not be able to create the web servers.
