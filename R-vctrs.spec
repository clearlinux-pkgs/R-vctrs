#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-vctrs
Version  : 0.3.6
Release  : 23
URL      : https://cran.r-project.org/src/contrib/vctrs_0.3.6.tar.gz
Source0  : https://cran.r-project.org/src/contrib/vctrs_0.3.6.tar.gz
Summary  : Vector Helpers
Group    : Development/Tools
License  : MIT MPL-2.0
Requires: R-vctrs-lib = %{version}-%{release}
Requires: R-digest
Requires: R-ellipsis
Requires: R-glue
Requires: R-rlang
BuildRequires : R-digest
BuildRequires : R-ellipsis
BuildRequires : R-glue
BuildRequires : R-rlang
BuildRequires : buildreq-R

%description
used to provide tools for consistent and well-founded type-coercion
    and size-recycling, and are in turn connected to ideas of type- and
    size-stability useful for analysing function interfaces.

%package lib
Summary: lib components for the R-vctrs package.
Group: Libraries

%description lib
lib components for the R-vctrs package.


%prep
%setup -q -c -n vctrs
cd %{_builddir}/vctrs

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1608224443

%install
export SOURCE_DATE_EPOCH=1608224443
rm -rf %{buildroot}
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
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library vctrs
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library vctrs
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library vctrs
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc vctrs || :


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
/usr/lib64/R/library/vctrs/tests/testthat/error/test-bind.txt
/usr/lib64/R/library/vctrs/tests/testthat/error/test-c.txt
/usr/lib64/R/library/vctrs/tests/testthat/error/test-cast.txt
/usr/lib64/R/library/vctrs/tests/testthat/error/test-conditions.txt
/usr/lib64/R/library/vctrs/tests/testthat/error/test-dictionary.txt
/usr/lib64/R/library/vctrs/tests/testthat/error/test-recycle.txt
/usr/lib64/R/library/vctrs/tests/testthat/error/test-rep.txt
/usr/lib64/R/library/vctrs/tests/testthat/error/test-shape.txt
/usr/lib64/R/library/vctrs/tests/testthat/error/test-slice-assign.txt
/usr/lib64/R/library/vctrs/tests/testthat/error/test-slice.txt
/usr/lib64/R/library/vctrs/tests/testthat/error/test-subscript-loc.txt
/usr/lib64/R/library/vctrs/tests/testthat/error/test-subscript.txt
/usr/lib64/R/library/vctrs/tests/testthat/error/test-type-asis.txt
/usr/lib64/R/library/vctrs/tests/testthat/error/test-type-data-frame.txt
/usr/lib64/R/library/vctrs/tests/testthat/error/test-type2.txt
/usr/lib64/R/library/vctrs/tests/testthat/error/test-unchop.txt
/usr/lib64/R/library/vctrs/tests/testthat/helper-c.R
/usr/lib64/R/library/vctrs/tests/testthat/helper-cast.R
/usr/lib64/R/library/vctrs/tests/testthat/helper-conditions.R
/usr/lib64/R/library/vctrs/tests/testthat/helper-encoding.R
/usr/lib64/R/library/vctrs/tests/testthat/helper-expectations.R
/usr/lib64/R/library/vctrs/tests/testthat/helper-memory.R
/usr/lib64/R/library/vctrs/tests/testthat/helper-order.R
/usr/lib64/R/library/vctrs/tests/testthat/helper-output.R
/usr/lib64/R/library/vctrs/tests/testthat/helper-performance.R
/usr/lib64/R/library/vctrs/tests/testthat/helper-rational.R
/usr/lib64/R/library/vctrs/tests/testthat/helper-s3.R
/usr/lib64/R/library/vctrs/tests/testthat/helper-s4.R
/usr/lib64/R/library/vctrs/tests/testthat/helper-shape.R
/usr/lib64/R/library/vctrs/tests/testthat/helper-size.R
/usr/lib64/R/library/vctrs/tests/testthat/helper-type-dplyr.R
/usr/lib64/R/library/vctrs/tests/testthat/helper-types.R
/usr/lib64/R/library/vctrs/tests/testthat/helper-vctrs.R
/usr/lib64/R/library/vctrs/tests/testthat/out/vec-ptype-0.txt
/usr/lib64/R/library/vctrs/tests/testthat/out/vec-ptype-1.txt
/usr/lib64/R/library/vctrs/tests/testthat/out/vec-ptype-2.txt
/usr/lib64/R/library/vctrs/tests/testthat/out/vec-ptype-3.txt
/usr/lib64/R/library/vctrs/tests/testthat/output/bind-name-repair.txt
/usr/lib64/R/library/vctrs/tests/testthat/output/test-vec-as-names.txt
/usr/lib64/R/library/vctrs/tests/testthat/performance/test-bind.txt
/usr/lib64/R/library/vctrs/tests/testthat/performance/test-c.txt
/usr/lib64/R/library/vctrs/tests/testthat/test-arith.R
/usr/lib64/R/library/vctrs/tests/testthat/test-assert-explanations.txt
/usr/lib64/R/library/vctrs/tests/testthat/test-assert.R
/usr/lib64/R/library/vctrs/tests/testthat/test-bind.R
/usr/lib64/R/library/vctrs/tests/testthat/test-c.R
/usr/lib64/R/library/vctrs/tests/testthat/test-cast-error-nested.txt
/usr/lib64/R/library/vctrs/tests/testthat/test-cast-list.R
/usr/lib64/R/library/vctrs/tests/testthat/test-cast.R
/usr/lib64/R/library/vctrs/tests/testthat/test-compare.R
/usr/lib64/R/library/vctrs/tests/testthat/test-complete.R
/usr/lib64/R/library/vctrs/tests/testthat/test-conditions.R
/usr/lib64/R/library/vctrs/tests/testthat/test-dictionary.R
/usr/lib64/R/library/vctrs/tests/testthat/test-dim.R
/usr/lib64/R/library/vctrs/tests/testthat/test-empty.R
/usr/lib64/R/library/vctrs/tests/testthat/test-equal.R
/usr/lib64/R/library/vctrs/tests/testthat/test-fields.R
/usr/lib64/R/library/vctrs/tests/testthat/test-fill.R
/usr/lib64/R/library/vctrs/tests/testthat/test-group.R
/usr/lib64/R/library/vctrs/tests/testthat/test-hash-hash.txt
/usr/lib64/R/library/vctrs/tests/testthat/test-hash.R
/usr/lib64/R/library/vctrs/tests/testthat/test-lifecycle-deprecated.R
/usr/lib64/R/library/vctrs/tests/testthat/test-list_of-print.txt
/usr/lib64/R/library/vctrs/tests/testthat/test-list_of-str-empty.txt
/usr/lib64/R/library/vctrs/tests/testthat/test-list_of-str.txt
/usr/lib64/R/library/vctrs/tests/testthat/test-list_of-type.txt
/usr/lib64/R/library/vctrs/tests/testthat/test-names.R
/usr/lib64/R/library/vctrs/tests/testthat/test-order-radix.R
/usr/lib64/R/library/vctrs/tests/testthat/test-order.R
/usr/lib64/R/library/vctrs/tests/testthat/test-partial-factor-print-both.txt
/usr/lib64/R/library/vctrs/tests/testthat/test-partial-factor-print-empty.txt
/usr/lib64/R/library/vctrs/tests/testthat/test-partial-factor-print-learned.txt
/usr/lib64/R/library/vctrs/tests/testthat/test-partial-factor-print-partial.txt
/usr/lib64/R/library/vctrs/tests/testthat/test-partial-factor.R
/usr/lib64/R/library/vctrs/tests/testthat/test-partial-frame-print.txt
/usr/lib64/R/library/vctrs/tests/testthat/test-partial-frame.R
/usr/lib64/R/library/vctrs/tests/testthat/test-print-str-attr.txt
/usr/lib64/R/library/vctrs/tests/testthat/test-print-str-mtcars.txt
/usr/lib64/R/library/vctrs/tests/testthat/test-print-str.R
/usr/lib64/R/library/vctrs/tests/testthat/test-proxy-restore.R
/usr/lib64/R/library/vctrs/tests/testthat/test-proxy.R
/usr/lib64/R/library/vctrs/tests/testthat/test-ptype-abbr-full.R
/usr/lib64/R/library/vctrs/tests/testthat/test-rcrd-format.txt
/usr/lib64/R/library/vctrs/tests/testthat/test-recycle.R
/usr/lib64/R/library/vctrs/tests/testthat/test-rep.R
/usr/lib64/R/library/vctrs/tests/testthat/test-runs.R
/usr/lib64/R/library/vctrs/tests/testthat/test-s4.R
/usr/lib64/R/library/vctrs/tests/testthat/test-shape-print.txt
/usr/lib64/R/library/vctrs/tests/testthat/test-shape.R
/usr/lib64/R/library/vctrs/tests/testthat/test-size.R
/usr/lib64/R/library/vctrs/tests/testthat/test-slice-assign.R
/usr/lib64/R/library/vctrs/tests/testthat/test-slice-chop.R
/usr/lib64/R/library/vctrs/tests/testthat/test-slice.R
/usr/lib64/R/library/vctrs/tests/testthat/test-split.R
/usr/lib64/R/library/vctrs/tests/testthat/test-subscript-loc.R
/usr/lib64/R/library/vctrs/tests/testthat/test-subscript.R
/usr/lib64/R/library/vctrs/tests/testthat/test-translate.R
/usr/lib64/R/library/vctrs/tests/testthat/test-type-asis.R
/usr/lib64/R/library/vctrs/tests/testthat/test-type-bare.R
/usr/lib64/R/library/vctrs/tests/testthat/test-type-data-frame-embedded.txt
/usr/lib64/R/library/vctrs/tests/testthat/test-type-data-frame.R
/usr/lib64/R/library/vctrs/tests/testthat/test-type-data-frame.txt
/usr/lib64/R/library/vctrs/tests/testthat/test-type-date-time.R
/usr/lib64/R/library/vctrs/tests/testthat/test-type-date-time.txt
/usr/lib64/R/library/vctrs/tests/testthat/test-type-dplyr.R
/usr/lib64/R/library/vctrs/tests/testthat/test-type-factor.R
/usr/lib64/R/library/vctrs/tests/testthat/test-type-factor.txt
/usr/lib64/R/library/vctrs/tests/testthat/test-type-group-rle.txt
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
/usr/lib64/R/library/vctrs/tests/testthat/test-type-unspecified.txt
/usr/lib64/R/library/vctrs/tests/testthat/test-type-vctr.R
/usr/lib64/R/library/vctrs/tests/testthat/test-type-vec-c-error.txt
/usr/lib64/R/library/vctrs/tests/testthat/test-type-vec-size-common-error.txt
/usr/lib64/R/library/vctrs/tests/testthat/test-type-vec-type-common-error.txt
/usr/lib64/R/library/vctrs/tests/testthat/test-type.R
/usr/lib64/R/library/vctrs/tests/testthat/test-type2-error-messages.txt
/usr/lib64/R/library/vctrs/tests/testthat/test-type2.R
/usr/lib64/R/library/vctrs/tests/testthat/test-type2.txt
/usr/lib64/R/library/vctrs/tests/testthat/test-utils.R
/usr/lib64/R/library/vctrs/tests/testthat/test-vctr-print-names.txt
/usr/lib64/R/library/vctrs/tests/testthat/test-vctr-print.txt
/usr/lib64/R/library/vctrs/tests/testthat/test-vctrs.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/vctrs/libs/vctrs.so
/usr/lib64/R/library/vctrs/libs/vctrs.so.avx2
/usr/lib64/R/library/vctrs/libs/vctrs.so.avx512
