from setuptools import setup, find_packages

setup(
    name="mkdocs-post-count-plugin",
    version="0.1.0",
    packages=find_packages(),
    entry_points={
        "mkdocs.plugins": [
            "post_count = post_count.plugin:PostCountPlugin",
        ]
    },
)
