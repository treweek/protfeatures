import seq_features

def test_n_neg():
    """Perform unit tests on seq_features.n_neg."""

    assert seq_features.n_neg('E') == 1
    assert seq_features.n_neg('D') == 1
    assert seq_features.n_neg('') == 0
    assert seq_features.n_neg('ACKLWTTAE') == 1
    assert seq_features.n_neg('DDDDEEEE') == 8
    assert seq_features.n_neg('acklwttae') == 1
