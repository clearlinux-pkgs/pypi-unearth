#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
#
Name     : pypi-unearth
Version  : 0.9.2
Release  : 3
URL      : https://files.pythonhosted.org/packages/2e/14/7a73dc88a96ae767bceb516655363fbcceb899baae848b94ee6f42417344/unearth-0.9.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/2e/14/7a73dc88a96ae767bceb516655363fbcceb899baae848b94ee6f42417344/unearth-0.9.2.tar.gz
Summary  : A utility to fetch and download python packages
Group    : Development/Tools
License  : MIT
Requires: pypi-unearth-bin = %{version}-%{release}
Requires: pypi-unearth-license = %{version}-%{release}
Requires: pypi-unearth-python = %{version}-%{release}
Requires: pypi-unearth-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(pdm_pep517)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# unearth
<!--index start-->
[![Tests](https://github.com/frostming/unearth/workflows/Tests/badge.svg)](https://github.com/frostming/unearth/actions?query=workflow%3Aci)
[![pypi version](https://img.shields.io/pypi/v/unearth.svg)](https://pypi.org/project/unearth/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![pdm-managed](https://img.shields.io/badge/pdm-managed-blueviolet)](https://pdm.fming.dev)

%package bin
Summary: bin components for the pypi-unearth package.
Group: Binaries
Requires: pypi-unearth-license = %{version}-%{release}

%description bin
bin components for the pypi-unearth package.


%package license
Summary: license components for the pypi-unearth package.
Group: Default

%description license
license components for the pypi-unearth package.


%package python
Summary: python components for the pypi-unearth package.
Group: Default
Requires: pypi-unearth-python3 = %{version}-%{release}

%description python
python components for the pypi-unearth package.


%package python3
Summary: python3 components for the pypi-unearth package.
Group: Default
Requires: python3-core
Provides: pypi(unearth)
Requires: pypi(packaging)
Requires: pypi(requests)

%description python3
python3 components for the pypi-unearth package.


%prep
%setup -q -n unearth-0.9.2
cd %{_builddir}/unearth-0.9.2
pushd ..
cp -a unearth-0.9.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1688574124
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-unearth
cp %{_builddir}/unearth-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-unearth/09a428a2d5dd8dd70f7cb16bc0cf47c43ddc20ae || :
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/unearth

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-unearth/09a428a2d5dd8dd70f7cb16bc0cf47c43ddc20ae

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
