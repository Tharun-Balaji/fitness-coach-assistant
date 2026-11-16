from pathlib import Path


def load_system_prompt():
    """Load the system prompt from prompt.txt file."""
    prompt_path = Path(__file__).resolve().parent.parent / "prompt.txt"
    try:
        return prompt_path.read_text(encoding="utf-8").strip()
    except FileNotFoundError as exc:
        raise FileNotFoundError(
            f"Coach Alex system prompt was not found at {prompt_path}"
        ) from exc
    except (OSError, UnicodeError) as exc:
        raise OSError(f"Could not read Coach Alex system prompt at {prompt_path}") from exc


def get_system_prompt():
    """Get the system prompt for the fitness coach."""
    return load_system_prompt()

SYSTEM_PROMPT = get_system_prompt()
