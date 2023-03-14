#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-vctrs
Version  : 0.5.2
Release  : 48
URL      : https://cran.r-project.org/src/contrib/vctrs_0.5.2.tar.gz
Source0  : https://cran.r-project.org/src/contrib/vctrs_0.5.2.tar.gz
Summary  : Vector Helpers
Group    : Development/Tools
License  : MIT MPL-2.0
Requires: R-vctrs-lib = %{version}-%{release}
Requires: R-vctrs-license = %{version}-%{release}
Requires: R-cli
Requires: R-glue
Requires: R-lifecycle
Requires: R-rlang
BuildRequires : R-cli
BuildRequires : R-glue
BuildRequires : R-lifecycle
BuildRequires : R-rlang
BuildRequires : buildreq-R

%description
used to provide tools for consistent and well-founded type-coercion
    and size-recycling, and are in turn connected to ideas of type- and
    size-stability useful for analysing function interfaces.

%package lib
Summary: lib components for the R-vctrs package.
Group: Libraries
Requires: R-vctrs-license = %{version}-%{release}

%description lib
lib components for the R-vctrs package.


%package license
Summary: license components for the R-vctrs package.
Group: Default

%description license
license components for the R-vctrs package.


%prep
%setup -q -n vctrs
cd %{_builddir}/vctrs

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1678827026

%install
export SOURCE_DATE_EPOCH=1678827026
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/R-vctrs
cp %{_builddir}/vctrs/LICENSE.note %{buildroot}/usr/share/package-licenses/R-vctrs/b4cf59cc3bbfb71e343bf658f63c2a3398e8b61f || :
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/vctrs/DESCRIPTION
/usr/lib64/R/library/vctrs/INDEX
/usr/lib64/R/library/vctrs/LICENSE
/usr/lib64/R/library/vctrs/Meta/Rd.rds
/usr/lib64/R/library/vctrs/Meta/features.rds
/usr/lib64/R/library/vctrs/Meta/hsearch.rds
/usr/lib64/R/library/vctrs/Meta/links.rds
/usr/lib64/R/library/vctrs/Meta/nsInfo.rds
/usr/lib64/R/library/vctrs/Meta/package.rds
/usr/lib64/R/library/vctrs/Meta/vignette.rds
/usr/lib64/R/library/vctrs/NAMESPACE
/usr/lib64/R/library/vctrs/NEWS.md
/usr/lib64/R/library/vctrs/R/vctrs
/usr/lib64/R/library/vctrs/R/vctrs.rdb
/usr/lib64/R/library/vctrs/R/vctrs.rdx
/usr/lib64/R/library/vctrs/WORDLIST
/usr/lib64/R/library/vctrs/doc/index.html
/usr/lib64/R/library/vctrs/doc/pillar.R
/usr/lib64/R/library/vctrs/doc/pillar.Rmd
/usr/lib64/R/library/vctrs/doc/pillar.html
/usr/lib64/R/library/vctrs/doc/s3-vector.R
/usr/lib64/R/library/vctrs/doc/s3-vector.Rmd
/usr/lib64/R/library/vctrs/doc/s3-vector.html
/usr/lib64/R/library/vctrs/doc/stability.R
/usr/lib64/R/library/vctrs/doc/stability.Rmd
/usr/lib64/R/library/vctrs/doc/stability.html
/usr/lib64/R/library/vctrs/doc/type-size.R
/usr/lib64/R/library/vctrs/doc/type-size.Rmd
/usr/lib64/R/library/vctrs/doc/type-size.html
/usr/lib64/R/library/vctrs/help/AnIndex
/usr/lib64/R/library/vctrs/help/aliases.rds
/usr/lib64/R/library/vctrs/help/figures/cast.png
/usr/lib64/R/library/vctrs/help/figures/coerce.png
/usr/lib64/R/library/vctrs/help/figures/combined.png
/usr/lib64/R/library/vctrs/help/figures/lifecycle-archived.svg
/usr/lib64/R/library/vctrs/help/figures/lifecycle-defunct.svg
/usr/lib64/R/library/vctrs/help/figures/lifecycle-deprecated.svg
/usr/lib64/R/library/vctrs/help/figures/lifecycle-experimental.svg
/usr/lib64/R/library/vctrs/help/figures/lifecycle-maturing.svg
/usr/lib64/R/library/vctrs/help/figures/lifecycle-questioning.svg
/usr/lib64/R/library/vctrs/help/figures/lifecycle-soft-deprecated.svg
/usr/lib64/R/library/vctrs/help/figures/lifecycle-stable.svg
/usr/lib64/R/library/vctrs/help/figures/lifecycle-superseded.svg
/usr/lib64/R/library/vctrs/help/figures/logo.png
/usr/lib64/R/library/vctrs/help/figures/sizes-recycling.png
/usr/lib64/R/library/vctrs/help/figures/vec-count-deps.png
/usr/lib64/R/library/vctrs/help/figures/vec-count-deps.svg
/usr/lib64/R/library/vctrs/help/paths.rds
/usr/lib64/R/library/vctrs/help/vctrs.rdb
/usr/lib64/R/library/vctrs/help/vctrs.rdx
/usr/lib64/R/library/vctrs/html/00Index.html
/usr/lib64/R/library/vctrs/html/R.css
/usr/lib64/R/library/vctrs/include/vctrs.c
/usr/lib64/R/library/vctrs/include/vctrs.h
/usr/lib64/R/library/vctrs/tests/testthat.R
/usr/lib64/R/library/vctrs/tests/testthat/_snaps/assert.md
/usr/lib64/R/library/vctrs/tests/testthat/_snaps/bind.md
/usr/lib64/R/library/vctrs/tests/testthat/_snaps/c.md
/usr/lib64/R/library/vctrs/tests/testthat/_snaps/cast.md
/usr/lib64/R/library/vctrs/tests/testthat/_snaps/compare.md
/usr/lib64/R/library/vctrs/tests/testthat/_snaps/conditions.md
/usr/lib64/R/library/vctrs/tests/testthat/_snaps/dictionary.md
/usr/lib64/R/library/vctrs/tests/testthat/_snaps/error-call.md
/usr/lib64/R/library/vctrs/tests/testthat/_snaps/expand.md
/usr/lib64/R/library/vctrs/tests/testthat/_snaps/group.md
/usr/lib64/R/library/vctrs/tests/testthat/_snaps/hash.md
/usr/lib64/R/library/vctrs/tests/testthat/_snaps/interval.md
/usr/lib64/R/library/vctrs/tests/testthat/_snaps/lifecycle-deprecated.md
/usr/lib64/R/library/vctrs/tests/testthat/_snaps/match.md
/usr/lib64/R/library/vctrs/tests/testthat/_snaps/names.md
/usr/lib64/R/library/vctrs/tests/testthat/_snaps/order.md
/usr/lib64/R/library/vctrs/tests/testthat/_snaps/partial-factor.md
/usr/lib64/R/library/vctrs/tests/testthat/_snaps/partial-frame.md
/usr/lib64/R/library/vctrs/tests/testthat/_snaps/print-str.md
/usr/lib64/R/library/vctrs/tests/testthat/_snaps/ptype-abbr-full.md
/usr/lib64/R/library/vctrs/tests/testthat/_snaps/rank.md
/usr/lib64/R/library/vctrs/tests/testthat/_snaps/recycle.md
/usr/lib64/R/library/vctrs/tests/testthat/_snaps/rep.md
/usr/lib64/R/library/vctrs/tests/testthat/_snaps/runs.md
/usr/lib64/R/library/vctrs/tests/testthat/_snaps/set.md
/usr/lib64/R/library/vctrs/tests/testthat/_snaps/shape.md
/usr/lib64/R/library/vctrs/tests/testthat/_snaps/size.md
/usr/lib64/R/library/vctrs/tests/testthat/_snaps/slice-assign.md
/usr/lib64/R/library/vctrs/tests/testthat/_snaps/slice-chop.md
/usr/lib64/R/library/vctrs/tests/testthat/_snaps/slice-interleave.md
/usr/lib64/R/library/vctrs/tests/testthat/_snaps/slice.md
/usr/lib64/R/library/vctrs/tests/testthat/_snaps/subscript-loc.md
/usr/lib64/R/library/vctrs/tests/testthat/_snaps/subscript.md
/usr/lib64/R/library/vctrs/tests/testthat/_snaps/type-asis.md
/usr/lib64/R/library/vctrs/tests/testthat/_snaps/type-data-frame.md
/usr/lib64/R/library/vctrs/tests/testthat/_snaps/type-date-time.md
/usr/lib64/R/library/vctrs/tests/testthat/_snaps/type-factor.md
/usr/lib64/R/library/vctrs/tests/testthat/_snaps/type-list-of.md
/usr/lib64/R/library/vctrs/tests/testthat/_snaps/type-misc.md
/usr/lib64/R/library/vctrs/tests/testthat/_snaps/type-rcrd.md
/usr/lib64/R/library/vctrs/tests/testthat/_snaps/type-table.md
/usr/lib64/R/library/vctrs/tests/testthat/_snaps/type-tibble.md
/usr/lib64/R/library/vctrs/tests/testthat/_snaps/type-unspecified.md
/usr/lib64/R/library/vctrs/tests/testthat/_snaps/type-vctr.md
/usr/lib64/R/library/vctrs/tests/testthat/_snaps/type.md
/usr/lib64/R/library/vctrs/tests/testthat/_snaps/type2.md
/usr/lib64/R/library/vctrs/tests/testthat/helper-c.R
/usr/lib64/R/library/vctrs/tests/testthat/helper-cast.R
/usr/lib64/R/library/vctrs/tests/testthat/helper-conditions.R
/usr/lib64/R/library/vctrs/tests/testthat/helper-encoding.R
/usr/lib64/R/library/vctrs/tests/testthat/helper-expectations.R
/usr/lib64/R/library/vctrs/tests/testthat/helper-memory.R
/usr/lib64/R/library/vctrs/tests/testthat/helper-names.R
/usr/lib64/R/library/vctrs/tests/testthat/helper-order.R
/usr/lib64/R/library/vctrs/tests/testthat/helper-performance.R
/usr/lib64/R/library/vctrs/tests/testthat/helper-rational.R
/usr/lib64/R/library/vctrs/tests/testthat/helper-restart.R
/usr/lib64/R/library/vctrs/tests/testthat/helper-s3.R
/usr/lib64/R/library/vctrs/tests/testthat/helper-s4.R
/usr/lib64/R/library/vctrs/tests/testthat/helper-shape.R
/usr/lib64/R/library/vctrs/tests/testthat/helper-size.R
/usr/lib64/R/library/vctrs/tests/testthat/helper-type-dplyr.R
/usr/lib64/R/library/vctrs/tests/testthat/helper-types.R
/usr/lib64/R/library/vctrs/tests/testthat/helper-vctrs.R
/usr/lib64/R/library/vctrs/tests/testthat/test-arith.R
/usr/lib64/R/library/vctrs/tests/testthat/test-assert.R
/usr/lib64/R/library/vctrs/tests/testthat/test-bind.R
/usr/lib64/R/library/vctrs/tests/testthat/test-c.R
/usr/lib64/R/library/vctrs/tests/testthat/test-cast.R
/usr/lib64/R/library/vctrs/tests/testthat/test-compare.R
/usr/lib64/R/library/vctrs/tests/testthat/test-complete.R
/usr/lib64/R/library/vctrs/tests/testthat/test-conditions.R
/usr/lib64/R/library/vctrs/tests/testthat/test-dictionary.R
/usr/lib64/R/library/vctrs/tests/testthat/test-dim.R
/usr/lib64/R/library/vctrs/tests/testthat/test-empty.R
/usr/lib64/R/library/vctrs/tests/testthat/test-equal.R
/usr/lib64/R/library/vctrs/tests/testthat/test-error-call.R
/usr/lib64/R/library/vctrs/tests/testthat/test-expand.R
/usr/lib64/R/library/vctrs/tests/testthat/test-fields.R
/usr/lib64/R/library/vctrs/tests/testthat/test-fill.R
/usr/lib64/R/library/vctrs/tests/testthat/test-group.R
/usr/lib64/R/library/vctrs/tests/testthat/test-hash.R
/usr/lib64/R/library/vctrs/tests/testthat/test-interval.R
/usr/lib64/R/library/vctrs/tests/testthat/test-lifecycle-deprecated.R
/usr/lib64/R/library/vctrs/tests/testthat/test-match.R
/usr/lib64/R/library/vctrs/tests/testthat/test-missing.R
/usr/lib64/R/library/vctrs/tests/testthat/test-names.R
/usr/lib64/R/library/vctrs/tests/testthat/test-order.R
/usr/lib64/R/library/vctrs/tests/testthat/test-partial-factor.R
/usr/lib64/R/library/vctrs/tests/testthat/test-partial-frame.R
/usr/lib64/R/library/vctrs/tests/testthat/test-print-str.R
/usr/lib64/R/library/vctrs/tests/testthat/test-proxy-restore.R
/usr/lib64/R/library/vctrs/tests/testthat/test-proxy.R
/usr/lib64/R/library/vctrs/tests/testthat/test-ptype-abbr-full.R
/usr/lib64/R/library/vctrs/tests/testthat/test-rank.R
/usr/lib64/R/library/vctrs/tests/testthat/test-recycle.R
/usr/lib64/R/library/vctrs/tests/testthat/test-rep.R
/usr/lib64/R/library/vctrs/tests/testthat/test-runs.R
/usr/lib64/R/library/vctrs/tests/testthat/test-s4.R
/usr/lib64/R/library/vctrs/tests/testthat/test-set.R
/usr/lib64/R/library/vctrs/tests/testthat/test-shape.R
/usr/lib64/R/library/vctrs/tests/testthat/test-size.R
/usr/lib64/R/library/vctrs/tests/testthat/test-slice-assign.R
/usr/lib64/R/library/vctrs/tests/testthat/test-slice-chop.R
/usr/lib64/R/library/vctrs/tests/testthat/test-slice-interleave.R
/usr/lib64/R/library/vctrs/tests/testthat/test-slice.R
/usr/lib64/R/library/vctrs/tests/testthat/test-split.R
/usr/lib64/R/library/vctrs/tests/testthat/test-subscript-loc.R
/usr/lib64/R/library/vctrs/tests/testthat/test-subscript.R
/usr/lib64/R/library/vctrs/tests/testthat/test-translate.R
/usr/lib64/R/library/vctrs/tests/testthat/test-type-asis.R
/usr/lib64/R/library/vctrs/tests/testthat/test-type-bare.R
/usr/lib64/R/library/vctrs/tests/testthat/test-type-data-frame.R
/usr/lib64/R/library/vctrs/tests/testthat/test-type-date-time.R
/usr/lib64/R/library/vctrs/tests/testthat/test-type-dplyr.R
/usr/lib64/R/library/vctrs/tests/testthat/test-type-factor.R
/usr/lib64/R/library/vctrs/tests/testthat/test-type-integer64.R
/usr/lib64/R/library/vctrs/tests/testthat/test-type-list-of.R
/usr/lib64/R/library/vctrs/tests/testthat/test-type-misc.R
/usr/lib64/R/library/vctrs/tests/testthat/test-type-rational.R
/usr/lib64/R/library/vctrs/tests/testthat/test-type-rcrd.R
/usr/lib64/R/library/vctrs/tests/testthat/test-type-sclr.R
/usr/lib64/R/library/vctrs/tests/testthat/test-type-sf.R
/usr/lib64/R/library/vctrs/tests/testthat/test-type-table.R
/usr/lib64/R/library/vctrs/tests/testthat/test-type-tibble.R
/usr/lib64/R/library/vctrs/tests/testthat/test-type-unspecified.R
/usr/lib64/R/library/vctrs/tests/testthat/test-type-vctr.R
/usr/lib64/R/library/vctrs/tests/testthat/test-type.R
/usr/lib64/R/library/vctrs/tests/testthat/test-type2.R
/usr/lib64/R/library/vctrs/tests/testthat/test-utils.R
/usr/lib64/R/library/vctrs/tests/testthat/test-vctrs.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/vctrs/libs/vctrs.so
/usr/lib64/R/library/vctrs/libs/vctrs.so.avx2
/usr/lib64/R/library/vctrs/libs/vctrs.so.avx512

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/R-vctrs/b4cf59cc3bbfb71e343bf658f63c2a3398e8b61f
