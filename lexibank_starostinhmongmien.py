import pathlib

from pylexibank.providers import tob


class Dataset(tob.TOB):
    dir = pathlib.Path(__file__).parent
    id = "starostinhmongmien"
    pages = 6
    name = "hmo"
    dset = "hmo"
