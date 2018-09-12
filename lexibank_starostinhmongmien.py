# coding=utf-8
from __future__ import unicode_literals, print_function

from pylexibank.providers import tob
from pylexibank.dataset import Metadata


class Dataset(tob.TOB):
    dir = Path(__file__).parent
    pages = 6
    name = 'hmo'
    dset = 'hmo'
