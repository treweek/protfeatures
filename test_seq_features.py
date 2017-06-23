import seq_features
import pytest

def test_n_neg():
    """Perform unit tests on seq_features.n_neg."""

    assert seq_features.n_neg('E') == 1
    assert seq_features.n_neg('D') == 1
    assert seq_features.n_neg('') == 0
    assert seq_features.n_neg('ACKLWTTAE') == 1
    assert seq_features.n_neg('DDDDEEEE') == 8
    assert seq_features.n_neg('acklwttae') == 1

def test_n_neg_for_invalid_amino_acid():
    with pytest.raises(RuntimeError) as excinfo:
        seq_features.n_neg('Z')
    excinfo.match("Z is not a valid amino acid")
