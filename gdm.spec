Summary:	GNOME Display Manager
Summary(pl):	gdm
Name:		gdm
Version:	2.0beta4
Release:	6
Source0:	ftp://socsci.auc.dk/~mkp/gdm/%{name}-%{version}.tar.gz
Source1:	%{name}.pamd
Source2:	%{name}.init
Patch0:	%{name}-config.patch
Patch1:	%{name}-gnomerc.patch
Patch2:	%{name}-chpass.patch
Patch3:	%{name}-daemonfixes.patch
Patch4:	%{name}-dumberrmsg.patch
Patch5:	%{name}-fdleak.patch
Patch6:	%{name}-fixmessages.patch
Patch7:	%{name}-i18n.patch
Patch8:	%{name}-loopofdeath.patch
Patch9:	%{name}-no_questions_asked.patch
Patch10:	%{name}-pipewrite.patch
Patch11:	%{name}-rhlang.patch
Patch12:	%{name}-system-auth.patch
Patch13:	%{name}-tolower.patch
Patch14:	%{name}-usershell.patch
Patch15:	%{name}-nonbash-shell.patch
Patch16:	%{name}-xdmcp.patch
Patch17:	%{name}-ypconfigure.patch
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
License:	LGPL/GPL
Prereq:		/usr/sbin/groupadd
Prereq:		/usr/sbin/groupdel
Prereq:		/usr/sbin/useradd
Prereq:		/usr/sbin/userdel
Prereq:		/sbin/chkconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildRequires:	gnome-libs-devel
BuildRequires:	gtk+-devel
BuildRequires:	esound-devel
Requires:	gnome-libs >= 1.0.0
Requires:	which
Requires:	/usr/X11R6/bin/sessreg
Obsoletes:	xdm kdm wdm

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man
%define		_sysconfdir	/etc/X11

%description 
gdm manages local and remote displays and provides the user with a
graphical login window.

%description -l pl
gdm zarz±dza lokalnymi i zdalnymi X serwerami i udostêpnia
u¿ytkownikowi graficzne okienko logowania.

%prep
%setup -q
%patch0 -p1	
%patch1 -p1	
%patch2 -p1	
%patch3 -p1	
%patch4 -p1	
%patch5 -p1	
%patch6 -p1	
%patch7 -p1	
%patch8 -p1	
%patch9 -p1	
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1

%build
CFLAGS="$RPM_OPT_FLAGS" \
./configure %{_target_platform} \
	--prefix=%{_prefix} \
	--sysconfdir=%{_sysconfdir} \
	--localstatedir=/var/lib
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/etc/rc.d/init.d/

install -d $RPM_BUILD_ROOT{%{_prefix},/etc/{pam.d,security}}
install %{SOURCE2} $RPM_BUILD_ROOT/etc/rc.d/init.d/gdm

%{__make} install prefix=$RPM_BUILD_ROOT%{_prefix} \
	sysconfdir=$RPM_BUILD_ROOT%{_sysconfdir} \
	localstatedir=$RPM_BUILD_ROOT/var/lib

sed -e "s#$RPM_BUILD_ROOT##g" config/gnomerc >config/gnomerc.X
install config/gnomerc.X $RPM_BUILD_ROOT%{_sysconfdir}/gdm/gnomerc

sed -e "s#$RPM_BUILD_ROOT##g" $RPM_BUILD_ROOT%{_sysconfdir}/gdm/Sessions/Gnome \
	> $RPM_BUILD_ROOT%{_sysconfdir}/gdm/Sessions/Gnome.X

mv -f $RPM_BUILD_ROOT%{_sysconfdir}/gdm/Sessions/Gnome.X \
	$RPM_BUILD_ROOT%{_sysconfdir}/gdm/Sessions/Gnome

install %{SOURCE1} $RPM_BUILD_ROOT/etc/pam.d/gdm
touch $RPM_BUILD_ROOT/etc/security/blacklist.gdm

strip $RPM_BUILD_ROOT%{_bindir}/* || :

gzip -9nf AUTHORS ChangeLog NEWS README TODO RELEASENOTES

%find_lang gdm

%pre
/usr/sbin/groupadd -g 55 -r -f xdm

if [ -z "`id -u xdm 2>/dev/null`" ]; then
	/usr/sbin/useradd -u 55 -r -d /dev/null -s /bin/false -c 'X Display Manager' -g xdm xdm 1>&2
fi

%post
/sbin/chkconfig --add gdm
if [ -f /var/lock/subsys/gdm ]; then
        /etc/rc.d/init.d/gdm restart >&2
else
        echo "Run \"/etc/rc.d/init.d/gdm start\" to start gdm." >&2
fi

%preun
if [ -f /var/lock/subsys/gdm ]; then
		 /etc/rc.d/init.d/gdm stop >&2
fi
/sbin/chkconfig --del gdm

%postun
if [ "$1" = "0" ]; then

	if [ -n "`id -u xdm 2>/dev/null`" ]; then
		/usr/sbin/userdel xdm
	fi
	
	/usr/sbin/groupdel xdm

fi

%clean
rm -rf $RPM_BUILD_ROOT

%files -f gdm.lang
%defattr(644,root,root,755)
%doc {AUTHORS,ChangeLog,NEWS,README,TODO}.gz
%attr(775,root,xdm) %{_bindir}/gdm
%attr(775,root,xdm) %{_bindir}/gdmlogin
%attr(775,root,xdm) %{_bindir}/gdmchooser
%attr(775,root,xdm) %config %{_sysconfdir}/gdm/Init
%attr(775,root,xdm) %config %{_sysconfdir}/gdm/PreSession
%attr(775,root,xdm) %config %{_sysconfdir}/gdm/Sessions
%attr(775,root,xdm) %config %{_sysconfdir}/gdm/PostSession
%attr(775,root,xdm) %config %{_sysconfdir}/gdm/gnomerc
%attr(664,root,xdm) %config %{_sysconfdir}/gdm/gdm.conf
%attr(664,root,xdm) %config %{_sysconfdir}/gdm/locale.alias
%attr(775,root,xdm) %dir %{_sysconfdir}/gdm
%attr(640,root,root) %config %verify(not size mtime md5) /etc/pam.d/gdm
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) /etc/security/blacklist.gdm
%attr(750,xdm,xdm) /var/lib/gdm
%attr(754,root,root) /etc/rc.d/init.d/gdm
%{_datadir}/pixmaps/*
