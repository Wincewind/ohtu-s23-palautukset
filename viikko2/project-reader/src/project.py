class Project:
    def __init__(self, name, description, toml_license, authors, dependencies, dev_dependencies):
        self.name = name
        self.description = description
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies
        self.toml_license = toml_license
        self.authors = authors

    def _stringify_details(self, details):
        return "- "+"\n- ".join(details) if len(details) > 0 else "-"

    def __str__(self):
        return (
f"""
Name: {self.name}
Description: {self.description or '-'}
License: {self.toml_license or '-'}

Authors:
{self._stringify_details(self.authors)}

Dependencies:
{self._stringify_details(self.dependencies)}

Development dependencies:
{self._stringify_details(self.dev_dependencies)}
""")
