from setuptools import setup
import json


with open("metadata.json", encoding="utf-8") as fp:
    metadata = json.load(fp)


setup(
    name="lexibank_starostinhmongmien",
    description=metadata["title"],
    license=metadata.get("license", ""),
    url=metadata.get("url", ""),
    py_modules=["lexibank_starostinhmongmien"],
    include_package_data=True,
    zip_safe=False,
    entry_points={"lexibank.dataset": ["starostinhmongmien=lexibank_starostinhmongmien:Dataset"]},
    install_requires=["pylexibank>=3.0"],
)
