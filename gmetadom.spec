#
# TODO:
# - build with ocaml 
Summary:	gdome2 binding for various programming languages
Summary(pl):	Wi�zania gdome2 dla r�nych j�zyk�w programowania
Name:		gmetadom
Version:	0.1.8
Release:	1
License:	LGPL
Group:		Libraries
# Source0-md5:	2799db817f67c872af14ae9497aa202f
Source0:	http://telia.dl.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.tar.gz
Patch0:		%{name}-assert.patch
URL:		http://sourceforge.net/projects/%{name}/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gdome2-devel
BuildRequires:	gettext-devel
BuildRequires:	libtool
BuildRequires:	libstdc++-devel
#BuildRequires:	ocaml >= 3.04-7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gdome2 binding for various programming languages. gdome2 is a fast,
light and complete DOM level2 implementation based on libxml2.

%description -l pl
Wi�zania gdome2 dla r�nych j�zyk�w programowania. gdome2 jest szybk�,
lekk� i kompletn� implementacj� DOM poziom 2 opart� o libxml2.

%package -n ocaml-gdome2
Summary:	gdome2 binding for OCaml
Summary(pl):	Wi�zania gdome2 dla OCamla
Group:		Libraries
%requires_eq	ocaml-runtime

%description -n ocaml-gdome2
gdome2 binding for OCaml. gdome2 is a fast, light and complete DOM
level2 implementation based on libxml2.

This package contains files needed to run bytecode executables using
this library.

%description -n ocaml-gdome2 -l pl
Wi�zania gdome2 dla OCamla. gdome2 jest szybk�, lekk� i kompletn�
implementacj� DOM poziom 2 opart� o libxml2.

Pakiet ten zawiera binaria potrzebne do uruchamiania program�w
u�ywaj�cych tej biblioteki.

%package -n ocaml-gdome2-devel
Summary:	gdome2 binding for OCaml - development part
Summary(pl):	Wi�zania gdome2 dla OCamla - cze�� programistyczna
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	ocaml-gdome2 = %{version}-%{release}
%requires_eq	ocaml

%description -n ocaml-gdome2-devel
gdome2 binding for OCaml. gdome2 is a fast, light and complete DOM
level2 implementation based on libxml2.

This package contains files needed to develop OCaml programs using
this library.

%description -n ocaml-gdome2-devel -l pl
Wi�zania gdome2 dla OCamla. gdome2 jest szybk�, lekk� i kompletn�
implementacj� DOM poziom 2 opart� o libxml2.

Pakiet ten zawiera pliki niezb�dne do tworzenia program�w u�ywaj�cych
tej biblioteki.

%package -n gdome2-cpp_smart
Summary:	gdome2 binding for C++/smart pointers
Summary(pl):	Wi�zania gdome2 dla C++/m�dre wska�niki
Group:		Libraries

%description -n gdome2-cpp_smart
gdome2 binding for C++ with smart pointers. gdome2 is a fast, light
and complete DOM level2 implementation based on libxml2.

%description -n gdome2-cpp_smart -l pl
Wi�zania gdome2 dla C++ z m�drymi wska�nikami. gdome2 jest szybk�,
lekk� i kompletn� implementacj� DOM poziom 2 opart� o libxml2.

%package -n gdome2-cpp_smart-devel
Summary:	gdome2 binding for C++/smart pointers - development part
Summary(pl):	Wi�zania gdome2 dla C++/m�dre wska�niki - cze�� programistyczna
Group:		Development/Libraries
Requires:	libstdc++-devel
Requires:	%{name} = %{version}-%{release}
Requires:	gdome2-cpp_smart = %{version}-%{release}

%description -n gdome2-cpp_smart-devel
gdome2 binding for C++ with smart pointers. gdome2 is a fast, light
and complete DOM level2 implementation based on libxml2.

This package contains header files needed to develop programs using
gdome2-cpp_smart.

%description -n gdome2-cpp_smart-devel -l pl
Wi�zania gdome2 dla C++ z m�drymi wska�nikami. gdome2 jest szybk�,
lekk� i kompletn� implementacj� DOM poziom 2 opart� o libxml2.

Pakiet ten zawiera pliki nag��wkowe niezb�dne do rozwijania program�w
korzystaj�cych z gdome2-cpp_smart.

%package -n gdome2-cpp_smart-static
Summary:	gdome2 binding for C++/smart pointers - static libraries
Summary(pl):	Wi�zania gdome2 dla C++/m�dre wska�niki - biblioteki statyczne
Group:		Development/Libraries
Requires:	gdome2-cpp_smart-devel = %{version}-%{release}

%description -n gdome2-cpp_smart-static
gdome2 binding for C++ with smart pointers. gdome2 is a fast, light
and complete DOM level2 implementation based on libxml2.

This package contains static libraries needed to develop programs
using gdome2-cpp_smart.

%description -n gdome2-cpp_smart-static -l pl
Wi�zania gdome2 dla C++ z m�drymi wska�nikami. gdome2 jest szybk�,
lekk� i kompletn� implementacj� DOM poziom 2 opart� o libxml2.

Pakiet ten zawiera statyczne bibilioteki niezb�dne do rozwijania
program�w korzystaj�cych z gdome2-cpp_smart.

%prep
%setup -q
%patch0 -p1
find -name CVS | xargs rm -rf

%build
rm -f missing
glib-gettextize --copy --force
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}

%configure \
	--with-modules=gdome_cpp_smart

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc xml/DOM/* AUTHORS ChangeLog HISTORY LICENSE
%dir %{_includedir}/gmetadom

#%files -n ocaml-gdome2
#%defattr(644,root,root,755)
#%dir %{_libdir}/ocaml/gdome2
#%attr(755,root,root) %{_libdir}/ocaml/gdome2/libmlgdome.so*
#%{_libdir}/ocaml/libmlgdome.so

#%files -n ocaml-gdome2-devel
#%defattr(644,root,root,755)
#%doc src/gdome_caml/ocaml/gdome.mli
#%{_libdir}/ocaml/gdome2/*.cm[ixa]*
#%{_libdir}/ocaml/gdome2/*.a
#%{_examplesdir}/ocaml-gdome2-%{version}
#%{_libdir}/ocaml/site-lib/gdome2
#%{_includedir}/caml/*

%files -n gdome2-cpp_smart
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgmetadom_gdome_cpp_smart.so.*.*

%files -n gdome2-cpp_smart-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgmetadom_gdome_cpp_smart.so
%{_libdir}/libgmetadom_gdome_cpp_smart.la
%{_includedir}/gmetadom
%{_pkgconfigdir}/gdome2-cpp-smart.pc

%files -n gdome2-cpp_smart-static
%defattr(644,root,root,755)
%{_libdir}/libgmetadom_gdome_cpp_smart.a
