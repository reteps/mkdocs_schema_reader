from setuptools import setup, find_packages


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="mkdocs_schema_reader_2",
    version="0.12.1",
    description="A MkDocs plugin to embed json schema files as markdown within your documentation.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords="mkdocs, schema, json, plugin",
    url="https://github.com/mysiki/mkdocs_schema_reader",
    author="",
    author_email="",
    license="MIT",
    python_requires=">=3.6",
    install_requires=["mkdocs>=1.0.4", "jsonschema2md>=0.3.0"],
    packages=find_packages(),
    entry_points={
        "mkdocs.plugins": [
            "schema_reader = mkdocs_schema_reader.schema_reader:SchemaReader"
        ]
    },
)
