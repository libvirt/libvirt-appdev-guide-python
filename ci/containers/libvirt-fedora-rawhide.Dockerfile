FROM registry.fedoraproject.org/fedora:rawhide

RUN dnf update -y --nogpgcheck fedora-gpg-keys && \
    dnf update -y && \
    dnf install -y glibc-devel

# Temp hack for https://bugzilla.redhat.com/show_bug.cgi?id=1900021
RUN curl  -O -J https://kojipkgs.fedoraproject.org/packages/glibc/2.32.9000/15.fc34/x86_64/glibc-2.32.9000-15.fc34.x86_64.rpm
RUN curl  -O -J https://kojipkgs.fedoraproject.org/packages/glibc/2.32.9000/15.fc34/x86_64/glibc-common-2.32.9000-15.fc34.x86_64.rpm
RUN curl  -O -J https://kojipkgs.fedoraproject.org/packages/glibc/2.32.9000/15.fc34/x86_64/glibc-devel-2.32.9000-15.fc34.x86_64.rpm
RUN curl  -O -J https://kojipkgs.fedoraproject.org/packages/glibc/2.32.9000/15.fc34/noarch/glibc-headers-x86-2.32.9000-15.fc34.noarch.rpm
RUN curl  -O -J https://kojipkgs.fedoraproject.org/packages/glibc/2.32.9000/15.fc34/x86_64/glibc-langpack-en-2.32.9000-15.fc34.x86_64.rpm
RUN curl  -O -J https://kojipkgs.fedoraproject.org/packages/glibc/2.32.9000/15.fc34/x86_64/glibc-minimal-langpack-2.32.9000-15.fc34.x86_64.rpm
RUN rpm -Uvh glibc* --oldpackage

RUN dnf install -y \
        bash \
        bash-completion \
        ca-certificates \
        ccache \
        gcc \
        gettext \
        git \
        make \
        patch \
        perl \
        perl-App-cpanminus \
        pkgconfig \
        publican \
        python3 \
        python3-pip \
        python3-setuptools \
        python3-wheel \
        rpm-build && \
    dnf autoremove -y && \
    dnf clean all -y && \
    mkdir -p /usr/libexec/ccache-wrappers && \
    ln -s /usr/bin/ccache /usr/libexec/ccache-wrappers/cc && \
    ln -s /usr/bin/ccache /usr/libexec/ccache-wrappers/$(basename /usr/bin/gcc)

ENV LANG "en_US.UTF-8"

ENV MAKE "/usr/bin/make"
ENV NINJA "/usr/bin/ninja"
ENV PYTHON "/usr/bin/python3"

ENV CCACHE_WRAPPERSDIR "/usr/libexec/ccache-wrappers"
