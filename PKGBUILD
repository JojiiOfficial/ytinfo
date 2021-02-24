# Maintainer: Jojii <Jojii ad gmx.net>
pkgname=ytinfo
pkgver=0.0.1
pkgrel=1
pkgdesc="simple script to retrieve youtube metadata from a youtube url"
url="https://github.com/JojiiOfficial/ytinfo"
license=('GPL')
depends=("youtube-dl")
makedepends=()
source=("git+$url")
arch=("any")
md5sums=("SKIP")

package() {
    cd $pkgname
    install -Dm 755 "main.py" "${pkgdir}/usr/bin/${pkgname}"
    install -Dm 755 "LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
