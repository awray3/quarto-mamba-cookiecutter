from box import Box
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent.parent

params = Box.from_yaml(filename=PROJECT_ROOT / 'params.yml')

__all__ = [PROJECT_ROOT, params]