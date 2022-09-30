# THIS FILE WAS AUTO-GENERATED
#
#  $ lcitool manifest ci/manifest.yml
#
# https://gitlab.com/libvirt/libvirt-ci

function install_buildenv() {
    dnf update -y
    dnf install -y \
        ca-certificates \
        git \
        glibc-langpack-en \
        make \
        publican
    rpm -qa | sort > /packages.txt
}

export LANG="en_US.UTF-8"
export MAKE="/usr/bin/make"
