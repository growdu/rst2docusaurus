======================
Example RST Document
======================

This is a paragraph in reStructuredText. It is a simple way to write formatted text.

Headings
========

This is a section heading
--------------------------

This is a subsection heading
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Lists
=====

- This is a bullet list item.
- Another bullet list item.

1. This is an enumerated list item.
2. Another enumerated list item.

Links
=====

Here is an inline link to `Google <https://www.google.com>`_.

Here is an anonymous hyperlink reference:

`Python official website`__

__ https://www.python.org

Images
======

Here is an image:

.. image:: https://docusaurus.io/zh-CN/img/undraw_typewriter.svg
   :alt: element

.. figure:: https://docusaurus.io/zh-CN/img/docusaurus.svg

Code Blocks
===========

Here is a block of code:

.. code-block:: python

    def hello_world():
        print("Hello, World!")

Tables
======

Here is a simple table:

+-----------+----------+
| Header 1  | Header 2 |
+===========+==========+
| Row 1,    | Row 1,   |
| Column 1  | Column 2 |
+-----------+----------+
| Row 2,    | Row 2,   |
| Column 1  | Column 2 |
+-----------+----------+

单元格合并
==========

行合并
===========

+-----------------+------------+------------+
| Header 1        | Header 2   | Header 3   |
+=================+============+============+
| Row 1, Col 1    | Row 1, Col 2 and 3 merged together        |
+-----------------+-------------------------+----------------+
| Row 2, Col 1 and 2 merged together         | Row 2, Col 3   |
+-----------------+------------+------------+
| Row 3, Col 1    | Row 3, Col 2 | Row 3, Col 3 |
+-----------------+------------+------------+

列合并
==========

+----------------+----------------+----------------+
| Header 1       | Header 2        | Header 3       |
+================+=================+================+
| Row 1, Col 1   | Row 1, Col 2    | Row 1, Col 3   |
+----------------+-----------------+----------------+
| Row 2, Col 1 (merged with below) |
+                                  +----------------+
|                                  | Row 2, Col 3   |
+----------------+-----------------+----------------+
| Row 3, Col 1   | Row 3, Col 2    | Row 3, Col 3   |
+----------------+-----------------+----------------+



Admonitions
===========

.. note::

   This is a note.

.. warning::

   This is a warning.

Footnotes
=========

This is a sentence with a footnote reference [1]_.

.. [1] This is the footnote.
