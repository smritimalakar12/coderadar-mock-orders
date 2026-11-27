from payments.client import charge


def test_charge_total():
    assert charge("o1", 10)["amount"] == 10
