Summary:	GNOME Display Manager
Summary(es):	Administrador de Entrada del GNOME
Summary(pl):	gdm
Summary(pt_BR):	Gerenciador de Entrada do GNOME
Name:		gdm
Version:	2.2.5.4
Release:	7
Epoch:		1
License:	LGPL/GPL
Group:		X11/Applications
Source0:	ftp://ftp.gnome.org/pub/GNOME/stable/sources/%{name}/%{name}-%{version}.tar.bz2
Source1:	%{name}.pamd
Source2:	%{name}.init
Source3:	%{name}.conf
Source4:	%{name}-pld-logo.png
Patch0:		%{name}-xdmcp.patch
Patch1:		%{name}-am_fixes.patch
Patch2:		%{name}-permissions.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	esound-devel
BuildRequires:	gdk-pixbuf-devel
BuildRequires:	gettext-devel
BuildRequires:	gnome-libs-devel
BuildRequires:	gtk+-devel
BuildRequires:	libglade-devel
BuildRequires:	libtool
BuildRequires:	libxml-devel
BuildRequires:	perl-modules
BuildRequires:	scrollkeeper
BuildRequires:	intltool >= 0.14
Requires:	gnome-libs >= 1.0.0
Requires:	which
Requires:	/usr/X11R6/bin/sessreg
PreReq:		scrollkeeper
PreReq:		shadow
PreReq:		/sbin/chkconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	xdm kdm wdm

%define		_prefix		/usr/X11R6
%define		_bindir		%{_prefix}/bin
%define		_datadir	%{_prefix}/share
%define		_sbindir	%{_prefix}/sbin
%define		_mandir		%{_prefix}/man
%define		_localstatedir	/var/lib
%define		_sysconfdir	/etc/X11
%define		_omf_dest_dir	%(scrollkeeper-config --omfdir)

%description
Gdm (the GNOME Display Manager) is a highly configurable
reimplementation of xdm, the X Display Manager. Gdm allows you to log
into your system with the X Window System running and supports running
several different X sessions on your local machine at the same time.

%description -l es
Administrador de Entrada del GNOME.

%description -l pl
Gdm jest wysokokonfigurowaln± reimplementacj± xdma. Gdm pozwala
logowaæ siê do systemu z poziomu X11 i wspiera jednoczesn± pracê kilku
ró¿nych Xsesji na lokalnej maszynie.

%description -l pt_BR
Gerenciador de Entrada do GNOME.

%package Xnest
Summary:	Xnest (ie embedded X) server for GDM
Summary(pl):	Serwer Xnest dla GDM
Group:		X11/Applications
Requires:	%{name} = %{version}
Requires:	XFree86-Xnest

%description Xnest
This package add support for Xnest server in gdm.

%description Xnest -l pl
Ten pakiet dodaje do gdm wsparcie dla Xnest.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
rm -f missing
libtoolize --copy --force
gettextize --copy --force
aclocal -I %{_aclocaldir}/gnome
%{__autoconf}
%{__automake}
%configure \
	--with-xinerama=yes \
	--with-xdmcp=yes \
	--with-tcp-wrappers=yes \
	--disable-console-helper

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/{rc.d/init.d,pam.d,security}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	Settingsdir=%{_applnkdir}/Settings/GNOME \
	Systemdir=%{_applnkdir}/System \
	omf_dest_dir=%{_omf_dest_dir}/%{name}

install %{SOURCE1} $RPM_BUILD_ROOT/etc/pam.d/gdm
install %{SOURCE2} $RPM_BUILD_ROOT/etc/rc.d/init.d/gdm
install %{SOURCE3} $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/gdm.conf
install %{SOURCE4} $RPM_BUILD_ROOT/usr/X11R6/share/pixmaps
touch $RPM_BUILD_ROOT/etc/security/blacklist.gdm

mv $RPM_BUILD_ROOT%{_applnkdir}/System/gdmconfig.desktop \
	$RPM_BUILD_ROOT%{_applnkdir}/Settings/GNOME/

gzip -9nf AUTHORS ChangeLog NEWS README TODO

%find_lang %{name} --all-name --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%pre
/usr/sbin/groupadd -g 55 -r -f xdm

if [ -z "`id -u xdm 2>/dev/null`" ]; then
	/usr/sbin/useradd -u 55 -r -d /dev/null -s /bin/false -c 'X Display Manager' -g xdm xdm 1>&2
fi

%post
/sbin/chkconfig --add gdm
if [ -f /var/lock/subsys/gdm ]; then
	echo "Run \"/etc/rc.d/init.d/gdm restart\" to restart gdm." >&2
else
	echo "Run \"/etc/rc.d/init.d/gdm start\" to start gdm." >&2
fi
/usr/bin/scrollkeeper-update

%preun
if [ "$1" = "0" ]; then
	if [ -f /var/lock/subsys/gdm ]; then
		/etc/rc.d/init.d/gdm stop >&2
	fi
	/sbin/chkconfig --del gdm
fi

%postun
if [ "$1" = "0" ]; then
	if [ -n "`id -u xdm 2>/dev/null`" ]; then
		/usr/sbin/userdel xdm
	fi
	/usr/sbin/groupdel xdm
fi
/usr/bin/scrollkeeper-update

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/gdm
%attr(755,root,root) %{_bindir}/gdmchooser
%attr(755,root,root) %{_bindir}/gdmconfig
%attr(755,root,root) %{_bindir}/gdmflexiserver
%attr(755,root,root) %{_bindir}/gdmlogin
%attr(755,root,root) %{_bindir}/gdmmktemp
%attr(755,root,root) %{_bindir}/gdmphotosetup
%attr(755,root,root) %{_sbindir}/*
%attr(755,root,root) %config %{_sysconfdir}/gdm/Init
%attr(755,root,root) %config %{_sysconfdir}/gdm/PreSession
%attr(755,root,root) %config %{_sysconfdir}/gdm/Sessions
%attr(755,root,root) %config %{_sysconfdir}/gdm/PostSession
%attr(755,root,root) %config %{_sysconfdir}/gdm/gnomerc
%attr(755,root,root) %config %{_sysconfdir}/gdm/XKeepsCrashing
%config %{_sysconfdir}/gdm/factory-gdm.conf
%config %{_sysconfdir}/gdm/gdm.conf
%config %{_sysconfdir}/gdm/locale.alias
%attr(755,root,root) %dir %{_sysconfdir}/gdm
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) /etc/pam.d/gdm
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) /etc/security/blacklist.gdm
%attr(770,root,xdm) /var/lib/gdm
%attr(754,root,root) /etc/rc.d/init.d/gdm
%{_pixmapsdir}/*
# these lines to devel subpackage?
%{_applnkdir}/Settings/GNOME/*
%{_applnkdir}/System/gdmflexiserver.desktop
%{_datadir}/gdm
%{_omf_dest_dir}/%{name}

%files Xnest
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gdmXnestchooser
%{_applnkdir}/System/gdmflexiserver-xnest.desktop
