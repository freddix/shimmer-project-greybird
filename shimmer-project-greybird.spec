Summary:	Greybird theme
Name:		shimmer-project-greybird
Version:	1.4
Release:	3
License:	GPL v2 and Attribution-ShareAlike 3.0 Unported
Group:		X11/Themes
#Source0:	https://github.com/shimmerproject/Greybird/archive/v%{version}.tar.gz
Source0:	https://github.com/shimmerproject/Greybird/archive/master.zip
# Source0-md5:	fb633bec4a999789677b1238cd086732
BuildRequires:	automake
URL:		http://shimmerproject.org/project/greybird/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_enable_debug_packages	0

%description
Greybird is a set of themes for programs using GTK+ created by
The Shimmer Project.

%package -n gtk+-theme-greybird
Summary:	Greybird GTK+ theme
Group:		Themes
Requires:	shimmer-project-greybird = %{version}-%{release}
Requires:	gtk+-theme-engine-murrine

%description -n gtk+-theme-greybird
Greybird theme - GTK+ variant.

%package -n gtk+3-theme-greybird
Summary:	Greybird GTK+3 theme
Group:		Themes
Requires:	shimmer-project-greybird = %{version}-%{release}

%description -n gtk+3-theme-greybird
Greybird theme - GTK+3 variant.

%package -n metacity-theme-greybird
Summary:	Greybird Metacity theme
Group:		Themes
Requires:	shimmer-project-greybird = %{version}-%{release}

%description -n metacity-theme-greybird
Greybird theme for Metacity window manager.

%package -n xfwm4-theme-greybird
Summary:	Greybird xfwm4 theme
Group:		Themes
Requires:	shimmer-project-greybird = %{version}-%{release}
Requires:	xfwm4

%description -n xfwm4-theme-greybird
Greybird theme for xfwm4 window manager.

%package -n xfce4-notifyd-theme-greybird
Summary:	Greybird theme for xfce4-notifyd
Group:		Themes
Requires:	shimmer-project-greybird = %{version}-%{release}
Requires:	xfce4-notifyd

%description -n xfce4-notifyd-theme-greybird
Greybird theme for xfce4-notifyd notification daemon.

%prep
#%setup -qn Greybird-%{version}
%setup -qn Greybird-master

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/themes/Greybird

cp -ar gtk-2.0 gtk-3.0 metacity-1 xfce-notify-4.0 xfwm4 xfwm4_compact index.theme \
	$RPM_BUILD_ROOT%{_datadir}/themes/Greybird

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE.CC README
%dir %{_datadir}/themes/Greybird
%{_datadir}/themes/Greybird/index.theme

%files -n gtk+-theme-greybird
%defattr(644,root,root,755)
%{_datadir}/themes/Greybird/gtk-2.0

%files -n gtk+3-theme-greybird
%defattr(644,root,root,755)
%{_datadir}/themes/Greybird/gtk-3.0

%files -n metacity-theme-greybird
%defattr(644,root,root,755)
%{_datadir}/themes/Greybird/metacity-1

%files -n xfce4-notifyd-theme-greybird
%defattr(644,root,root,755)
%{_datadir}/themes/Greybird/xfce-notify-4.0

%files -n xfwm4-theme-greybird
%defattr(644,root,root,755)
%{_datadir}/themes/Greybird/xfwm4
%{_datadir}/themes/Greybird/xfwm4_compact

