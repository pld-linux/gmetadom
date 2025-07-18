#
# Conditional build:
%bcond_without	ocaml		# OCaml binding
%bcond_without	ocaml_opt	# native optimized binaries
#
%ifnarch %{ix86} %{x8664} %{arm} aarch64 ppc sparc sparcv9
%undefine	with_ocaml_opt
%endif

%define		ocaml_ver	1:3.09.3
Summary:	gdome2 binding for various programming languages
Summary(pl.UTF-8):	Wiązania gdome2 dla różnych języków programowania
Name:		gmetadom
Version:	0.2.6
Release:	16
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://downloads.sourceforge.net/gmetadom/%{name}-%{version}.tar.gz
# Source0-md5:	7bfb5d9c6f20ffa5e790b63d1f8cb481
Patch0:		%{name}-gcc43.patch
URL:		http://gmetadom.sourceforge.net/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	gdome2-devel >= 0.8.0
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.5
%{?with_ocaml:BuildRequires:	ocaml >= %{ocaml_ver}}
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.198
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gdome2 binding for various programming languages. gdome2 is a fast,
light and complete DOM level2 implementation based on libxml2.

%description -l pl.UTF-8
Wiązania gdome2 dla różnych języków programowania. gdome2 jest szybką,
lekką i kompletną implementacją DOM poziom 2 opartą o libxml2.

%package -n ocaml-gdome2
Summary:	gdome2 binding for OCaml
Summary(pl.UTF-8):	Wiązania gdome2 dla OCamla
Group:		Libraries
Requires:	gdome2 >= 0.8.0
%requires_eq	ocaml-runtime

%description -n ocaml-gdome2
gdome2 binding for OCaml. gdome2 is a fast, light and complete DOM
level2 implementation based on libxml2.

This package contains files needed to run bytecode executables using
this library.

%description -n ocaml-gdome2 -l pl.UTF-8
Wiązania gdome2 dla OCamla. gdome2 jest szybką, lekką i kompletną
implementacją DOM poziom 2 opartą o libxml2.

Pakiet ten zawiera binaria potrzebne do uruchamiania programów
używających tej biblioteki.

%package -n ocaml-gdome2-devel
Summary:	gdome2 binding for OCaml - development part
Summary(pl.UTF-8):	Wiązania gdome2 dla OCamla - cześć programistyczna
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	ocaml-gdome2 = %{version}-%{release}
%requires_eq	ocaml

%description -n ocaml-gdome2-devel
gdome2 binding for OCaml. gdome2 is a fast, light and complete DOM
level2 implementation based on libxml2.

This package contains files needed to develop OCaml programs using
this library.

%description -n ocaml-gdome2-devel -l pl.UTF-8
Wiązania gdome2 dla OCamla. gdome2 jest szybką, lekką i kompletną
implementacją DOM poziom 2 opartą o libxml2.

Pakiet ten zawiera pliki niezbędne do tworzenia programów używających
tej biblioteki.

%package -n gdome2-cpp_smart
Summary:	gdome2 binding for C++/smart pointers
Summary(pl.UTF-8):	Wiązania gdome2 dla C++/mądre wskaźniki
Group:		Libraries
Requires:	gdome2 >= 0.8.0

%description -n gdome2-cpp_smart
gdome2 binding for C++ with smart pointers. gdome2 is a fast, light
and complete DOM level2 implementation based on libxml2.

%description -n gdome2-cpp_smart -l pl.UTF-8
Wiązania gdome2 dla C++ z mądrymi wskaźnikami. gdome2 jest szybką,
lekką i kompletną implementacją DOM poziom 2 opartą o libxml2.

%package -n gdome2-cpp_smart-devel
Summary:	gdome2 binding for C++/smart pointers - development part
Summary(pl.UTF-8):	Wiązania gdome2 dla C++/mądre wskaźniki - cześć programistyczna
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gdome2-cpp_smart = %{version}-%{release}
Requires:	gdome2-devel >= 0.8.0
Requires:	libstdc++-devel

%description -n gdome2-cpp_smart-devel
gdome2 binding for C++ with smart pointers. gdome2 is a fast, light
and complete DOM level2 implementation based on libxml2.

This package contains header files needed to develop programs using
gdome2-cpp_smart.

%description -n gdome2-cpp_smart-devel -l pl.UTF-8
Wiązania gdome2 dla C++ z mądrymi wskaźnikami. gdome2 jest szybką,
lekką i kompletną implementacją DOM poziom 2 opartą o libxml2.

Pakiet ten zawiera pliki nagłówkowe niezbędne do rozwijania programów
korzystających z gdome2-cpp_smart.

%package -n gdome2-cpp_smart-static
Summary:	gdome2 binding for C++/smart pointers - static libraries
Summary(pl.UTF-8):	Wiązania gdome2 dla C++/mądre wskaźniki - biblioteki statyczne
Group:		Development/Libraries
Requires:	gdome2-cpp_smart-devel = %{version}-%{release}

%description -n gdome2-cpp_smart-static
gdome2 binding for C++ with smart pointers. gdome2 is a fast, light
and complete DOM level2 implementation based on libxml2.

This package contains static libraries needed to develop programs
using gdome2-cpp_smart.

%description -n gdome2-cpp_smart-static -l pl.UTF-8
Wiązania gdome2 dla C++ z mądrymi wskaźnikami. gdome2 jest szybką,
lekką i kompletną implementacją DOM poziom 2 opartą o libxml2.

Pakiet ten zawiera statyczne biblioteki niezbędne do rozwijania
programów korzystających z gdome2-cpp_smart.

%prep
%setup -q
%patch -P0 -p1

# clean up CVS dirs in xml tree
find -name CVS | xargs rm -rf

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}

%configure \
	--with-modules="gdome_cpp_smart%{?with_ocaml: gdome_caml}"

%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/ocaml-gdome2-%{version}
install src/gdome_caml/examples/*.ml $RPM_BUILD_ROOT%{_examplesdir}/ocaml-gdome2-%{version}

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libgmetadom_gdome_cpp_smart.la

%if %{with ocaml}
# .mli packaged as %doc
%{__rm} $RPM_BUILD_ROOT%{_libdir}/ocaml/gdome2/*.{ml,mli}
# findlib-specific file, useless with rpm
%{__rm} $RPM_BUILD_ROOT%{_libdir}/ocaml/stublibs/dllmlgdome.so.owner
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post	-n gdome2-cpp_smart -p /sbin/ldconfig
%postun	-n gdome2-cpp_smart -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc xml/DOM/* AUTHORS ChangeLog HISTORY LICENSE
%dir %{_includedir}/gmetadom

%if %{with ocaml}
%files -n ocaml-gdome2
%defattr(644,root,root,755)
%dir %{_libdir}/ocaml/gdome2
%attr(755,root,root) %{_libdir}/ocaml/stublibs/dllmlgdome.so

%files -n ocaml-gdome2-devel
%defattr(644,root,root,755)
%doc src/gdome_caml/ocaml/gdome.mli
%{_libdir}/ocaml/gdome2/META
%{_libdir}/ocaml/gdome2/*.cmi
%{_libdir}/ocaml/gdome2/gdomeInit.cmo
%{_libdir}/ocaml/gdome2/mlgdomevalue.h
%{_libdir}/ocaml/gdome2/mlgdome.cma
%{_libdir}/ocaml/gdome2/mlogdome.cma
%if %{with ocaml_opt}
%{_libdir}/ocaml/gdome2/gdomeInit.cmx
%{_libdir}/ocaml/gdome2/gdomeInit.o
%{_libdir}/ocaml/gdome2/mlgdome.a
%{_libdir}/ocaml/gdome2/mlgdome.cmxa
%{_libdir}/ocaml/gdome2/mlogdome.a
%{_libdir}/ocaml/gdome2/mlogdome.cmxa
%endif
%{_libdir}/ocaml/gdome2/libmlgdome.a
%{_examplesdir}/ocaml-gdome2-%{version}
%endif

%files -n gdome2-cpp_smart
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgmetadom_gdome_cpp_smart.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgmetadom_gdome_cpp_smart.so.0

%files -n gdome2-cpp_smart-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgmetadom_gdome_cpp_smart.so
%{_includedir}/gmetadom
%{_pkgconfigdir}/gdome2-cpp-smart.pc

%files -n gdome2-cpp_smart-static
%defattr(644,root,root,755)
%{_libdir}/libgmetadom_gdome_cpp_smart.a
