import pkgutil
import importlib


def load_skills():

    tools = []

    for _, module_name, _ in pkgutil.iter_modules(["app/skills"]):

        module = importlib.import_module(f"app.skills.{module_name}")

        for attr in dir(module):

            obj = getattr(module, attr)

            if hasattr(obj, "name") and hasattr(obj, "description"):

                tools.append(obj)

    return tools