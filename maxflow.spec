Summary:	Library implementing the max-flow/min-cut algorithm
Summary(pl.UTF-8):	Biblioteka implementująca algorytm maksymalnego przepływu i minimalnego cięcia
Name:		maxflow
Version:	3.0.5
Release:	1
License:	GPL v3+
Group:		Libraries
Source0:	https://github.com/gerddie/maxflow/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	4354e9a5cb02a97d424c89f07683f30e
URL:		https://github.com/gerddie/maxflow
BuildRequires:	cmake >= 2.8.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Library implementing the max-flow/min-cut algorithm.

%description -l pl.UTF-8
Biblioteka implementująca algorytm maksymalnego przepływu i
minimalnego cięcia.

%package devel
Summary:	Header files for maxflow library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki maxflow
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for maxflow library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki maxflow.

%prep
%setup -q

%build
install -d build
cd build
%cmake .. \
	-DCMAKE_INSTALL_INCLUDEDIR=include \
	-DCMAKE_INSTALL_LIBDIR=%{_lib}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGES.TXT README.md
%attr(755,root,root) %{_libdir}/libmaxflow.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libmaxflow.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmaxflow.so
%{_includedir}/maxflow-3.0
%{_pkgconfigdir}/maxflow.pc
