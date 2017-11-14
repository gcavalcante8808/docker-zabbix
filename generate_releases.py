#!/usr/bin/env python


import sys
import os
import pystache

from git import Repo

# Get the Git Tree
repo = Repo()

# Get current tags
tags = repo.tags

# Gather the Supported Versions and Daemons.
with open('supported_versions', 'r') as openfile:
    supported_versions = [line.rstrip('\n') for line in openfile]
    
with open('supported_daemons', 'r') as openfile:
    supported_daemons = [line.rstrip('\n') for line in openfile]
    
    
def create_version_dirs(dirname):
    """ Create directories named by the versions, creating needed dirs recursively"""
    if sys.version_info < (3,2):
        if not os.path.exists(os.path.dirname(filename)):
            try:
                os.makedirs(os.path.dirname(filename))
            except OSError as exc:
                if exc.errno != errno.EEXIST:
                    raise
    else:
        os.makedirs(os.path.dirname(filename), exist_ok=True)

def add_to_git(version):
    """ Add newly created files to git """
    repo.git.add(A=True)
    commit = repo.index.commit('Automatic generation of %s commit' % version)
    tag = [ tag for tag in tags if tag.name == version ]
    if tag:
        print('Tag %s will be removed from local repo' %version)
        repo.delete_tag(version)

    repo.create_tag(version, ref=commit,
                    message="Automatic generation of %s tag" % version)

# Iter over supported daemons and versions, creating the needed directories and using
# mustache to write the new Dockerfile Version.
for version in supported_versions:
    context = {"version": version}

    for daemon in supported_daemons:
        filename = '{}/Dockerfile'.format(daemon)
        # Create Version Dir.
        create_version_dirs(filename)
        
        # Write the New Dockerfile for specific version.
        template_file = '{}/Dockerfile.mustache'.format(daemon)
        
        template = open(template_file, 'r').read()

        with open(filename, 'w') as tempfile:
            tempfile.write(pystache.render(template, context))

    add_to_git(version)

print("All files for supported versions were generated")
