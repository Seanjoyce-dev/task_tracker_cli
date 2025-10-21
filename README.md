# task-tracker-cli

A tiny command-line task tracker built with Typer and Pydantic. Store tasks in `tasks.json` and manage them with simple commands.

## Requirements

- Python 3.14+
- The project declares dependencies in `pyproject.toml`:
  - pydantic >= 2.12.3
  - rich >= 14.2.0
  - typer >= 0.20.0

If you use `uv` to manage your environment and dependencies, install and activate the environment using your usual `uv` workflow. For example (depending on your `uv` setup):

```bash
# install dependencies with uv (example - adjust to your uv workflow)
uv install
# then activate the environment created by uv
uv activate
```

After activating the environment, run the CLI from the project root.

If you don't use `uv`, you can install the required packages directly into your active Python environment:

```bash
python -m pip install pydantic rich typer
```

## Usage

Run the CLI from the project root:

```bash
python main.py COMMAND [ARGS...]
```

Available commands (from `main.py`):

- add DESCRIPTION
- update TASK_ID DESCRIPTION
- delete TASK_ID
- mark-in-progress TASK_ID
- mark-done TASK_ID
- list-tasks [STATUS]

Examples:

```bash
python main.py add "Write README"
python main.py list-tasks
python main.py mark-done 1
```

Statuses:

- todo
- in_progress
- done

## Data file

Tasks are stored in `tasks.json` with the shape:

```json
{
  "items": [
    {
      "id": 1,
      "description": "Buy groceries",
      "status": "todo",
      "created_at": "2025-10-21T20:17:40.730396",
      "updated_at": "2025-10-21T20:17:40.730396"
    }
  ]
}
```

## Development

- The CLI is implemented in `main.py` and uses models in the `models/` package.
- Ensure the environment that contains the installed dependencies is active before running the CLI.

## Notes

- `pyproject.toml` lists the project metadata and dependencies.
- `tasks.json` is created/updated by the CLI. Keep a backup if you need to reset.

Contributions welcome.
