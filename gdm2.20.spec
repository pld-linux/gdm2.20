Summary:	GNOME Display Manager
Name:		gdm
Version:	1.0.0
Release:	3
Source0:	ftp://ftp.socsci.auc.dk/pub/empl/mkp/gdm-%{PACKAGE_VERSION}.tar.gz
Source1:	gdm.initd
Source2:	gdm.pamd
Patch0:		gdm-gnomerc.patch
Patch1:		gdm-groupwrite.patch
Patch2:		gdm-installdirs.patch
Patch3:		gdm-nocompletion.patch
Patch4:		gdm-rhconf.patch
Group:		X11/Utilities
Copyright:	LGPL/GPL
BuildRoot:	/tmp/%{name}-%{version}-root
Requires:	gnome-libs >= 1.0.0

%define		_prefix	/usr/X11R6
%define		_mandir %{_prefix}/man

%description 
gdm manages local and remote displays and provides the user with a
graphical login window.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
autoheader
automake
autoconf
CFLAGS="$RPM_OPT_FLAGS" \
./configure %{_target_platform} \
	--prefix=%{_prefix} \
	--sysconfdir=/etc/X11 \
	--localstatedir=/var/state
make

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_prefix},/etc/{pam.d,security,rc.d/init.d}}

make install prefix=$RPM_BUILD_ROOT%{_prefix} \
	sysconfdir=$RPM_BUILD_ROOT/etc/X11 \
	localstatedir=$RPM_BUILD_ROOT/var/state

#sed -e "s#$RPM_BUILD_ROOT##g" config/gdm.conf >config/gdm.conf.X
sed -e "s#User=gdm#User=root#g" -e "s#Group=gdm#Group=root#g" \
	config/gdm.conf >$RPM_BUILD_ROOT/etc/X11/gdm/gdm.conf

install %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/gdm
install %{SOURCE2} $RPM_BUILD_ROOT/etc/pam.d/gdm
touch $RPM_BUILD_ROOT/etc/security/blacklist.gdm

strip $RPM_BUILD_ROOT%{_bindir}/* || :

gzip -9nf AUTHORS ChangeLog NEWS README TODO docs/gdm-manual.txt

%find_lang gdm

%clean
rm -rf $RPM_BUILD_ROOT

%files -f gdm.lang
%defattr(644,root,root,755)
%doc {AUTHORS,ChangeLog,NEWS,README,TODO,docs/gdm-manual.txt}.gz
%attr(755,root,root) %{_bindir}/gdm
%attr(755,root,root) %{_bindir}/gdmgreeter
%attr(755,root,root) %{_bindir}/gdmchooser
%attr(755,root,root) %config /etc/X11/gdm/Init/*
%attr(755,root,root) %config /etc/X11/gdm/Sessions/*
%config /etc/X11/gdm/gnomerc
%config /etc/X11/gdm/gdm.conf
%attr(640,root,root) %config %verify(not size mtime md5) /etc/pam.d/gdm
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) /etc/security/blacklist.gdm
%attr(754,root,root) /etc/rc.d/init.d/gdm
%attr(750,root,root) /var/state/gdm
%{_datadir}/pixmaps/*
