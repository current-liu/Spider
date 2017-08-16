#!/usr/bin/env
# coding:utf-8
"""
Created on 2017/8/16 0016 下午 4:30

base Info
"""
from unittest import TestCase

from mafengwo.member import h_parser
from mafengwo.member.action import doc_e

__author__ = 'Administrator'
__version__ = '1.0'


class TestGet_member(TestCase):
    def test_parser_member(self):
        h_parser.parser_member(doc_e)
