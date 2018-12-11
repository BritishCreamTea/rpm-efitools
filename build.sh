#!/bin/bash -e

VERSION=1.8.1

cd SOURCES
if [ -f SOURCES/efitools-$VERSION.tar.gz ]; then
  rm efitools-$VERSION.tar.gz
fi
./get-tarball.sh
cd ..
rpmbuild --define "_topdir `pwd`" -ba SPECS/efitools.spec
echo "Output RPMS are located in ./RPMS/$(uname -p)/"
