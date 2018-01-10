#!/usr/bin/env python


import sys
import os
import pystache
import argparse

from git import Repo


class Version2TagManager:
    """
    Receive a list of supported versions, create appropriate Dockerfiles to 
    versions and create git local tags for 'em.
    """
    def __init__(self, version=False):
        """
        Version should be a list with the following format:
        ['X.X.X']
        
        #TODO: Force type using mytype.
        """
        # Get the Git Tree
        self.repo = Repo()

        # Get current tags
        self.tags = self.repo.tags

        # Gather the Supported Versions and Daemons.
        self.supported_versions = version
        if not self.supported_versions:
            with open('supported_versions', 'r') as openfile:
                self.supported_versions = [line.rstrip('\n') for line in openfile]
    
        with open('supported_daemons', 'r') as openfile:
            self.supported_daemons = [line.rstrip('\n') for line in openfile]
    
    def create_version_dirs(self, filename):
        """ Create directories named by the versions, creating needed dirs recursively"""
        #TODO: This should be a static method probably.
        if sys.version_info < (3,2):
            if not os.path.exists(os.path.dirname(filename)):
                try:
                    os.makedirs(os.path.dirname(filename))
                except OSError as exc:
                    if exc.errno != errno.EEXIST:
                        raise
        else:
            os.makedirs(os.path.dirname(filename), exist_ok=True)

    def add_to_git(self, version):
        """ Add newly created files to git """
        self.repo.git.add(A=True)
        commit = self.repo.index.commit('Automatic generation of %s commit' % version)
        tag = [ tag for tag in self.tags if tag.name == version ]
        if tag:
            print('Tag %s will be removed from local repo' %version)
            repo.delete_tag(version)

        self.repo.create_tag(version, ref=commit,
                        message="Automatic generation of %s tag" % version)

    def create_tag_version(self):
        """ 
        Iter over supported daemons and versions, creating the needed 
        directories and using mustache to write the new Dockerfile 
        Version.

        This method calls the create_version_dirs and add_to_git to 
        create a new directory with the files and to add them to 
        a git local tag/version.
        """
        for version in self.supported_versions:
            context = {"version": version}

            for daemon in self.supported_daemons:
                filename = '{}/Dockerfile'.format(daemon)
                # Create Version Dir.
                self.create_version_dirs(filename)
                    
                # Write the New Dockerfile for specific version.
                template_file = '{}/Dockerfile.mustache'.format(daemon)
                    
                template = open(template_file, 'r').read()

                with open(filename, 'w') as tempfile:
                    tempfile.write(pystache.render(template, context))

            self.add_to_git(version)

        print("All files for supported versions were generated")

if __name__ == '__main__':
    PARSER = argparse.ArgumentParser()
    PARSER.add_argument('--version', type=str, required=True)
    
    args = PARSER.parse_args()
    
    manager = Version2TagManager(version=[args.version])
    manager.create_tag_version()

