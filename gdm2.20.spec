#
# BIG FAT WARNING!
#
#	DO NOT even think of moving this (2.24) to HEAD or sending
#	to builders/ftp. Despite it being newer, it's just a pathetic
#	excuse for a display manager and does not even come close
#	feature-wise to 2.20.
#
# TODO:
# - s=/dev/null=/home/services/xdm= in %%trigger for graceful upgrade from xdm/kdm/gdm 2.2
# - check /etc/pam.d/gdm-autologin
#
# Conditiional build:
%bcond_without	selinux	# without selinux
#
Summary:	GNOME Display Manager
Summary(es.UTF-8):	Administrador de Entrada del GNOME
Summary(ja.UTF-8):	GNOME ディスプレイマネージャ
Summary(pl.UTF-8):	gdm - zarządca ekranów GNOME
Summary(pt_BR.UTF-8):	Gerenciador de Entrada do GNOME
Summary(ru.UTF-8):	Дисплейный менеджер GNOME
Summary(uk.UTF-8):	Дисплейний менеджер GNOME
Name:		gdm
Version:	2.26.1
Release:	1
Epoch:		2
License:	GPL/LGPL
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gdm/2.26/%{name}-%{version}.tar.bz2
# Source0-md5:	c2c15f8b741962f278fa7e790aaa9a2b
Source1:	%{name}.pamd
Source2:	%{name}.init
Source3:	%{name}-pld-logo.png
#Source4:	%{name}-autologin.pamd
Patch0:		%{name}-xdmcp.patch
Patch1:		%{name}-libxklavier40.patch
Patch2:		%{name}-xsession.patch
Patch4:		%{name}-defaults.patch
URL:		http://www.gnome.org/projects/gdm/
BuildRequires:	ConsoleKit-devel
BuildRequires:	GConf2-devel >= 2.24.0
BuildRequires:	PolicyKit-gnome-devel >= 0.8
BuildRequires:	attr-devel
BuildRequires:	audit-libs-devel
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake >= 1:1.9
BuildRequires:	check >= 0.9.4
BuildRequires:	dbus-glib-devel >= 0.74
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.16.0
BuildRequires:	gnome-doc-utils
BuildRequires:	gnome-panel-devel >= 2.24.0
BuildRequires:	gtk+2-devel >= 2:2.14.0
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libglade2-devel >= 1:2.6.2
%{?with_selinux:BuildRequires:	libselinux-devel}
BuildRequires:	libtool
BuildRequires:	libxklavier-devel >= 3.5
BuildRequires:	pam-devel
BuildRequires:	perl-modules
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	scrollkeeper
BuildRequires:	xorg-lib-libXdmcp-devel
BuildRequires:	xorg-lib-libXi-devel
BuildRequires:	xorg-lib-libXinerama-devel
BuildRequires:	xorg-lib-libdmx-devel
Requires(post,postun):	gtk+2
Requires(post,postun):	hicolor-icon-theme
Requires(post,postun):	/usr/bin/scrollkeeper-update
Requires(postun):	/usr/sbin/groupdel
Requires(postun):	/usr/sbin/userdel
Requires(pre):	/bin/id
Requires(pre):	/usr/sbin/groupadd
Requires(pre):	/usr/sbin/useradd
Requires:	/usr/bin/Xorg
Requires:	PolicyKit-gnome >= 0.8
Requires:	gnome-session >= 2.24.0
Requires:	gnome-settings-daemon >= 2.24.0
Requires:	libgnomeui >= 2.24.0
Requires:	pam >= 0.99.7.1
Requires:	which
Requires:	xorg-app-sessreg
Requires:	xorg-app-xmodmap
Provides:	XDM
Provides:	group(xdm)
Provides:	user(xdm)
Obsoletes:	gdm-Xnest
Conflicts:	gdkxft
# sr@Latn vs. sr@latin
Conflicts:	glibc-misc < 6:2.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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

%package init
Summary:	Init script for GDM
Summary(pl.UTF-8):	Skrypt init dla GDM-a
Group:		X11/Applications
Requires(post,preun):	/sbin/chkconfig
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	open

%description init
Init script for GDM.

%description init -l pl.UTF-8
Skrypt init dla GDM-a.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch4 -p1
rm -f data/gdm.schemas.in

%build
%{__libtoolize}
%{__glib_gettextize}
%{__intltoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	--disable-console-helper \
	--disable-scrollkeeper \
	--with-console-kit \
	--enable-authentication-scheme=pam \
	--with-pam-prefix=/etc \
	--with-tcp-wrappers=yes \
	--with%{!?with_selinux:out}-selinux \
	--with-xdmcp=yes \
	--with-xinerama=yes \
	--with-user=xdm \
	--with-group=xdm

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/{rc.d/init.d,pam.d,security} \
	$RPM_BUILD_ROOT{/home/services/xdm,/var/log/gdm} \

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	PAM_PREFIX=/etc

install %{SOURCE1} $RPM_BUILD_ROOT/etc/pam.d/gdm
#install %{SOURCE4} $RPM_BUILD_ROOT/etc/pam.d/gdm-autologin
install %{SOURCE2} $RPM_BUILD_ROOT/etc/rc.d/init.d/gdm

install %{SOURCE3} $RPM_BUILD_ROOT%{_pixmapsdir}

touch $RPM_BUILD_ROOT/etc/security/blacklist.gdm

%find_lang %{name} --with-gnome --with-omf --all-name

# Remove useless files
rm -f $RPM_BUILD_ROOT%{_libdir}/gtk-2.0/modules/*.{la,a}

# moved to gnome-session
rm -f $RPM_BUILD_ROOT%{_datadir}/xsessions/gnome.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%pre
%groupadd -g 55 -r -f xdm
%useradd -u 55 -r -d /home/services/xdm -s /bin/false -c "X Display Manager" -g xdm xdm

%post
%gconf_schema_install gdm-simple-greeter.schemas
%scrollkeeper_update_post
%update_icon_cache hicolor

%preun
%gconf_schema_uninstall gdm-simple-greeter.schemas

%postun
%scrollkeeper_update_postun
%update_icon_cache hicolor

if [ "$1" = "0" ]; then
	%userremove xdm
	%groupremove xdm
fi

%triggerpostun -- %{name} < 1:2.13.0.8-1
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

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_libexecdir}/gdm-crash-logger
%attr(755,root,root) %{_libexecdir}/gdm-factory-slave
%attr(755,root,root) %{_libexecdir}/gdm-host-chooser
%attr(755,root,root) %{_libexecdir}/gdm-product-slave
%attr(755,root,root) %{_libexecdir}/gdm-session-worker
%attr(755,root,root) %{_libexecdir}/gdm-simple-chooser
%attr(755,root,root) %{_libexecdir}/gdm-simple-greeter
%attr(755,root,root) %{_libexecdir}/gdm-simple-slave
%attr(755,root,root) %{_libexecdir}/gdm-user-switch-applet
%attr(755,root,root) %{_libexecdir}/gdm-xdmcp-chooser-slave
%attr(755,root,root) %{_sbindir}/*
%attr(755,root,root) %{_bindir}/*
%dir %{_sysconfdir}/gdm
%dir %{_sysconfdir}/gdm/Init
%attr(755,root,root) %config %{_sysconfdir}/gdm/Init/Default
%attr(755,root,root) %config %{_sysconfdir}/gdm/PreSession
%attr(755,root,root) %config %{_sysconfdir}/gdm/PostSession
%attr(755,root,root) %config %{_sysconfdir}/gdm/Xsession
%dir %{_sysconfdir}/gdm/PostLogin
%config %{_sysconfdir}/gdm/PostLogin/Default.sample
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/gdm/custom.conf
%{_sysconfdir}/gdm/gdm.schemas
%{_sysconfdir}/gconf/schemas/gdm-simple-greeter.schemas
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/dbus-1/system.d/*
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/pam.d/gdm*
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/security/blacklist.gdm
%attr(750,xdm,xdm) %{_localstatedir}/gdm
%attr(750,xdm,xdm) %{_localstatedir}/log/gdm
%attr(750,xdm,xdm) /home/services/xdm
%{_pixmapsdir}/*
%{_datadir}/gdm
%{_iconsdir}/hicolor/*/apps/*.png
%{_datadir}/gnome-2.0/ui/GNOME_FastUserSwitchApplet.xml
%{_libdir}/bonobo/servers/*.server
%{_localstatedir}/lib/gdm

%files init
%defattr(644,root,root,755)
%attr(754,root,root) /etc/rc.d/init.d/gdm
