"""
Nose tests for acp_times.py
"""

from acp_times import open_time, close_time
import arrow

import nose    # Testing framework
import logging
logging.basicConfig(format='%(levelname)s:%(message)s',
                    level=logging.WARNING)
log = logging.getLogger(__name__)

dummy_start_time = arrow.get('2020-01-03T00:00:00+00:00')

expected_60km_open = arrow.get('2020-01-03T01:46:00+00:00')
def test_60km_control_open():
    """
    Tests within the 1st bracket (0-200km)
    """
    assert open_time(60, 200, dummy_start_time) == expected_60km_open


expected_40km_close = arrow.get('2020-01-03T03:00:00+00:00')
def test_40km_control_close():
    """
    Tests whether the French variation is in place.
    Control points < 60km should be treated differently
    Specifically, divided by 20 rather than 15 and having 1 hour added

    *see "Oddities" at the bottom*
    https://rusa.org/pages/acp-brevet-control-times-calculator
    """
    assert close_time(40, 200, dummy_start_time) == expected_40km_close


expected_205km_open = arrow.get('2020-01-03T05:53:00+00:00')
def test_205km_control_open():
    """
    Tests whether 205km control point open time is treated properly
    (as 200km rather than 205)

    See Example 1 @ https://rusa.org/pages/acp-brevet-control-times-calculator
    """
    assert open_time(205, 200, dummy_start_time) == expected_205km_open


expected_200km_close = arrow.get('2020-01-03T13:30:00+00:00')
def test_200km_control_close():
    """
    Tests weird close time at 200km
    https://rusa.org/pages/rulesForRiders
    Check Article 9 at this link for more info
    """
    assert close_time(200, 200, dummy_start_time) == expected_200km_close


expected_550km_open = arrow.get('2020-01-03T17:08:00+00:00')
def test_550km_control_open():
    """
    Tests control point in 3rd bracket to ensure each subsequent
    brackets min speed is being used properly.

    See https://rusa.org/pages/acp-brevet-control-times-calculator
    """
    assert open_time(550, 600, dummy_start_time) == expected_550km_open
