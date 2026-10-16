# Contributing

Issues and pull requests are welcome.

## Philosophy

This tool is deliberately zero-dependency (stdlib only) and single-file where possible. Please don't open a PR adding a third-party package unless it removes significantly more complexity than it adds — that's a design constraint, not an oversight.

## Before opening a PR

1. Run the test suite (`python3 test_*.py`) and make sure it passes.
2. If you're adding a feature, add a test for it in the same file.
3. Keep the README's usage examples in sync with any CLI flag changes.

## Bug reports

Please include: the command you ran, the input file (or a minimal reproduction), what you expected, and what actually happened.
