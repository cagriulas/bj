from cleo import Command
from bj.lib.scenerios import list_all, solve_all
from bj.lib.builder import save_configs
import sys


class CustomCommand(Command):
    pass


class ListRepositoryRequests(CustomCommand):
    """
    List uncreated repository request issues

    list
    """

    def handle(self):
        all_requests = list_all()
        self.line("Requested Repositories")
        self.line("-------------------------")
        for key, req in all_requests:
            self.line(f"Key: <key>{key}</key> - <Project Key: {req['project_key']}, Project Name: {req['project_name']}, Repository Name: {req['repo_name']}>")


class SolveRepositoryRequests(CustomCommand):
    """
    Solve repository request issues

    solve
        {issue-keys?* : resolve issues by id}
        {--all : resolve all request issues}
    """

    def handle(self):
        self.line("Creating Repositories")
        self.line("-------------------------")
        if self.option('all'):
            for i in solve_all():
                r_dtl = i["repository_detail"]
                self.line(f"[CREATED] - Key: {i['issue_key']} - ID: {r_dtl.id}, Name: {r_dtl.name}, Link: <{r_dtl.browse_link}>") 
        else:
            for i in solve_all(self.argument('issue-keys')):
                r_dtl = i["repository_detail"]
                self.line(f"[CREATED] - Key: {i['issue_key']} - ID: {r_dtl.id}, Name: {r_dtl.name}, Link: <{r_dtl.browse_link}>") 
        self.line("<info>DONE</info>")


class CreateConfig(CustomCommand):
    """
    Create config file

    config
        {--bb-url= : bitbucket host url}
        {--bb-username= : bitbucket username}
        {--bb-pw= : bitbucket password}
        {--jira-url= : jira host url }
        {--jira-username= : jira username}
        {--jira-pw= : jira password}
    """

    def handle(self):
        for opt in ("bb-url", "bb-username", "bb-pw", "jira-url", "jira-username", "jira-pw"):
            if opt not in list(self._args.options(include_defaults=False).keys()):
                self.line(f"<error>Missing required option `--{opt}`</error>")
                self.line(f"<info>Type `bj help config` for details.</info>")
                sys.exit(0)

        cfg_path = save_configs(**self._args.options())
        self.line(f"<info>[INFO]</info> - Configs saved '{cfg_path}'")


