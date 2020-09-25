import pytest
import knot_sim.simulator_core.thing_parser as thing_parser

ACCEPTABLE_DIFFERENCE = 0.000000000000001


def test_create_modbus_server_bank_from_invalid_raw_returns_empty():
    server_bank = thing_parser.create_modbus_server_bank_from_raw("Invalid")
    assert server_bank == {}
