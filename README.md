# BJ
Create repositories according to jira issue on bitbucket

## Requirements
poetry (python)

## Build
```bash
$ cd bj
$ poetry build
$ pip install dist/*.whl
```

## Usage

Set configs
```bash
$ bj config --bb-url=http://192.168.56.2/bitbucket --bb-pw=1234 --bb-username=admin --jira-url=http://192.168.56.2/JIRA --jira-pw=1234 --jira-username=admin
```

List open issues
```bash
$ bj list
Requested Repositories
-------------------------
Key: BR-9 - <Project Key: project17, Project Name: project17, Repository Name: repo1>
Key: BR-8 - <Project Key: project4, Project Name: project4, Repository Name: repo7>
Key: BR-5 - <Project Key: testproject, Project Name: testproject, Repository Name: test repo>
```

to solve selected issues
```bash
$ bj solve BR-9 BR-8
Creating Repositories
-------------------------
[CREATED] - Key: BR-9 - ID: 13, Name: repo1, Link: <[{'href': 'http://192.168.56.2/bitbucket/projects/PROJECT17/repos/repo1/browse'}]>
[CREATED] - Key: BR-8 - ID: 14, Name: repo7, Link: <[{'href': 'http://192.168.56.2/bitbucket/projects/PROJECT4/repos/repo7/browse'}]>
DONE
```

to solve all issues
```bash
$ bj solve --all
[CREATED] - Key: BR-5 - ID: 12, Name: test repo, Link: <[{'href': 'http://192.168.56.2/bitbucket/projects/TESTPROJECT/repos/test-repo/browse'}]>
DONE
```

for help
```bash
$ bj help
```

for advanced help about any command use
```bash
$ bj help solve
```