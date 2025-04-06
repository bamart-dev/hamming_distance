import pytest

from main import hamming_distance as hd


def test_hamming_distance_returns_diff_same_lengths():
    strand1 = "GAGCCTACTAACGGGAT"
    strand2 = "CATCGTAATGACGGCCT"

    result = hd(strand1, strand2)

    assert result == 7


def test_hamming_distance_no_diff_returns_zero():
    strand1 = "GAGCCTACTAACGGGAT"
    strand2 = "GAGCCTACTAACGGGAT"

    result = hd(strand1, strand2)

    assert result == 0


def test_hamming_distance_returns_diff_all_lower_case_bases():
    strand1 = "GAGCCTACTAACGGGAT".lower()
    strand2 = "CATCGTAATGACGGCCT".lower()

    result = hd(strand1, strand2)

    assert result == 7


def test_hamming_distance_returns_diff_strand1_lower_case_bases():
    strand1 = "GAGCCTACTAACGGGAT".lower()
    strand2 = "CATCGTAATGACGGCCT"

    result = hd(strand1, strand2)

    assert result == 7


def test_hamming_distance_returns_diff_strand2_lower_case_bases():
    strand1 = "GAGCCTACTAACGGGAT"
    strand2 = "CATCGTAATGACGGCCT".lower()

    result = hd(strand1, strand2)

    assert result == 7


def test_hamming_distance_returns_rna_message():
    strand1 = "GAGCCTACTAACGGGAT"
    strand2 = "CAUCGUAAUGACGGCCU"

    result = hd(strand1, strand2)

    assert result == "A RNA strand has been passed in."


def test_hamming_distance_strand1_empty_raises_error():
    strand1 = ""
    strand2 = "CATCGTAATGACGGCCT"

    with pytest.raises(ValueError) as err:
        hd(strand1, strand2)

    assert str(err.value) == "An empty DNA strand has been provided."


def test_hamming_distance_strand2_empty_raises_error():
    strand1 = "GAGCCTACTAACGGGAT"
    strand2 = ""

    with pytest.raises(ValueError) as err:
        hd(strand1, strand2)

    assert str(err.value) == "An empty DNA strand has been provided."


def test_hamming_distance_returns_diff_shorter_strand1():
    strand1 = "GAGCCTACTAA"
    strand2 = "CATCGTAATGACGGCCT"

    result = hd(strand1, strand2)

    assert result == 11


def test_hamming_distance_returns_diff_shorter_strand2():
    strand1 = "GAGCCTACTAACGGGAT"
    strand2 = "CATCGTAA"

    result = hd(strand1, strand2)

    assert result == 13
