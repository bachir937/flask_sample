import os
import importlib

def register_routes(app):
    route_dir = os.path.dirname(__file__)
    for filename in os.listdir(route_dir):
        if filename.endswith(".py") and filename != "__init__.py":
            module_name = f"routes.{filename[:-3]}"
            module = importlib.import_module(module_name)
            if hasattr(module, "bp"):
                app.register_blueprint(module.bp)
