from .builder import Builder


class JIRARepositoryRequests():
    def __init__(self):
        self._jira = Builder().build_jira()
        self.fields = {}
        for field in self._jira.fields():
            if field["custom"]:
                self.fields[field["name"]] = field["id"]

    def _parse_issue(self, issue):
        repo_name = getattr(issue.fields, self.fields["Bitbucket Repository Name"])
        project_name = getattr(issue.fields, self.fields["Bitbucket Project Name"])
        project_key = self._create_project_key_from_name(project_name)
        return project_key, project_name, repo_name

    @staticmethod
    def _create_project_key_from_name(project_name):
        return project_name.lower().replace("[^a-z0-9_-]", "-")

    def _serialize(self, issues):
        repos = []
        for issue in issues:
            project_key, project_name, repo_name = self._parse_issue(issue)
            repos.append(dict(
                issue=issue,
                issue_dtl=dict(
                    project_key=project_key,
                    project_name=project_name,
                    repo_name=repo_name 
                )
            ))
        return repos

    def get_by_ids(self, id_s):
        ids = f"({str(id_s)[1:-1]})"
        issues = self._jira.search_issues("project=BR AND status='To Do' AND issueKey IN {}".format(ids))
        return self._serialize(issues)

    def get_all(self):
        issues = self._jira.search_issues('project=BR AND status="To Do"')
        return self._serialize(issues)
        
    def solve(self, issues):
        for issue in issues:
            transition_id = None
            for tr in self._jira.transitions(issue):
                if tr["name"] == "Done":
                    transition_id = tr["id"]
            if transition_id:
                self._jira.transition_issue(issue, transition_id)
            else:
                print("Done transition not found")
