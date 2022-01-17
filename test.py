from src.pysugg.exception_catcher import ExceptionCatcher
from src.pysugg.exception_executors.module_suggest_executor import ModuleSuggestExecutor

ExceptionCatcher().add_executor(ModuleSuggestExecutor("test", print_trace=True)).start()

# For test, you can see we have not imported the 'os' module, but no error raise as usual here.
# And, you will find suggested import statements.
flask
