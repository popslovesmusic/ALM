from alm.constants import L2_CACHE_BUDGET_BYTES
from alm.state import assert_cache_residency, stencil_payload_bytes


def test_residency_budget_enforced():
    payload = assert_cache_residency()
    assert payload == stencil_payload_bytes()
    assert payload <= L2_CACHE_BUDGET_BYTES
