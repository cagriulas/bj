from .builder import Builder
import stashy


class BBOps():
    def __init__(self):
        self.bb = Builder().build_bb()        

    def new_repo_request(self, project_key, project_name, repo_name):
        try:
            p = self.bb.projects[project_key].get()
        except stashy.errors.NotFoundException:
            p = self.bb.projects.create(project_key, project_name)
        try:
            r = self.bb.projects[p["key"]].repos[repo_name].get()
        except stashy.errors.NotFoundException:
            r = self.bb.projects[p["key"]].repos.create(repo_name)
        return BJRepo(r)
        

class BJRepo():
    def __init__(self, response):
        self.id = response["id"]
        self.name = response["name"]
        self.browse_link = response["links"]["self"]
        self.project = BJProject(response["project"])

    def __repr__(self):
        return f"<{self.__class__.__name__} id={self.id} name={self.name} project={self.project}>"


class BJProject():
    def __init__(self, response):
        self.id = response["id"]
        self.key = response["key"]
        self.name = response["name"]
        self.browse_link = response["links"]["self"]

    def __repr__(self):
        return f"<{self.__class__.__name__} id={self.id} key={self.key} name={self.name}>"
