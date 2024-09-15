# Example RST Document

This is a paragraph in reStructuredText. It is a simple way to write
formatted text.

## Headings

### This is a section heading

#### This is a subsection heading

## Lists

- This is a bullet list item.
- Another bullet list item.

1.  This is an enumerated list item.
2.  Another enumerated list item.

## Links

Here is an inline link to [Google](https://www.google.com).

Here is an anonymous hyperlink reference:

[Python official website](https://www.python.org)

## Images

Here is an image:

![element](https://docusaurus.io/zh-CN/img/undraw_typewriter.svg)

![](https://docusaurus.io/zh-CN/img/docusaurus.svg)

## Code Blocks

Here is a block of code:

``` python
def hello_world():
    print("Hello, World!")
```

## Tables

Here is a simple table:

<table style="width:32%;">
<colgroup>
<col style="width: 16%" />
<col style="width: 15%" />
</colgroup>
<thead>
<tr class="header">
<th>Header 1</th>
<th>Header 2</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Row 1, Column 1</td>
<td>Row 1, Column 2</td>
</tr>
<tr class="even">
<td>Row 2, Column 1</td>
<td>Row 2, Column 2</td>
</tr>
</tbody>
</table>

## 单元格合并

## 行合并

<table style="width:86%;">
<colgroup>
<col style="width: 25%" />
<col style="width: 61%" />
</colgroup>
<tbody>
<tr class="odd">
<td rowspan="2"><blockquote>
<p>Header 1</p>
</blockquote>
<dl>
<dt>=================</dt>
<dd>
<p>Row 1, Col 1</p>
</dd>
</dl></td>
<td rowspan="2"><blockquote>
<p>Header 2 | Header 3 |</p>
</blockquote>
<dl>
<dt>============+============+</dt>
<dd>
<p>Row 1, Col 2 and 3 merged together</p>
</dd>
</dl></td>
</tr>
<tr class="even">
</tr>
<tr class="odd">
<td colspan="2">Row 2, Col 1 and 2 merged together | Row 2, Col 3</td>
</tr>
<tr class="even">
<td>Row 3, Col 1</td>
<td>Row 3, Col 2 | Row 3, Col 3 |</td>
</tr>
</tbody>
</table>

## 列合并

<table style="width:72%;">
<colgroup>
<col style="width: 23%" />
<col style="width: 25%" />
<col style="width: 23%" />
</colgroup>
<thead>
<tr class="header">
<th>Header 1</th>
<th colspan="2">Header 2 | Header 3</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Row 1, Col 1</td>
<td>Row 1, Col 2</td>
<td>Row 1, Col 3</td>
</tr>
<tr class="even">
<td colspan="2" rowspan="2">Row 2, Col 1 (merged with below)</td>
<td></td>
</tr>
<tr class="odd">
<td>Row 2, Col 3</td>
</tr>
<tr class="even">
<td>Row 3, Col 1</td>
<td>Row 3, Col 2</td>
<td>Row 3, Col 3</td>
</tr>
</tbody>
</table>

## Admonitions

<div class="note">

<div class="title">

Note

</div>

This is a note.

</div>

<div class="warning">

<div class="title">

Warning

</div>

This is a warning.

</div>

## Footnotes

This is a sentence with a footnote reference[1].

[1] This is the footnote.
