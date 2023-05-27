from .base import WebDriverBrowser, require_arg
from .base import get_timeout_multiplier
from ..executors import executor_kwargs as base_executor_kwargs
from ..executors.executorwebdriver import (WebDriverTestharnessExecutor,  # noqa: F401
                                           WebDriverRefTestExecutor,  # noqa: F401
                                           WebDriverCrashtestExecutor)  # noqa: F401
from ..executors.base import WdspecExecutor

__wptrunner__ = {
    "product": "ladybird",
    "check_args": "check_args",
    "browser": "LadybirdBrowser",
    "browser_kwargs": "browser_kwargs",
    "executor_kwargs": "executor_kwargs",
    "env_options": "env_options",
    "env_extras": "env_extras",
    "timeout_multiplier": "get_timeout_multiplier",
    "executor": {
        "testharness": "WebDriverTestharnessExecutor",
        "reftest": "WebDriverRefTestExecutor",
        "wdspec": "WdspecExecutor",
        "crashtest": "WebDriverCrashtestExecutor"
    }
}

def check_args(**kwargs):
    pass

def browser_kwargs(logger, test_type, run_info_data, config, **kwargs):
    return {}

def executor_kwargs(logger, test_type, test_environment, run_info_data,
                    **kwargs):
    executor_kwargs = base_executor_kwargs(test_type, test_environment, run_info_data, **kwargs)
    executor_kwargs["capabilities"] = {}
    return executor_kwargs

def env_options():
    return {}

def env_extras(**kwargs):
    return []

class LadybirdBrowser(WebDriverBrowser):
    def __init__(self, logger, webdriver_args=None,
                 host="localhost", port=None, base_path="/", env=None, **kwargs):
        webdriver_bin = "/Users/kalenik/projects/serenity/Build/lagom/Ladybird/WebDriver/WebDriver"

        super().__init__(logger, "binary???", webdriver_bin, webdriver_args=webdriver_args,
                         host=host, port=port, base_path=base_path, env=env, **kwargs)
        self.host = "localhost"
    
    def make_command(self):
        return [self.webdriver_binary, "--port", str(self.port)] + self.webdriver_args
