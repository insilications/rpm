#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : rpm
Version  : 4.14.2.1
Release  : 203
URL      : http://ftp.rpm.org/releases/rpm-4.14.x/rpm-4.14.2.1.tar.bz2
Source0  : http://ftp.rpm.org/releases/rpm-4.14.x/rpm-4.14.2.1.tar.bz2
Summary  : RPM Package Manager
Group    : Development/Tools
License  : GPL-2.0+
Requires: rpm-bin = %{version}-%{release}
Requires: rpm-lib = %{version}-%{release}
Requires: rpm-locales = %{version}-%{release}
Requires: rpm-man = %{version}-%{release}
Requires: rpm-python = %{version}-%{release}
Requires: rpm-python3 = %{version}-%{release}
Requires: unzip
Requires: zip
BuildRequires : acl-dev
BuildRequires : acl-staticdev
BuildRequires : automake
BuildRequires : automake-dev
BuildRequires : binutils-dev
BuildRequires : binutils-extras
BuildRequires : bison
BuildRequires : bzip2-dev
BuildRequires : bzip2-staticdev
BuildRequires : compat-lua-53
BuildRequires : compat-lua-53-abi
BuildRequires : compat-lua-53-bin
BuildRequires : compat-lua-53-dev
BuildRequires : compat-lua-53-lib
BuildRequires : compat-lua-53-man
BuildRequires : compat-lua-53-staticdev
BuildRequires : db-dev
BuildRequires : dbus-dev
BuildRequires : dejagnu
BuildRequires : docbook-utils
BuildRequires : docbook-xml
BuildRequires : doxygen
BuildRequires : elfutils-dev
BuildRequires : expect
BuildRequires : fakechroot
BuildRequires : fakechroot-dev
BuildRequires : fakechroot-staticdev
BuildRequires : file
BuildRequires : file-abi
BuildRequires : file-bin
BuildRequires : file-data
BuildRequires : file-dev
BuildRequires : file-lib
BuildRequires : file-license
BuildRequires : file-man
BuildRequires : flex
BuildRequires : gcc
BuildRequires : gcc-dev
BuildRequires : gcc-dev32
BuildRequires : gcc-doc
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libs-math
BuildRequires : gcc-libstdc++32
BuildRequires : gcc-libubsan
BuildRequires : gcc-locale
BuildRequires : gdb
BuildRequires : gdb-dev
BuildRequires : gettext-bin
BuildRequires : git
BuildRequires : glibc-bench
BuildRequires : glibc-bin
BuildRequires : glibc-dev
BuildRequires : glibc-dev32
BuildRequires : glibc-doc
BuildRequires : glibc-extras
BuildRequires : glibc-lib-avx2
BuildRequires : glibc-libc32
BuildRequires : glibc-locale
BuildRequires : glibc-nscd
BuildRequires : glibc-staticdev
BuildRequires : glibc-utils
BuildRequires : gmp-dev
BuildRequires : gmp-staticdev
BuildRequires : gnupg
BuildRequires : graphviz
BuildRequires : guile
BuildRequires : libarchive
BuildRequires : libarchive-dev
BuildRequires : libarchive-staticdev
BuildRequires : libcap
BuildRequires : libcap-dev
BuildRequires : libedit
BuildRequires : libedit-dev
BuildRequires : libffi-dev
BuildRequires : libffi-staticdev
BuildRequires : libgcc1
BuildRequires : libgcrypt
BuildRequires : libgcrypt-dev
BuildRequires : libstdc++
BuildRequires : libtool
BuildRequires : libtool-dev
BuildRequires : libunwind
BuildRequires : libunwind-dev
BuildRequires : m4
BuildRequires : nspr-dev
BuildRequires : openssl-dev
BuildRequires : openssl-staticdev
BuildRequires : pkg-config-dev
BuildRequires : pkgconfig(dbus-1)
BuildRequires : pkgconfig(libarchive)
BuildRequires : pkgconfig(libzstd)
BuildRequires : pkgconfig(lmdb)
BuildRequires : pkgconfig(nss)
BuildRequires : pkgconfig(python-3.9)
BuildRequires : pkgconfig(zlib)
BuildRequires : popt
BuildRequires : popt-dev
BuildRequires : python3-dev
BuildRequires : python3-staticdev
BuildRequires : sqlite-autoconf
BuildRequires : sqlite-autoconf-dev
BuildRequires : unzip
BuildRequires : xz-dev
BuildRequires : xz-staticdev
BuildRequires : zip
BuildRequires : zlib
BuildRequires : zlib-dev
BuildRequires : zlib-staticdev
BuildRequires : zstd-dev
BuildRequires : zstd-staticdev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: 0001-Ensure-lib-is-used-and-not-lib64.patch
Patch2: 0002-Fix-32bit-kernel-builds-by-not-using-eu-strip.patch
Patch3: 0003-add-an-fflush.patch
Patch4: 0004-skip-pkgconfig-dep.patch
Patch5: 0005-Relocate-debuginfo-to-usr-share-debug.patch
Patch6: 0006-Don-t-emit-compiler-version-requirement.patch
Patch7: 0007-debuginfo-do-not-strip-static-libraries.patch
Patch8: 0008-scripts-Don-t-bail-out-when-debugedit-fails.patch
Patch9: 0009-fileattrs-Ensure-we-match-all-binaries-for-elf-depen.patch
Patch10: 0010-Don-t-fail-a-build-if-build-id-is-a-duplicate.patch
Patch11: 0011-Add-ldconfig-post-transaction-hook.patch
Patch12: 0012-support-lib32-pkgconfig-files.patch
Patch13: 0013-preserve-timestamps.patch
Patch14: 0014-skip-datasync.patch
Patch15: 0015-rpm-use-localhost-as-hostname-for-building-all-packa.patch
Patch16: 0016-fileattrs-Don-t-scan-libraries-in-glibc-auto-search-.patch
Patch17: 0017-Force-locale-files-not-to-be-executable.patch
Patch18: 0018-discover-uid0-based-on-usr-share-defaults.patch
Patch19: 0019-fix-debuginfo-build-id-matching-code.patch
Patch20: 0020-Skip-HEREDOCs-when-parsing-perl-virtual-Provides.patch
Patch21: 0021-Disable-mono-fileattrs.patch
Patch22: 0022-rpm2cpio-cannot-handle-files-over-4GB-error-out-clea.patch
Patch23: 0023-Build-with-Lua-5.3-for-now.patch
Patch24: 0024-elf.attr-exclude-openmpi-directories.patch
Patch25: 0025-elf.attr-exclude-mingw-library-tree.patch
Patch26: 0001-rpmbuild-bb-shortcircuit.patch

%description
This is RPM, the RPM Package Manager.
The latest releases are always available at:

%package bin
Summary: bin components for the rpm package.
Group: Binaries

%description bin
bin components for the rpm package.


%package dev
Summary: dev components for the rpm package.
Group: Development
Requires: rpm-lib = %{version}-%{release}
Requires: rpm-bin = %{version}-%{release}
Provides: rpm-devel = %{version}-%{release}
Requires: rpm = %{version}-%{release}

%description dev
dev components for the rpm package.


%package extras
Summary: extras components for the rpm package.
Group: Default

%description extras
extras components for the rpm package.


%package lib
Summary: lib components for the rpm package.
Group: Libraries

%description lib
lib components for the rpm package.


%package locales
Summary: locales components for the rpm package.
Group: Default

%description locales
locales components for the rpm package.


%package man
Summary: man components for the rpm package.
Group: Default

%description man
man components for the rpm package.


%package python
Summary: python components for the rpm package.
Group: Default
Requires: rpm-python3 = %{version}-%{release}

%description python
python components for the rpm package.


%package python3
Summary: python3 components for the rpm package.
Group: Default
Requires: python3-core

%description python3
python3 components for the rpm package.


%prep
%setup -q -n rpm-4.14.2.1
cd %{_builddir}/rpm-4.14.2.1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1
%patch25 -p1
%patch26 -p1

%build
unset http_proxy
unset https_proxy
unset no_proxy
export SSL_CERT_FILE=/var/cache/ca-certs/anchors/ca-certificates.crt
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1620614703
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
## altflags1 content
export CFLAGS="-g -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc -Wl,--build-id=sha1"
# -ffat-lto-objects -fno-PIE -fno-PIE -m64 -no-pie -fPIC -Wl,-z,max-page-size=0x1000 -fvisibility=hidden -flto-partition=none
# gcc: -feliminate-unused-debug-types -fipa-pta -flto=16 -Wno-error -Wp,-D_REENTRANT -fno-common
export CXXFLAGS="-g -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -fvisibility-inlines-hidden -pipe -ffat-lto-objects -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc -Wl,--build-id=sha1"
#
export FCFLAGS="-g -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc -Wl,--build-id=sha1"
export FFLAGS="-g -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -Wl,--build-id=sha1"
export CFFLAGS="-g -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc -Wl,--build-id=sha1"
#
export LDFLAGS="-g -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc -lpthread -Wl,--build-id=sha1"
#
export AR=/usr/bin/gcc-ar
export RANLIB=/usr/bin/gcc-ranlib
export NM=/usr/bin/gcc-nm
#
export MAKEFLAGS=%{?_smp_mflags}
#
%global _lto_cflags 1
#global _lto_cflags %{nil}
%global _disable_maintainer_mode 1
#%global _disable_maintainer_mode %{nil}
#
export CCACHE_DISABLE=true
export PATH="/usr/lib64/ccache/bin:$PATH"
export CCACHE_NOHASHDIR=true
export CCACHE_CPP2=true
export CCACHE_SLOPPINESS=pch_defines,time_macros,locale,file_stat_matches,file_stat_matches_ctime,include_file_ctime,include_file_mtime,modules,system_headers,clang_index_store,file_macro
#export CCACHE_SLOPPINESS=modules,include_file_mtime,include_file_ctime,time_macros,pch_defines,file_stat_matches,clang_index_store,system_headers,locale
#export CCACHE_SLOPPINESS=pch_defines,time_macros,locale,clang_index_store,file_macro
export CCACHE_DIR=/var/tmp/ccache
export CCACHE_BASEDIR=/builddir/build/BUILD
#export CCACHE_LOGFILE=/var/tmp/ccache/cache.debug
#export CCACHE_DEBUG=true
#export CCACHE_NODIRECT=true
## altflags1 end
%reconfigure --enable-python \
--with-lua \
--with-cap \
--with-acl \
--enable-nls \
--without-internal-beecrypt \
--without-selinux \
--disable-inhibit-plugin
make  %{?_smp_mflags}


%install
export SOURCE_DATE_EPOCH=1620614703
rm -rf %{buildroot}
%make_install
%find_lang rpm
## Remove excluded files
rm -f %{buildroot}/usr/lib/rpm/fileattrs/perl.attr
rm -f %{buildroot}/usr/lib/rpm/fileattrs/perllib.attr

%files
%defattr(-,root,root,-)
/usr/lib/rpm/brp-compress
/usr/lib/rpm/brp-java-gcjcompile
/usr/lib/rpm/brp-python-bytecompile
/usr/lib/rpm/brp-python-hardlink
/usr/lib/rpm/brp-strip
/usr/lib/rpm/brp-strip-comment-note
/usr/lib/rpm/brp-strip-shared
/usr/lib/rpm/brp-strip-static-archive
/usr/lib/rpm/check-buildroot
/usr/lib/rpm/check-files
/usr/lib/rpm/check-prereqs
/usr/lib/rpm/check-rpaths
/usr/lib/rpm/check-rpaths-worker
/usr/lib/rpm/config.guess
/usr/lib/rpm/config.sub
/usr/lib/rpm/debugedit
/usr/lib/rpm/debuginfo.prov
/usr/lib/rpm/desktop-file.prov
/usr/lib/rpm/elfdeps
/usr/lib/rpm/fileattrs/debuginfo.attr
/usr/lib/rpm/fileattrs/desktop.attr
/usr/lib/rpm/fileattrs/elf.attr
/usr/lib/rpm/fileattrs/font.attr
/usr/lib/rpm/fileattrs/libtool.attr
/usr/lib/rpm/fileattrs/metainfo.attr
/usr/lib/rpm/fileattrs/ocaml.attr
/usr/lib/rpm/fileattrs/pkgconfig.attr
/usr/lib/rpm/fileattrs/python.attr
/usr/lib/rpm/fileattrs/script.attr
/usr/lib/rpm/find-debuginfo.sh
/usr/lib/rpm/find-lang.sh
/usr/lib/rpm/find-provides
/usr/lib/rpm/find-requires
/usr/lib/rpm/fontconfig.prov
/usr/lib/rpm/libtooldeps.sh
/usr/lib/rpm/macros
/usr/lib/rpm/macros.perl
/usr/lib/rpm/macros.php
/usr/lib/rpm/macros.python
/usr/lib/rpm/metainfo.prov
/usr/lib/rpm/mkinstalldirs
/usr/lib/rpm/ocaml-find-provides.sh
/usr/lib/rpm/ocaml-find-requires.sh
/usr/lib/rpm/perl.prov
/usr/lib/rpm/perl.req
/usr/lib/rpm/pkgconfigdeps.sh
/usr/lib/rpm/platform/aarch64-linux/macros
/usr/lib/rpm/platform/alpha-linux/macros
/usr/lib/rpm/platform/alphaev5-linux/macros
/usr/lib/rpm/platform/alphaev56-linux/macros
/usr/lib/rpm/platform/alphaev6-linux/macros
/usr/lib/rpm/platform/alphaev67-linux/macros
/usr/lib/rpm/platform/alphapca56-linux/macros
/usr/lib/rpm/platform/amd64-linux/macros
/usr/lib/rpm/platform/armv3l-linux/macros
/usr/lib/rpm/platform/armv4b-linux/macros
/usr/lib/rpm/platform/armv4l-linux/macros
/usr/lib/rpm/platform/armv5tejl-linux/macros
/usr/lib/rpm/platform/armv5tel-linux/macros
/usr/lib/rpm/platform/armv5tl-linux/macros
/usr/lib/rpm/platform/armv6hl-linux/macros
/usr/lib/rpm/platform/armv6l-linux/macros
/usr/lib/rpm/platform/armv7hl-linux/macros
/usr/lib/rpm/platform/armv7hnl-linux/macros
/usr/lib/rpm/platform/armv7l-linux/macros
/usr/lib/rpm/platform/athlon-linux/macros
/usr/lib/rpm/platform/geode-linux/macros
/usr/lib/rpm/platform/i386-linux/macros
/usr/lib/rpm/platform/i486-linux/macros
/usr/lib/rpm/platform/i586-linux/macros
/usr/lib/rpm/platform/i686-linux/macros
/usr/lib/rpm/platform/ia32e-linux/macros
/usr/lib/rpm/platform/ia64-linux/macros
/usr/lib/rpm/platform/m68k-linux/macros
/usr/lib/rpm/platform/mips-linux/macros
/usr/lib/rpm/platform/mips64-linux/macros
/usr/lib/rpm/platform/mips64el-linux/macros
/usr/lib/rpm/platform/mips64r6-linux/macros
/usr/lib/rpm/platform/mips64r6el-linux/macros
/usr/lib/rpm/platform/mipsel-linux/macros
/usr/lib/rpm/platform/mipsr6-linux/macros
/usr/lib/rpm/platform/mipsr6el-linux/macros
/usr/lib/rpm/platform/noarch-linux/macros
/usr/lib/rpm/platform/pentium3-linux/macros
/usr/lib/rpm/platform/pentium4-linux/macros
/usr/lib/rpm/platform/ppc-linux/macros
/usr/lib/rpm/platform/ppc32dy4-linux/macros
/usr/lib/rpm/platform/ppc64-linux/macros
/usr/lib/rpm/platform/ppc64iseries-linux/macros
/usr/lib/rpm/platform/ppc64le-linux/macros
/usr/lib/rpm/platform/ppc64p7-linux/macros
/usr/lib/rpm/platform/ppc64pseries-linux/macros
/usr/lib/rpm/platform/ppc8260-linux/macros
/usr/lib/rpm/platform/ppc8560-linux/macros
/usr/lib/rpm/platform/ppciseries-linux/macros
/usr/lib/rpm/platform/ppcpseries-linux/macros
/usr/lib/rpm/platform/riscv64-linux/macros
/usr/lib/rpm/platform/s390-linux/macros
/usr/lib/rpm/platform/s390x-linux/macros
/usr/lib/rpm/platform/sh-linux/macros
/usr/lib/rpm/platform/sh3-linux/macros
/usr/lib/rpm/platform/sh4-linux/macros
/usr/lib/rpm/platform/sh4a-linux/macros
/usr/lib/rpm/platform/sparc-linux/macros
/usr/lib/rpm/platform/sparc64-linux/macros
/usr/lib/rpm/platform/sparc64v-linux/macros
/usr/lib/rpm/platform/sparcv8-linux/macros
/usr/lib/rpm/platform/sparcv9-linux/macros
/usr/lib/rpm/platform/sparcv9v-linux/macros
/usr/lib/rpm/platform/x86_64-linux/macros
/usr/lib/rpm/python-macro-helper
/usr/lib/rpm/pythondeps.sh
/usr/lib/rpm/pythondistdeps.py
/usr/lib/rpm/rpm.daily
/usr/lib/rpm/rpm.log
/usr/lib/rpm/rpm.supp
/usr/lib/rpm/rpm2cpio.sh
/usr/lib/rpm/rpmdb_loadcvt
/usr/lib/rpm/rpmdeps
/usr/lib/rpm/rpmpopt-4.14.2.1
/usr/lib/rpm/rpmrc
/usr/lib/rpm/script.req
/usr/lib/rpm/sepdebugcrcfix
/usr/lib/rpm/tgpg

%files bin
%defattr(-,root,root,-)
/usr/bin/gendiff
/usr/bin/rpm
/usr/bin/rpm2archive
/usr/bin/rpmbuild
/usr/bin/rpmdb
/usr/bin/rpmgraph
/usr/bin/rpmkeys
/usr/bin/rpmquery
/usr/bin/rpmsign
/usr/bin/rpmspec
/usr/bin/rpmverify

%files dev
%defattr(-,root,root,-)
/usr/include/rpm/argv.h
/usr/include/rpm/header.h
/usr/include/rpm/rpmarchive.h
/usr/include/rpm/rpmbase64.h
/usr/include/rpm/rpmbuild.h
/usr/include/rpm/rpmcallback.h
/usr/include/rpm/rpmcli.h
/usr/include/rpm/rpmdb.h
/usr/include/rpm/rpmds.h
/usr/include/rpm/rpmfc.h
/usr/include/rpm/rpmfi.h
/usr/include/rpm/rpmfiles.h
/usr/include/rpm/rpmfileutil.h
/usr/include/rpm/rpmio.h
/usr/include/rpm/rpmkeyring.h
/usr/include/rpm/rpmlib.h
/usr/include/rpm/rpmlog.h
/usr/include/rpm/rpmmacro.h
/usr/include/rpm/rpmpgp.h
/usr/include/rpm/rpmpol.h
/usr/include/rpm/rpmprob.h
/usr/include/rpm/rpmps.h
/usr/include/rpm/rpmsign.h
/usr/include/rpm/rpmspec.h
/usr/include/rpm/rpmsq.h
/usr/include/rpm/rpmstring.h
/usr/include/rpm/rpmstrpool.h
/usr/include/rpm/rpmsw.h
/usr/include/rpm/rpmtag.h
/usr/include/rpm/rpmtd.h
/usr/include/rpm/rpmte.h
/usr/include/rpm/rpmts.h
/usr/include/rpm/rpmtypes.h
/usr/include/rpm/rpmurl.h
/usr/include/rpm/rpmutil.h
/usr/include/rpm/rpmvf.h
/usr/lib64/librpm.so
/usr/lib64/librpmbuild.so
/usr/lib64/librpmio.so
/usr/lib64/librpmsign.so
/usr/lib64/pkgconfig/rpm.pc
/usr/lib64/rpm-plugins/ima.so
/usr/lib64/rpm-plugins/ldconfig.so
/usr/lib64/rpm-plugins/prioreset.so
/usr/lib64/rpm-plugins/syslog.so

%files extras
%defattr(-,root,root,-)
/usr/bin/rpm2cpio

%files lib
%defattr(-,root,root,-)
/usr/lib64/librpm.so.8
/usr/lib64/librpm.so.8.1.0
/usr/lib64/librpmbuild.so.8
/usr/lib64/librpmbuild.so.8.1.0
/usr/lib64/librpmio.so.8
/usr/lib64/librpmio.so.8.1.0
/usr/lib64/librpmsign.so.8
/usr/lib64/librpmsign.so.8.1.0

%files man
%defattr(0644,root,root,0755)
/usr/share/man/fr/man8/rpm.8
/usr/share/man/ja/man8/rpm.8
/usr/share/man/ja/man8/rpm2cpio.8
/usr/share/man/ja/man8/rpmbuild.8
/usr/share/man/ja/man8/rpmgraph.8
/usr/share/man/ko/man8/rpm.8
/usr/share/man/ko/man8/rpm2cpio.8
/usr/share/man/man1/gendiff.1
/usr/share/man/man8/rpm-misc.8
/usr/share/man/man8/rpm-plugin-systemd-inhibit.8
/usr/share/man/man8/rpm.8
/usr/share/man/man8/rpm2cpio.8
/usr/share/man/man8/rpmbuild.8
/usr/share/man/man8/rpmdb.8
/usr/share/man/man8/rpmdeps.8
/usr/share/man/man8/rpmgraph.8
/usr/share/man/man8/rpmkeys.8
/usr/share/man/man8/rpmsign.8
/usr/share/man/man8/rpmspec.8
/usr/share/man/pl/man1/gendiff.1
/usr/share/man/pl/man8/rpm.8
/usr/share/man/pl/man8/rpm2cpio.8
/usr/share/man/pl/man8/rpmbuild.8
/usr/share/man/pl/man8/rpmdeps.8
/usr/share/man/pl/man8/rpmgraph.8
/usr/share/man/ru/man8/rpm.8
/usr/share/man/ru/man8/rpm2cpio.8
/usr/share/man/sk/man8/rpm.8

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

%files locales -f rpm.lang
%defattr(-,root,root,-)
