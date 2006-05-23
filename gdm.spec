# TODO:
# /etc/X11/dm dir should belong to XFree? It is common for KDE and GNOME
# s=/dev/null=/home/services/xdm= in %%trigger for gracefull upgrade from xdm/kdm/gdm 2.2
# check /etc/pam.d/gdm-autologin
#
# Conditiional build:
%bcond_without	selinux	# without selinux
#
Summary:	GNOME Display Manager
Summary(es):	Administrador de Entrada del GNOME
Summary(ja):	GNOME ¥Ç¥£¥¹¥×¥ì¥¤¥Þ¥Í¡¼¥¸¥ã
Summary(pl):	gdm - zarz±dca ekranów GNOME
Summary(pt_BR):	Gerenciador de Entrada do GNOME
Summary(ru):	äÉÓÐÌÅÊÎÙÊ ÍÅÎÅÄÖÅÒ GNOME
Summary(uk):	äÉÓÐÌÅÊÎÉÊ ÍÅÎÅÄÖÅÒ GNOME
Name:		gdm
Version:	2.14.7
Release:	1
Epoch:		1
License:	GPL/LGPL
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gdm/2.14/%{name}-%{version}.tar.bz2
# Source0-md5:	0ad3cb1eefd6fe216a3e2f0f7cd8944f
Source1:	%{name}.pamd
Source2:	%{name}.init
Source3:	%{name}-pld-logo.png
# http://cvs.pld-linux.org/cgi-bin/cvsweb/pld-artwork/gdm/storky/
Source4:	%{name}-storky.tar.gz
# Source4-md5:	e293fbe4a60004056f6894463b874ae8
Source5:	%{name}-autologin.pamd
Patch0:		%{name}-xdmcp.patch
Patch1:		%{name}-conf.patch
Patch2:		%{name}-xsession.patch
Patch3:		%{name}-logdir.patch
Patch4:		%{name}-desktop.patch
URL:		http://www.jirka.org/gdm.html
BuildRequires:	attr-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel >= 2:2.4.3
BuildRequires:	intltool >= 0.30
BuildRequires:	libglade2-devel >= 1:2.4.1
BuildRequires:	libgnome-devel >= 2.14.1
BuildRequires:	libgnomecanvas-devel >= 2.14.0
BuildRequires:	libgnomeui-devel >= 2.14.1
BuildRequires:	libgsf-devel >= 1.9.0
BuildRequires:	librsvg-devel >= 1:2.14.3
%{?with_selinux:BuildRequires:	libselinux-devel}
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 2.5.11
BuildRequires:	pam-devel
BuildRequires:	perl-modules
BuildRequires:	rpmbuild(macros) >= 1.268
Requires(pre):	/bin/id
Requires(pre):	/usr/sbin/groupadd
Requires(pre):	/usr/sbin/useradd
Requires(postun):	/usr/sbin/groupdel
Requires(postun):	/usr/sbin/userdel
Requires(post,postun):	/usr/bin/scrollkeeper-update
Requires:	libgnome >= 2.14.1
Requires:	libgnomecanvas >= 2.14.0
Requires:	libgnomeui >= 2.14.1
Requires:	sessreg
Requires:	which
Requires:	pam >= 0.79.0
Provides:	group(xdm)
Provides:	user(xdm)
Obsoletes:	X11-xdm
Obsoletes:	entrance
Obsoletes:	kdm
Obsoletes:	wdm
Obsoletes:	xdm
Conflicts:	gdkxft
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/X11
%define		_localstatedir	/var/lib

%description
Gdm (the GNOME Display Manager) is a highly configurable
reimplementation of xdm, the X Display Manager. Gdm allows you to log
into your system with the X Window System running and supports running
several different X sessions on your local machine at the same time.

%description -l es
Administrador de Entrada del GNOME.

%description -l ja
Gdm (the GNOME Display Manager) ¤Ï¡¢¹âÅÙ¤ËÀßÄê²ÄÇ½¤Ê xdm X Display
Manager ¤ÎºÆ¼ÂÁõÈÇ¤Ç¤¹¡£ Gdm ¤ò»È¤¦¤È¡¢ X Window System
¤¬Æ°¤¤¤Æ¤¤¤ë¤¢¤Ê¤¿¤Î
¥·¥¹¥Æ¥à¤Ë¤¤¤í¤¤¤í¤Ê¥»¥Ã¥·¥ç¥ó¤òÁªÂò¤·¤Æ¥í¥°¥¤¥ó¤¹¤ë¤³¤È¤¬¤Ç¤­¤Þ¤¹¡£

¤³¤Î¥Ð¡¼¥¸¥ç¥ó¤Î Gdm ¤Ç¤Ï¡¢³Æ¼ï¸À¸ì¤ä¡¢XIM ¤òÁªÂò¤¹¤ë¤³¤È¤â²ÄÇ½¤Ç¤¹¡£

%description -l pl
Gdm jest wysokokonfigurowaln± reimplementacj± xdma. Gdm pozwala
logowaæ siê do systemu z poziomu X11 i wspiera jednoczesn± pracê kilku
ró¿nych sesji X na lokalnej maszynie.

%description -l pt_BR
Gerenciador de Entrada do GNOME.

%description -l ru
GDM (GNOME Display Manager) - ÜÔÏ ÒÅÉÍÐÌÅÍÅÎÔÁÃÉÑ xdm (X Display
Manager). GDM ÐÏÚ×ÏÌÑÅÔ ×ÁÍ ×ÈÏÄÉÔØ × ÓÉÓÔÅÍÕ, ÎÁ ËÏÔÏÒÏÊ ÚÁÐÕÝÅÎÏ X
Window É ÐÏÄÄÅÒÖÉ×ÁÅÔ ÒÁÂÏÔÕ ÎÅÓËÏÌØÕÉÈ ÒÁÚÎÙÈ X ÓÅÁÎÓÏ× ÏÄÎÏ×ÒÅÍÅÎÎÏ.

%description -l uk
GDM (GNOME Display Manager) - ÃÅ ÒÅ¦ÍÐÌÅÍÅÎÔÁÃ¦Ñ xdm (X Display
Manager). GDM ÄÏÚ×ÏÌÑ¤ ×ÁÍ ×ÈÏÄÉÔÉ × ÓÉÓÔÅÍÕ, ÎÁ ÑË¦Ê ÚÁÐÕÝÅÎÏ X
Window ÔÁ Ð¦ÄÔÒÉÍÕ¤ ÒÏÂÏÔÕ Ë¦ÌØËÏÈ Ò¦ÚÎÉÈ X ÓÅÁÎÓ¦× ÏÄÎÏÞÁÓÎÏ.

%package Xnest
Summary:	Xnest (ie embedded X) server for GDM
Summary(pl):	Serwer Xnest dla GDM
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	XFree86-Xnest

%description Xnest
This package add support for Xnest server in gdm.

%description Xnest -l pl
Ten pakiet dodaje do gdm wsparcie dla Xnest.

%package init
Summary:	Init script for GDM
Summary(pl):	Skrypt init dla GDM-a
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	open
Requires(post,preun):	/sbin/chkconfig

%description init
Init script for GDM.

%description init -l pl
Skrypt init dla GDM-a.

%prep
%setup -q -a4
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
%{__libtoolize}
%{__glib_gettextize}
%{__intltoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-console-helper \
	--disable-scrollkeeper \
	--enable-authentication-scheme=pam \
	--with-pam-prefix=/etc \
	--with-tcp-wrappers=yes \
	--with%{!?with_selinux:out}-selinux \
	--with-xdmcp=yes \
	--with-xinerama=yes

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/{rc.d/init.d,pam.d,security} \
	$RPM_BUILD_ROOT{/home/services/xdm,/var/log/gdm} \
	$RPM_BUILD_ROOT%{_datadir}/gdm/themes/storky

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	PAM_PREFIX=/etc

mv $RPM_BUILD_ROOT%{_datadir}/gdm/BuiltInSessions/default.desktop \
	$RPM_BUILD_ROOT%{_datadir}/xsessions

install %{SOURCE1} $RPM_BUILD_ROOT/etc/pam.d/gdm
install %{SOURCE5} $RPM_BUILD_ROOT/etc/pam.d/gdm-autologin
install %{SOURCE2} $RPM_BUILD_ROOT/etc/rc.d/init.d/gdm

install %{SOURCE3} $RPM_BUILD_ROOT%{_pixmapsdir}

install storky/*.* $RPM_BUILD_ROOT%{_datadir}/gdm/themes/storky/

touch $RPM_BUILD_ROOT/etc/security/blacklist.gdm

%find_lang %{name} --all-name --with-gnome

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
%scrollkeeper_update_post

%postun
%scrollkeeper_update_postun
if [ "$1" = "0" ]; then
	%userremove xdm
	%groupremove xdm
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
%attr(755,root,root) %{_bindir}/gdm-dmx-reconnect-proxy
%attr(755,root,root) %{_bindir}/gdmdynamic
%attr(755,root,root) %{_bindir}/gdmflexiserver
%attr(755,root,root) %{_bindir}/gdmphotosetup
%attr(755,root,root) %{_bindir}/gdmthemetester
%attr(755,root,root) %{_libdir}/gdmaskpass
%attr(755,root,root) %{_libdir}/gdmopen
%attr(755,root,root) %{_libdir}/gdmtranslate
%attr(755,root,root) %{_libdir}/gdmchooser
%attr(755,root,root) %{_libdir}/gdmgreeter
%attr(755,root,root) %{_libdir}/gdmlogin
%attr(755,root,root) %{_sbindir}/*
%dir %{_sysconfdir}/gdm
%dir %{_sysconfdir}/gdm/modules
%attr(755,root,root) %config %{_sysconfdir}/gdm/Init
%attr(755,root,root) %config %{_sysconfdir}/gdm/PreSession
%attr(755,root,root) %config %{_sysconfdir}/gdm/PostSession
%attr(755,root,root) %config %{_sysconfdir}/gdm/XKeepsCrashing
%attr(755,root,root) %config %{_sysconfdir}/gdm/Xsession
%config %{_sysconfdir}/gdm/PostLogin/Default.sample
%config %{_sysconfdir}/gdm/locale.alias
%config %{_sysconfdir}/gdm/modules/*

%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/gdm/

%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/pam.d/gdm*
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/security/blacklist.gdm
%attr(750,xdm,xdm) /var/lib/gdm
%attr(750,xdm,xdm) /var/log/gdm
%attr(750,xdm,xdm) /home/services/xdm
%{_pixmapsdir}/*
%{_desktopdir}/gdmsetup.desktop
%{_desktopdir}/gdmflexiserver.desktop
%{_desktopdir}/gdmphotosetup.desktop
%{_datadir}/gdm
#%%{_datadir}/xsessions  -  moved to gnome-session
%{_datadir}/xsessions/default.desktop
%{_iconsdir}/hicolor/*/apps/*.png
%{_omf_dest_dir}/gdm
%attr(755,root,root) %{_libdir}/gtk-2.0/modules/lib*.so
%{_mandir}/man1/gdm*

%files Xnest
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gdmXnest
%attr(755,root,root) %{_bindir}/gdmXnestchooser
%{_desktopdir}/gdmflexiserver-xnest.desktop

%files init
%defattr(644,root,root,755)
%attr(754,root,root) /etc/rc.d/init.d/gdm
