import pytest
from project import get_specification as get_spec, get_unit, get_option
from exceptions import InvalidSpecification, InvalidOption


def test_get_spec(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "120")
    spec = get_spec("Impedance")
    assert spec == 120

    monkeypatch.setattr("builtins.input", lambda _: "0")
    spec = get_spec("Impedance")
    assert spec == 0

    monkeypatch.setattr("builtins.input", lambda _: "8.5")
    spec = get_spec("Impedance")
    assert spec == 8.5

    with pytest.raises(InvalidSpecification):
        monkeypatch.setattr("builtins.input", lambda _: "-30")
        spec = get_spec("Impedance")

    with pytest.raises(InvalidSpecification):
        monkeypatch.setattr("builtins.input", lambda _: "cat")
        spec = get_spec("Impedance")


def test_get_unit(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "1")
    option = get_unit()
    assert option == True

    monkeypatch.setattr("builtins.input", lambda _: "2")
    option = get_unit()
    assert option == False

    with pytest.raises(InvalidOption):
        monkeypatch.setattr("builtins.input", lambda _: "3")
        option = get_unit()

    with pytest.raises(InvalidOption):
        monkeypatch.setattr("builtins.input", lambda _: "0")
        option = get_unit()

    with pytest.raises(InvalidOption):
        monkeypatch.setattr("builtins.input", lambda _: "-1")
        option = get_unit()

    with pytest.raises(InvalidOption):
        monkeypatch.setattr("builtins.input", lambda _: "cat")
        option = get_unit()


def test_get_option(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "1")
    option = get_option()
    assert option == "1"

    monkeypatch.setattr("builtins.input", lambda _: "2")
    option = get_option()
    assert option == "2"

    monkeypatch.setattr("builtins.input", lambda _: "3")
    option = get_option()
    assert option == "3"

    with pytest.raises(InvalidOption):
        monkeypatch.setattr("builtins.input", lambda _: "4")
        option = get_option()

    with pytest.raises(InvalidOption):
        monkeypatch.setattr("builtins.input", lambda _: "0")
        option = get_option()

    with pytest.raises(InvalidOption):
        monkeypatch.setattr("builtins.input", lambda _: "-1")
        option = get_option()

    with pytest.raises(InvalidOption):
        monkeypatch.setattr("builtins.input", lambda _: "cat")
        option = get_option()
