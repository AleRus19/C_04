from pathlib import Path

from flakon import create_app

from calc.views import blueprints

# Get the name of this directory, i.e. application name
_APP_NAME = Path(__file__).parent.name

# Let's create the Flask App using Flakon
_app = create_app(
    name=_APP_NAME,
    blueprints=blueprints,
)
