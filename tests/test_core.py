"""Tests for life-betterment-simulation core module."""

from life_betterment_simulation.core import main


def test_main(capsys):
    """Test main entry point."""
    main()
    captured = capsys.readouterr()
    assert "life-betterment-simulation" in captured.out
