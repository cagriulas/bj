from .commands import ListRepositoryRequests, SolveRepositoryRequests, CreateConfig
from cleo import Application
from cleo.config import ApplicationConfig
from clikit.api.formatter import Style

ac = ApplicationConfig()
ac.add_style(Style('key').fg("white").bold())

application = Application('BJ', '0.1', complete=True, config=ac)
application.add(ListRepositoryRequests())
application.add(SolveRepositoryRequests())
application.add(CreateConfig())


def run():
    return application.run()
