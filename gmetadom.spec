Summary:	gdome2 binding for various programming languages
Summary(pl):	Wi±zania gdome2 dla ró¿nych jêzyków programowania
Name:		gmetadom
Version:	0.0.3
Release:	1
License:	LGPL
Group:		Libraries
URL:		http://sourceforge.net/projects/%{name}/
Source0:	http://telia.dl.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.tar.gz
Patch0:		%{name}-ac-am.patch
BuildRequires:	gdome2-devel
BuildRequires:	ocaml >= 3.04-7
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	gettext-devel
BuildRequires:	libstdc++2-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gdome2 binding for various programming languages. gdome2 is a fast,
light and complete DOM level2 implementation based on libxml2.

%description -l pl
Wi±zania gdome2 dla ró¿nych jêzyków programowania. gdome2 jest szybk±,
lekk± i kompletn± implementacj± DOM poziom 2 opart± o libxml2.

%package -n ocaml-gdome2
Summary:	gdome2 binding for OCaml
Summary(pl):	Wi±zania gdome2 dla OCamla
Group:		Libraries
%requires_eq	ocaml-runtime

%description -n ocaml-gdome2
gdome2 binding for OCaml. gdome2 is a fast, light and complete DOM
level2 implementation based on libxml2.

This package contains files needed to run bytecode executables using
this library.

%description -n ocaml-gdome2 -l pl
Wi±zania gdome2 dla OCamla. gdome2 jest szybk±, lekk± i kompletn±
implementacj± DOM poziom 2 opart± o libxml2.

Pakiet ten zawiera binaria potrzebne do uruchamiania programów
u¿ywaj±cych tej biblioteki.

%package -n ocaml-gdome2-devel
Summary:	gdome2 binding for OCaml - development part
Summary(pl):	Wi±zania gdome2 dla OCamla - cze¶æ programistyczna
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
Wi±zania gdome2 dla OCamla. gdome2 jest szybk±, lekk± i kompletn±
implementacj± DOM poziom 2 opart± o libxml2.

Pakiet ten zawiera pliki niezbêdne do tworzenia programów u¿ywaj±cych
tej biblioteki.

%package -n gdome2-cpp_smart
Summary:	gdome2 binding for C++/smart pointers
Summary(pl):	Wi±zania gdome2 dla C++/m±dre wska¼niki
Group:		Libraries

%description -n gdome2-cpp_smart
gdome2 binding for C++ with smart pointers. gdome2 is a fast, light
and complete DOM level2 implementation based on libxml2.

%description -n gdome2-cpp_smart -l pl
Wi±zania gdome2 dla C++ z m±drymi wska¼nikami. gdome2 jest szybk±,
lekk± i kompletn± implementacj± DOM poziom 2 opart± o libxml2.

%package -n gdome2-cpp_smart-devel
Summary:	gdome2 binding for C++/smart pointers - development part
Summary(pl):	Wi±zania gdome2 dla C++/m±dre wska¼niki - cze¶æ programistyczna
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
Wi±zania gdome2 dla C++ z m±drymi wska¼nikami. gdome2 jest szybk±,
lekk± i kompletn± implementacj± DOM poziom 2 opart± o libxml2.

Pakiet ten zawiera pliki nag³ówkowe niezbêdne do rozwijania programów
korzystaj±cych z gdome2-cpp_smart.

%package -n gdome2-cpp_smart-static
Summary:	gdome2 binding for C++/smart pointers - static libraries
Summary(pl):	Wi±zania gdome2 dla C++/m±dre wska¼niki - biblioteki statyczne
Group:		Development/Libraries
Requires:	gdome2-cpp_smart-devel = %{version}-%{release}

%description -n gdome2-cpp_smart-static
gdome2 binding for C++ with smart pointers. gdome2 is a fast, light
and complete DOM level2 implementation based on libxml2.

This package contains static libraries needed to develop programs
using gdome2-cpp_smart.

%description -n gdome2-cpp_smart-static -l pl
Wi±zania gdome2 dla C++ z m±drymi wska¼nikami. gdome2 jest szybk±,
lekk± i kompletn± implementacj± DOM poziom 2 opart± o libxml2.

Pakiet ten zawiera statyczne bibilioteki niezbêdne do rozwijania
programów korzystaj±cych z gdome2-cpp_smart.

%prep
%setup -q
%patch0 -p1
find -name CVS | xargs rm -rf

%build
rm -f missing
gettextize --copy --force
libtoolize --copy --force
aclocal
%{__autoconf}
%{__automake}

%configure CXX=g++2

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

(cd $RPM_BUILD_ROOT%{_libdir}/ocaml && ln -s gdome2/lib*.so .)

install -d $RPM_BUILD_ROOT%{_examplesdir}/ocaml-gdome2-%{version}
cp src/gdome_caml/examples/* \
	$RPM_BUILD_ROOT%{_examplesdir}/ocaml-gdome2-%{version}

install -d $RPM_BUILD_ROOT%{_libdir}/ocaml/site-lib/gdome2
mv $RPM_BUILD_ROOT%{_libdir}/ocaml/gdome2/META \
	$RPM_BUILD_ROOT%{_libdir}/ocaml/site-lib/gdome2
echo 'directory = "+gdome2"' \
	>> $RPM_BUILD_ROOT%{_libdir}/ocaml/site-lib/gdome2/META

install -d $RPM_BUILD_ROOT%{_includedir}/caml
mv $RPM_BUILD_ROOT%{_libdir}/ocaml/gdome2/*.h \
	$RPM_BUILD_ROOT%{_includedir}/caml

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc xml/DOM/* AUTHORS ChangeLog HISTORY LICENSE
%dir %{_datadir}/gmetadom
%dir %{_includedir}/gmetadom

%files -n ocaml-gdome2
%defattr(644,root,root,755)
%dir %{_libdir}/ocaml/gdome2
%attr(755,root,root) %{_libdir}/ocaml/gdome2/libmlgdome.so*
%{_libdir}/ocaml/libmlgdome.so

%files -n ocaml-gdome2-devel
%defattr(644,root,root,755)
%doc src/gdome_caml/ocaml/gdome.mli
%{_libdir}/ocaml/gdome2/*.cm[ixa]*
%{_libdir}/ocaml/gdome2/*.a
%{_examplesdir}/ocaml-gdome2-%{version}
%{_libdir}/ocaml/site-lib/gdome2
%{_includedir}/caml/*

%files -n gdome2-cpp_smart
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgmetadom_gdome_cpp_smart.so.*

%files -n gdome2-cpp_smart-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gmetadom-config
%attr(755,root,root) %{_libdir}/libgmetadom_gdome_cpp_smart.la
%attr(755,root,root) %{_libdir}/libgmetadom_gdome_cpp_smart.so
%{_includedir}/gmetadom/*
%{_datadir}/gmetadom/gdome_cpp_smart.conf

%files -n gdome2-cpp_smart-static
%defattr(644,root,root,755)
%{_libdir}/libgmetadom_gdome_cpp_smart.a
