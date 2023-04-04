import logging


def pytest_configure(config):
    logging.basicConfig(level=logging.INFO)
    logging.getLogger().setLevel(logging.INFO)
    config.addinivalue_line("markers", "log: mark the test function to show log in the report")


def pytest_collection_modifyitems(items, config):
    for item in items:
        if "log" in item.keywords:
            item.parent.session._fixturemanager.parsefactories(item)
