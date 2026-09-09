"""Curriculum content + importer.

The DB-backed curriculum backbone (course → module → lesson → content /
resource / competency / practice item) for first-year university courses.
``content.py`` holds the structured bundle; ``seed.py`` is the idempotent
importer that turns it into rows (also exposed as a CLI for adding future
lessons without touching code).
"""
