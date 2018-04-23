#
# TODO:
# - s=/dev/null=/home/services/xdm= in %%trigger for graceful upgrade from xdm/kdm/gdm 2.2
# - check /etc/pam.d/gdm-autologin
#
# Conditiional build:
%bcond_without	selinux	# without selinux

Summary:	GNOME Display Manager
Summary(es.UTF-8):	Administrador de Entrada del GNOME
Summary(ja.UTF-8):	GNOME ディスプレイマネージャ
Summary(pl.UTF-8):	gdm - zarządca ekranów GNOME
Summary(pt_BR.UTF-8):	Gerenciador de Entrada do GNOME
Summary(ru.UTF-8):	Дисплейный менеджер GNOME
Summary(uk.UTF-8):	Дисплейний менеджер GNOME
Name:		gdm2.20
Version:	2.20.11
Release:	12
License:	GPL v2+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gdm/2.20/gdm-%{version}.tar.bz2
# Source0-md5:	67696b64c81c317f61065810a32e8b36
Source1:	gdm.pamd
Source2:	gdm.init
Source3:	gdm-pld-logo.png
# http://cvs.pld-linux.org/cgi-bin/cvsweb/pld-artwork/gdm/storky/
Source4:	gdm-storky.tar.gz
# Source4-md5:	e293fbe4a60004056f6894463b874ae8
Source5:	gdm-autologin.pamd
Patch0:		gdm-xdmcp.patch
Patch1:		gdm-conf.patch
Patch2:		gdm-xsession.patch
Patch3:		gdm-desktop.patch
Patch4:		gdm-defaults.patch
Patch5:		xinit-sh.patch
Patch6:		missing-prototypes.patch
Patch7:		gdm-format.patch
Patch8:		gdm-includes.patch
URL:		http://www.gnome.org/projects/gdm/
BuildRequires:	ConsoleKit-devel
BuildRequires:	attr-devel
BuildRequires:	audit-libs-devel
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	dbus-glib-devel >= 0.73
BuildRequires:	docbook-dtd412-xml
BuildRequires:	gettext-tools
BuildRequires:	gnome-common
BuildRequires:	gnome-doc-utils
BuildRequires:	gtk+2-devel >= 2:2.12.0
BuildRequires:	intltool >= 0.36.1
BuildRequires:	libart_lgpl-devel >= 2.3.19
BuildRequires:	libglade2-devel >= 1:2.6.2
BuildRequires:	libgnomeui-devel >= 2.20.0
BuildRequires:	libgsf-devel >= 1.14.6
BuildRequires:	librsvg-devel >= 1:2.18.1
%{?with_selinux:BuildRequires:	libselinux-devel}
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 1:2.6.29
BuildRequires:	pam-devel
BuildRequires:	perl-modules
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.627
BuildRequires:	scrollkeeper
BuildRequires:	sed >= 4.0
BuildRequires:	xorg-lib-libXdmcp-devel
BuildRequires:	xorg-lib-libXi-devel
BuildRequires:	xorg-lib-libXinerama-devel
BuildRequires:	xorg-lib-libdmx-devel
Requires(post,postun):	/usr/bin/scrollkeeper-update
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
Requires(postun):	/usr/sbin/groupdel
Requires(postun):	/usr/sbin/userdel
Requires(pre):	/bin/id
Requires(pre):	/usr/sbin/groupadd
Requires(pre):	/usr/sbin/useradd
Requires(post,preun,postun):	systemd-units >= 38
Requires:	libgnomeui >= 2.20.0
Requires:	pam >= 0.99.7.1
Requires:	systemd-units >= 38
Requires:	which
Requires:	xinitrc-ng >= 1.0
Requires:	xorg-app-sessreg
Requires:	xorg-app-xmodmap
Suggests:	zenity
Provides:	XDM
Provides:	gdm = 2:%{version}
Provides:	group(xdm)
Provides:	user(xdm)
Obsoletes:	gdm <= 2:%{version}
Conflicts:	gdkxft
Conflicts:	gdm > 2:%{version}
# sr@Latn vs. sr@latin
Conflicts:	glibc-misc < 6:2.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_localstatedir	/var/lib

%description
Gdm (the GNOME Display Manager) is a highly configurable
reimplementation of xdm, the X Display Manager. Gdm allows you to log
into your system with the X Window System running and supports running
several different X sessions on your local machine at the same time.

%description -l es.UTF-8
Administrador de Entrada del GNOME.

%description -l ja.UTF-8
Gdm (the GNOME Display Manager) は、高度に設定可能な xdm X Display
Manager の再実装版です。 Gdm を使うと、 X Window System
が動いているあなたの
システムにいろいろなセッションを選択してログインすることができます。

このバージョンの Gdm では、各種言語や、XIM を選択することも可能です。

%description -l pl.UTF-8
Gdm jest wysokokonfigurowalną reimplementacją xdma. Gdm pozwala
logować się do systemu z poziomu X11 i wspiera jednoczesną pracę kilku
różnych sesji X na lokalnej maszynie.

%description -l pt_BR.UTF-8
Gerenciador de Entrada do GNOME.

%description -l ru.UTF-8
GDM (GNOME Display Manager) - это реимплементация xdm (X Display
Manager). GDM позволяет вам входить в систему, на которой запущено X
Window и поддерживает работу нескольуих разных X сеансов одновременно.

%description -l uk.UTF-8
GDM (GNOME Display Manager) - це реімплементація xdm (X Display
Manager). GDM дозволяє вам входити в систему, на якій запущено X
Window та підтримує роботу кількох різних X сеансів одночасно.

%package faces
Summary:	Faces icons for GDM
Summary(pl.UTF-8):	Ikony twarzy dla GDM
Group:		X11/Applications
Conflicts:	gnome-control-center >= 3

%description faces
Faces icons for GDM.

%description faces -l pl.UTF-8
Ikony twarzy dla GDM.

%package Xnest
Summary:	Xnest (ie embedded X) server for GDM
Summary(pl.UTF-8):	Serwer Xnest dla GDM
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	xorg-xserver-Xnest
Obsoletes:	gdm-Xnest <= 2:%{version}

%description Xnest
This package add support for Xnest server in gdm.

%description Xnest -l pl.UTF-8
Ten pakiet dodaje do gdm wsparcie dla Xnest.

%package init
Summary:	Init script for GDM
Summary(pl.UTF-8):	Skrypt init dla GDM-a
Group:		X11/Applications
Requires(post,preun):	/sbin/chkconfig
Requires:	%{name} = %{version}-%{release}
Requires:	open
Obsoletes:	gdm-init <= 2:%{version}
Conflicts:	gdm-init > 2:%{version}

%description init
Init script for GDM.

%description init -l pl.UTF-8
Skrypt init dla GDM-a.

%prep
%setup -q -a4 -n gdm-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1

%{__sed} -i -e 's#sr@Latn#sr@latin#' po/LINGUAS
%{__mv} po/sr@{Latn,latin}.po

%build
%{__libtoolize}
%{__glib_gettextize}
%{__intltoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	LIBS="-lXau" \
	ZENITY=/usr/bin/zenity \
	--disable-console-helper \
	--disable-scrollkeeper \
	--enable-authentication-scheme=pam \
	--enable-secureremote \
	--with-console-kit \
	--with-pam-prefix=/etc \
	--with-tcp-wrappers \
	--with-selinux%{!?with_selinux:=no} \
	--with-libaudit \
	--with-xdmcp \
	--with-xinerama \
	--with-dmx \
	--enable-ipv6

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/{rc.d/init.d,pam.d,security} \
	$RPM_BUILD_ROOT{/home/services/xdm,/var/log/gdm} \
	$RPM_BUILD_ROOT%{_datadir}/gdm/themes/storky \
	$RPM_BUILD_ROOT%{systemdunitdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	PAM_PREFIX=/etc

%{__mv} $RPM_BUILD_ROOT%{_datadir}/gdm/BuiltInSessions/default.desktop \
	$RPM_BUILD_ROOT%{_datadir}/xsessions

cp -p %{SOURCE1} $RPM_BUILD_ROOT/etc/pam.d/gdm
cp -p %{SOURCE5} $RPM_BUILD_ROOT/etc/pam.d/gdm-autologin
install %{SOURCE2} $RPM_BUILD_ROOT/etc/rc.d/init.d/gdm

cp -p %{SOURCE3} $RPM_BUILD_ROOT%{_pixmapsdir}

ln -sf /dev/null $RPM_BUILD_ROOT%{systemdunitdir}/gdm.service

cp -p storky/*.* $RPM_BUILD_ROOT%{_datadir}/gdm/themes/storky/

touch $RPM_BUILD_ROOT/etc/security/blacklist.gdm

%find_lang gdm --with-gnome --with-omf --all-name

# Remove useless files
%{__rm} $RPM_BUILD_ROOT%{_libdir}/gtk-2.0/modules/*.{la,a}

# moved to gnome-session
%{__rm} $RPM_BUILD_ROOT%{_datadir}/xsessions/gnome.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%pre
%groupadd -g 55 -r -f xdm
%useradd -u 55 -r -d /home/services/xdm -s /bin/false -c "X Display Manager" -g xdm xdm

%post
%scrollkeeper_update_post
%update_icon_cache hicolor
%systemd_reload

%postun
%scrollkeeper_update_postun
%update_icon_cache hicolor
%systemd_reload

if [ "$1" = "0" ]; then
	%userremove xdm
	%groupremove xdm
fi

%triggerpostun -- gdm < 1:2.13.0.8-1
if [ -f /etc/X11/gdm/gdm.conf-custom.rpmsave ]; then
    mv /etc/X11/gdm/gdm.conf-custom.rpmsave /etc/gdm/custom.conf
fi

%post init
/sbin/chkconfig --add gdm
if [ -f /var/lock/subsys/gdm ]; then
	echo "Run \"/sbin/service gdm restart\" to restart gdm." >&2
	echo "WARNING: it will terminate all sessions opened from gdm!" >&2
else
	echo "Run \"/sbin/service gdm start\" to start gdm." >&2
fi

%preun init
if [ "$1" = "0" ]; then
	%service gdm stop
	/sbin/chkconfig --del gdm
fi

%files -f gdm.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/gdm-dmx-reconnect-proxy
%attr(755,root,root) %{_bindir}/gdmdynamic
%attr(755,root,root) %{_bindir}/gdmflexiserver
%attr(755,root,root) %{_bindir}/gdmphotosetup
%attr(755,root,root) %{_bindir}/gdmthemetester
%attr(755,root,root) %{_sbindir}/gdm
%attr(755,root,root) %{_sbindir}/gdm-binary
%attr(755,root,root) %{_sbindir}/gdm-restart
%attr(755,root,root) %{_sbindir}/gdm-safe-restart
%attr(755,root,root) %{_sbindir}/gdm-stop
%attr(755,root,root) %{_sbindir}/gdmsetup
%attr(755,root,root) %{_libexecdir}/gdm-ssh-session
%attr(755,root,root) %{_libexecdir}/gdmaskpass
%attr(755,root,root) %{_libexecdir}/gdmopen
%attr(755,root,root) %{_libexecdir}/gdmtranslate
%attr(755,root,root) %{_libexecdir}/gdmchooser
%attr(755,root,root) %{_libexecdir}/gdmgreeter
%attr(755,root,root) %{_libexecdir}/gdmlogin

%{systemdunitdir}/gdm.service
%dir %{_sysconfdir}/gdm
%dir %{_sysconfdir}/gdm/Init
%dir %{_sysconfdir}/gdm/PreSession
%dir %{_sysconfdir}/gdm/PostSession
%dir %{_sysconfdir}/gdm/PostLogin
%dir %{_sysconfdir}/gdm/modules
%attr(755,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/gdm/Init/Default
%attr(755,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/gdm/PostLogin/Default.sample
%attr(755,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/gdm/PostSession/Default
%attr(755,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/gdm/PreSession/Default
%attr(755,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/gdm/XKeepsCrashing
%attr(755,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/gdm/Xsession
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/gdm/custom.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/gdm/locale.alias
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/gdm/modules/*

%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/pam.d/gdm*
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/security/blacklist.gdm
%attr(1770,root,xdm) /var/lib/gdm
%attr(750,xdm,xdm) /var/log/gdm
%attr(750,xdm,xdm) /home/services/xdm
%{_pixmapsdir}/gdm-foot-logo.png
%{_pixmapsdir}/gdm-pld-logo.png
%{_pixmapsdir}/nobody.png
%{_pixmapsdir}/nohost.png
%{_datadir}/gdm
%{_datadir}/xsessions/default.desktop
%{_datadir}/xsessions/ssh.desktop
%{_iconsdir}/hicolor/*x*/apps/gdm*.png
%{_iconsdir}/hicolor/scalable/apps/gdm*.svg
%attr(755,root,root) %{_libdir}/gtk-2.0/modules/libdwellmouselistener.so
%attr(755,root,root) %{_libdir}/gtk-2.0/modules/libkeymouselistener.so
%{_mandir}/man1/gdm.1*

%files faces
%defattr(644,root,root,755)
%{_pixmapsdir}/faces

%files Xnest
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gdmXnest
%attr(755,root,root) %{_bindir}/gdmXnestchooser

%files init
%defattr(644,root,root,755)
%attr(754,root,root) /etc/rc.d/init.d/gdm
