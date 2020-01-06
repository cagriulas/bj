from .builder import Builder

from .bitbucket import BBOps
from .jira import JIRARepositoryRequests


def solve_all(id_s=None):
    
    jo = JIRARepositoryRequests()
   
    if id_s:
        rr = jo.get_by_ids(id_s)
    else:
        rr = jo.get_all()
    
    bb = BBOps()
    
    for r in rr:
        repository_detail = bb.new_repo_request(**r["issue_dtl"])
        jo.solve([r["issue"]])

        yield {
            "repository_detail": repository_detail,
            "issue_key": r["issue"].key
        }


def list_all():
    jo = JIRARepositoryRequests()
    rr = jo.get_all()
    return ((x["issue"].key, x["issue_dtl"]) for x in rr)
