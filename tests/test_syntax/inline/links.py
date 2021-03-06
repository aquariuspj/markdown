# -*- coding: utf-8 -*-
"""
Python Markdown

A Python implementation of John Gruber's Markdown.

Documentation: https://python-markdown.github.io/
GitHub: https://github.com/Python-Markdown/markdown/
PyPI: https://pypi.org/project/Markdown/

Started by Manfred Stienstra (http://www.dwerg.net/).
Maintained for a few years by Yuri Takhteyev (http://www.freewisdom.org).
Currently maintained by Waylan Limberg (https://github.com/waylan),
Dmitry Shachnev (https://github.com/mitya57) and Isaac Muse (https://github.com/facelessuser).

Copyright 2007-2018 The Python Markdown Project (v. 1.7 and later)
Copyright 2004, 2005, 2006 Yuri Takhteyev (v. 0.2-1.6b)
Copyright 2004 Manfred Stienstra (the original version)

License: BSD (see LICENSE.md for details).
"""

from markdown.test_tools import TestCase


class TestAdvancedLinks(TestCase):

    def test_nested_square_brackets(self):
        self.assertMarkdownRenders(
            """[Text[[[[[[[]]]]]]][]](http://link.com) more text""",
            """<p><a href="http://link.com">Text[[[[[[[]]]]]]][]</a> more text</p>"""
        )

    def test_nested_round_brackets(self):
        self.assertMarkdownRenders(
            """[Text](http://link.com/(((((((()))))))())) more text""",
            """<p><a href="http://link.com/(((((((()))))))())">Text</a> more text</p>"""
        )

    def test_uneven_brackets_with_titles1(self):
        self.assertMarkdownRenders(
            """[Text](http://link.com/("title") more text""",
            """<p><a href="http://link.com/(" title="title">Text</a> more text</p>"""
        )

    def test_uneven_brackets_with_titles2(self):
        self.assertMarkdownRenders(
            """[Text](http://link.com/('"title") more text""",
            """<p><a href="http://link.com/('" title="title">Text</a> more text</p>"""
        )

    def test_uneven_brackets_with_titles3(self):
        self.assertMarkdownRenders(
            """[Text](http://link.com/("title)") more text""",
            """<p><a href="http://link.com/(" title="title)">Text</a> more text</p>"""
        )

    def test_uneven_brackets_with_titles4(self):
        self.assertMarkdownRenders(
            """[Text](http://link.com/( "title") more text""",
            """<p><a href="http://link.com/(" title="title">Text</a> more text</p>"""
        )

    def test_uneven_brackets_with_titles5(self):
        self.assertMarkdownRenders(
            """[Text](http://link.com/( "title)") more text""",
            """<p><a href="http://link.com/(" title="title)">Text</a> more text</p>"""
        )

    def test_mixed_title_quotes1(self):
        self.assertMarkdownRenders(
            """[Text](http://link.com/'"title") more text""",
            """<p><a href="http://link.com/'" title="title">Text</a> more text</p>"""
        )

    def test_mixed_title_quotes2(self):
        self.assertMarkdownRenders(
            """[Text](http://link.com/"'title') more text""",
            """<p><a href="http://link.com/&quot;" title="title">Text</a> more text</p>"""
        )

    def test_mixed_title_quotes3(self):
        self.assertMarkdownRenders(
            """[Text](http://link.com/with spaces'"and quotes" 'and title') more text""",
            """<p><a href="http://link.com/with spaces" title="&quot;and quotes&quot; 'and title">"""
            """Text</a> more text</p>"""
        )

    def test_mixed_title_quotes4(self):
        self.assertMarkdownRenders(
            """[Text](http://link.com/with spaces'"and quotes" 'and title") more text""",
            """<p><a href="http://link.com/with spaces'" title="and quotes&quot; 'and title">Text</a> more text</p>"""
        )

    def test_mixed_title_quotes5(self):
        self.assertMarkdownRenders(
            """[Text](http://link.com/with spaces '"and quotes" 'and title') more text""",
            """<p><a href="http://link.com/with spaces" title="&quot;and quotes&quot; 'and title">"""
            """Text</a> more text</p>"""
        )

    def test_mixed_title_quotes6(self):
        self.assertMarkdownRenders(
            """[Text](http://link.com/with spaces "and quotes" 'and title') more text""",
            """<p><a href="http://link.com/with spaces &quot;and quotes&quot;" title="and title">"""
            """Text</a> more text</p>"""
        )

    def test_single_quote(self):
        self.assertMarkdownRenders(
            """[test](link"notitle)""",
            """<p><a href="link&quot;notitle">test</a></p>"""
        )

    def test_angle_with_mixed_title_quotes(self):
        self.assertMarkdownRenders(
            """[Text](<http://link.com/with spaces '"and quotes"> 'and title') more text""",
            """<p><a href="http://link.com/with spaces '&quot;and quotes&quot;" title="and title">"""
            """Text</a> more text</p>"""
        )
