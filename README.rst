=========================
Sphinx Documentation Test
=========================

This repository shows an implementation of auto documentation using **github actions**, **sphinx**, and **github-pages**.

The documentation is automatically hosted on each commit using Github Pages. 

Documentation: `https://divykj.github.io/sphinx-docs-test <https://divykj.github.io/sphinx-docs-test/>`_


Steps
~~~~~

1. Create empty gh-pages branch

.. code-block:: shell

    git checkout --orphan gh-pages
    git rm -rf .
    git commit --allow-empty -m "root commit"
    git push origin gh-pages

2. Make docs folder with basic conf.py

.. code-block:: shell
    
    sphinx-quickstart . --no-makefile --no-batchfile

3. Add index.rst and other pages

.. code-block:: shell

    sphinx-apidoc --force --no-toc --module-first -o docs sphinx_docs_test

4. Build github action (using `peaceiris/actions-gh-pages <https://github.com/peaceiris/actions-gh-pages/>`_)

.. code-block:: shell

    sphinx-build docs public -b dirhtml

