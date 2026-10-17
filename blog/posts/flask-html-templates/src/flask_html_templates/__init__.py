"""Flask app for HTML templates with primality testing."""

from __future__ import annotations

from flask_html_templates.app import app, display_primarily, is_prime, main

__all__ = ["app", "display_primarily", "is_prime", "main"]

__version__ = "0.1.0"
