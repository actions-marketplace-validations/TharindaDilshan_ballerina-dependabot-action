#!/usr/bin/env python3
import os
import helpers
import file_fetcher
import file_parser
import file_updater

repo = helpers.configureGithubRepository()
tomlFile = file_fetcher.fetchTomlFileFromMainBranch(repo)
modulesToBeUpdated = file_parser.getModulesToBeUpdated(tomlFile)

if len(modulesToBeUpdated) > 0:
    file_updater.updateFileAndRaisePR(repo, modulesToBeUpdated)

exit(0)