"""Flask app for dynamic URLs (factorial example)."""

from __future__ import annotations

from flask_dynamic_url.app import app, calculate_factorial, main

__all__ = ["app", "calculate_factorial", "main"]

__version__ = "0.1.0"
