from setuptools import setup, find_packages

setup(
    name = "score",
    version = 1.0,
    author = "Venketaram Ramachandran",
    author_email = "v.ram28@gmail.com",
    url = "https://v-ramachandran.github.io/score",
    install_requires = ["requests","jsoncompare","PyYAML"],
    packages = find_packages()
)
