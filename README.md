# Aerominal Dev Tools Kit

Minimal diagnostic and performance suite for Aerominal.

## Usage

```bash
# List all tools
python aerominal_tools.py list

# Run full suite
python aerominal_tools.py run

# Run specific category (diag, perf, visual)
python aerominal_tools.py run -c diag
```

## Structure

- `aerominal_tools.py`: Main entry point.
- `run_suite.py`: Test runner engine.
- `tools/`:
    - `diag/`: System & config audits.
    - `perf/`: Benchmarks & stress tests.
    - `visual/`: Terminal rendering tests.

## Individual Tools
You can also run any script in the `tools/` subdirectories directly with `python`.
