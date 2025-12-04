# Testing

## Running Tests

We use `pytest` for testing.

```bash
pytest
```

## Writing Tests

*   **Unit Tests**: Place in `tests/`.
*   **CLI Tests**: Use `typer.testing.CliRunner`.

Example:
```python
from typer.testing import CliRunner
from structum.cli.main import app

runner = CliRunner()

def test_app():
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
```
