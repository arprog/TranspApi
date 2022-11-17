from subprocess import run
import pathlib
import os


def run_scrapy_shell_script(name_spider):
    path_ = str(pathlib.Path().resolve())
    path_ = path_[:-16]

    command_ = ["scrapy", "crawl", name_spider]

    execution = run(command_, env=dict(os.environ, PATH=path_))
