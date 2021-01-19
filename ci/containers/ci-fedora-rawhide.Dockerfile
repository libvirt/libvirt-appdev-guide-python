FROM registry.fedoraproject.org/fedora:rawhide

RUN dnf install -y nosync && \
    echo -e '#!/bin/sh\n\
if test -d /usr/lib64\n\
then\n\
    export LD_PRELOAD=/usr/lib64/nosync/nosync.so\n\
else\n\
    export LD_PRELOAD=/usr/lib/nosync/nosync.so\n\
fi\n\
exec "$@"' > /usr/bin/nosync && \
    chmod +x /usr/bin/nosync && \
    nosync dnf update -y --nogpgcheck fedora-gpg-keys && \
    nosync dnf update -y && \
    nosync dnf install -y \
        glibc-devel

# Temp hack for https://bugzilla.redhat.com/show_bug.cgi?id=1900021
RUN curl  -O -J https://kojipkgs.fedoraproject.org/packages/glibc/2.32.9000/15.fc34/x86_64/glibc-2.32.9000-15.fc34.x86_64.rpm
RUN curl  -O -J https://kojipkgs.fedoraproject.org/packages/glibc/2.32.9000/15.fc34/x86_64/glibc-common-2.32.9000-15.fc34.x86_64.rpm
RUN curl  -O -J https://kojipkgs.fedoraproject.org/packages/glibc/2.32.9000/15.fc34/x86_64/glibc-devel-2.32.9000-15.fc34.x86_64.rpm
RUN curl  -O -J https://kojipkgs.fedoraproject.org/packages/glibc/2.32.9000/15.fc34/noarch/glibc-headers-x86-2.32.9000-15.fc34.noarch.rpm
RUN curl  -O -J https://kojipkgs.fedoraproject.org/packages/glibc/2.32.9000/15.fc34/x86_64/glibc-langpack-en-2.32.9000-15.fc34.x86_64.rpm
RUN curl  -O -J https://kojipkgs.fedoraproject.org/packages/glibc/2.32.9000/15.fc34/x86_64/glibc-minimal-langpack-2.32.9000-15.fc34.x86_64.rpm
RUN rpm -Uvh glibc* --oldpackage

RUN nosync dnf install -y \
        ca-certificates \
        git \
        glibc-langpack-en \
        make \
        publican && \
    nosync dnf autoremove -y && \
    nosync dnf clean all -y && \
    rpm -qa | sort > /packages.txt

ENV LANG "en_US.UTF-8"
ENV MAKE "/usr/bin/make"
