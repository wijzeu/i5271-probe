"""Minimal health helpers for the probe service."""

def healthy() -> bool:
    return True

def status_line() -> str:
    return "ok" if healthy() else "degraded"
