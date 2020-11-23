FROM registry.fedoraproject.org/fedora:33

RUN dnf update -y && \
    dnf install -y \
        ca-certificates \
        git \
        glibc-langpack-en \
        make \
        publican && \
    dnf autoremove -y && \
    dnf clean all -y

ENV LANG "en_US.UTF-8"
ENV MAKE "/usr/bin/make"
