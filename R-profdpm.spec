#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-profdpm
Version  : 3.3
Release  : 6
URL      : https://cran.r-project.org/src/contrib/profdpm_3.3.tar.gz
Source0  : https://cran.r-project.org/src/contrib/profdpm_3.3.tar.gz
Summary  : Profile Dirichlet Process Mixtures
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-profdpm-lib = %{version}-%{release}
BuildRequires : buildreq-R

%description
the posterior mode) for a class of product partition models
        (PPM). The Dirichlet process mixture is currently the only
        available member of this class. These methods search for the
        maximum posterior (MAP) estimate for the data partition in a
        PPM.

%package lib
Summary: lib components for the R-profdpm package.
Group: Libraries

%description lib
lib components for the R-profdpm package.


%prep
%setup -q -c -n profdpm

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1552936369

%install
export SOURCE_DATE_EPOCH=1552936369
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library profdpm
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library profdpm
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library profdpm
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc  profdpm || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/profdpm/CITATION
/usr/lib64/R/library/profdpm/DESCRIPTION
/usr/lib64/R/library/profdpm/INDEX
/usr/lib64/R/library/profdpm/Meta/Rd.rds
/usr/lib64/R/library/profdpm/Meta/features.rds
/usr/lib64/R/library/profdpm/Meta/hsearch.rds
/usr/lib64/R/library/profdpm/Meta/links.rds
/usr/lib64/R/library/profdpm/Meta/nsInfo.rds
/usr/lib64/R/library/profdpm/Meta/package.rds
/usr/lib64/R/library/profdpm/Meta/vignette.rds
/usr/lib64/R/library/profdpm/NAMESPACE
/usr/lib64/R/library/profdpm/R/profdpm
/usr/lib64/R/library/profdpm/R/profdpm.rdb
/usr/lib64/R/library/profdpm/R/profdpm.rdx
/usr/lib64/R/library/profdpm/doc/index.html
/usr/lib64/R/library/profdpm/doc/profdpm.R
/usr/lib64/R/library/profdpm/doc/profdpm.Rnw
/usr/lib64/R/library/profdpm/doc/profdpm.pdf
/usr/lib64/R/library/profdpm/help/AnIndex
/usr/lib64/R/library/profdpm/help/aliases.rds
/usr/lib64/R/library/profdpm/help/paths.rds
/usr/lib64/R/library/profdpm/help/profdpm.rdb
/usr/lib64/R/library/profdpm/help/profdpm.rdx
/usr/lib64/R/library/profdpm/html/00Index.html
/usr/lib64/R/library/profdpm/html/R.css

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/profdpm/libs/profdpm.so
/usr/lib64/R/library/profdpm/libs/profdpm.so.avx2
/usr/lib64/R/library/profdpm/libs/profdpm.so.avx512
