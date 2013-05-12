Summary:	Cross-platform screen recording tool
Summary(pl.UTF-8):	Wieloplatformowe narzędzie do nagrywania ekranu
Name:		vnc2flv
Version:	20100207
Release:	1
License:	GPL v2+
Group:		Applications/Multimedia
Source0:	https://pypi.python.org/packages/source/v/vnc2flv/%{name}-%{version}.tar.gz
# Source0-md5:	8492e46496e187b49fe5569b5639804e
URL:		http://www.unixuser.org/~euske/python/vnc2flv/index.html
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
# for recordwin.sh
Requires:	alsa-utils
Requires:	awk
Requires:	lame
Requires:	x11vnc
Requires:	xorg-app-xwininfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pyvnc2swf is a cross-platform screen recording tool. It captures
screen motion through VNC protocol and generates a Shockwave Flash
(SWF) movie.

%description -l pl.UTF-8
Pyvnc2swf to wieloplatformowe narzędzie do nagrywania ekranu.
Przechwytuje ruch na ekranie poprzez protokół VNC i generuje film w
formacie Shockwave Flash (SWF).

%prep
%setup -q

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py install \
	--skip-build \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/index.html
%attr(755,root,root) %{_bindir}/flvaddmp3.py
%attr(755,root,root) %{_bindir}/flvcat.py
%attr(755,root,root) %{_bindir}/flvdump.py
%attr(755,root,root) %{_bindir}/flvrec.py
%attr(755,root,root) %{_bindir}/flvsplit.py
%attr(755,root,root) %{_bindir}/recordwin.sh
%attr(755,root,root) %{py_sitedir}/flvscreen.so
%{py_sitedir}/vnc2flv
%{py_sitedir}/vnc2flv-%{version}-py*.egg-info
