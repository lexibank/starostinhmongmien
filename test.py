def test_valid(cldf_dataset, cldf_logger):
    assert cldf_dataset.validate(log=cldf_logger)


def test_forms(cldf_dataset):
    assert len(list(cldf_dataset["FormTable"])) == 1827
    assert any(f["Form"] == "l̥i̯o35" for f in cldf_dataset["FormTable"])


def test_parameters(cldf_dataset):
    assert len(list(cldf_dataset["ParameterTable"])) == 110


def test_languages(cldf_dataset):
    assert len(list(cldf_dataset["LanguageTable"])) == 20


def test_cognates(cldf_dataset):
    assert len(list(cldf_dataset["CognateTable"])) == 1827
    assert any(f["Form"] == "ka3=sʰa3" for f in cldf_dataset["CognateTable"])
