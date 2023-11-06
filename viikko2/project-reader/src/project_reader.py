from urllib import request
from project import Project
from toml import loads


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        toml_data = loads(content)
        project = Project(name=toml_data['tool']['poetry']['name'],
                          description=toml_data['tool']['poetry']['description'],
                          toml_license=toml_data['tool']['poetry']['license'],
                          authors=[], dependencies=[], dev_dependencies=[])
        for author in toml_data['tool']['poetry']['authors']:
            project.authors.append(author)
        for dep in toml_data['tool']['poetry']['dependencies']:
            project.dependencies.append(dep)
        for dep in toml_data['tool']['poetry']['group']['dev']['dependencies']:
            project.dev_dependencies.append(dep)
        return  project
