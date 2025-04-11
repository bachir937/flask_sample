import os
import importlib

def register_middlewares(app):
    middlewares_dir = os.path.dirname(__file__)
    for filename in os.listdir(middlewares_dir):
        if filename.endswith(".py") and filename != "__init__.py":
            module_name = f"middlewares.{filename[:-3]}"
            module = importlib.import_module(module_name)
            if hasattr(module, "apply_middleware"):
                module.apply_middleware(app)
