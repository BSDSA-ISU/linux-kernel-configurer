#!/usr/bin/bash


linux_version="6.12.10"


starting() {
    cd "linux-$linux_version" || exit
    rm -rvf linux-upstream-6* *headers*
    #cp ../PKGBUILD ./PKGBUILD
}
downloadkernel() {
    if [[ -f "linux-6.12.10/*" ]]; then 
        rsync rsync://rsync.kernel.org/pub/linux/kernel/v6.x/linux-6.12.10.tar.xz . -rvz
    else
        echo "nothing"
    fi
}

makeconfig() {
    make menuconfig -j$(nproc)
}

installkernel() {
    sudo pacman -U linux-upstream-6* *headers*
}

build() {
    if [[ ! -f ".config" ]]; then
        echo "no config detected. Possible that the user didn't save his .config file"
    fi

    make -j$(nproc) pacman-pkg
}




downloadkernel
starting
makeconfig
build
installkernel