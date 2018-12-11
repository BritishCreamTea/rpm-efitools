#!/bin/bash -e

VERSION=1.8.1

# Removes all build directories
rm -rf BUILD BUILDROOT RPMS SRPMS
rm SOURCES/efitools-$VERSION.tar.gz
