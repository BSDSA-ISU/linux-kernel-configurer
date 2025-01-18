#!/usr/bin/bash


linux_version="6.12.10"

cd "linux-$linux_version" || exit
cp ../PKGBUILD ./PKGBUILD

makeconfig() {
    make menuconfig -j$(nproc)
}

makeconfig
if [[ ! -f ".config" ]]; then
    echo "no config detected. Possible that the user didn't save his .config file"
    return 1
fi

installkernel() {
    sudo pacman -U linux-upstream-6* linux-upstream-api-headers-6*
}

build() {
    make -j$(nproc)
}

