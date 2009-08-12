%{!?python_sitelib:  %global python_sitelib  %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}

Name:		vboxgtk
Version:	0.5.0
Release:	2%{?dist}
Summary:	A simple GTK frontend for VirtualBox  

Group:		Applications/Emulators
License:	GPLv3
URL:		http://vboxgtk.sourceforge.net/
Source0:	http://freefr.dl.sourceforge.net/project/%{name}/%{name}/%{name}/%{name}-%{version}.tar.gz
#Patch0: fix the vboxgtk desktop file, filed in : https://sourceforge.net/tracker/?func=detail&aid=2834528&group_id=263334&atid=1134168
Patch0:		vboxgtk-vboxgtk.desktop.in.patch
#Patch1: fix VirtualBox-OSE paths in vboxgtk launcher
Patch1:		vboxgtk-vboxpath.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%if 0%{?fedora} > 11
ExclusiveArch:  i686 x86_64
%else %if 0%{?fedora} > 10
ExclusiveArch:  i586 x86_64
%else
ExclusiveArch:  i386 x86_64
%endif

Requires:	python-VirtualBox-OSE

%description
A simple GTK frontend for VirtualBox.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build


%install
rm -rf $RPM_BUILD_ROOT
./setup.py install --root $RPM_BUILD_ROOT
%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT


%files -f %{name}.lang
%defattr(-,root,root,-)
%doc AUTHORS COPYING README
%{_bindir}/%{name}
%{python_sitelib}/%{name}
%{python_sitelib}/%{name}-%{version}*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
%{_datadir}/icons/hicolor/22x22/apps/%{name}.png
%{_datadir}/icons/hicolor/24x24/apps/%{name}.png
%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/%{name}

%changelog
* Sun Aug 09 2009 Hicham HAOUARI <hicham.haouari@gmail.com> 0.5.0-2
- Spec cleanup (https://bugzilla.rpmfusion.org/show_bug.cgi?id=751#c2).
* Fri Aug 07 2009 Hicham HAOUARI <hicham.haouari@gmail.com> 0.5.0-1
- Initial package for rpmfusion.
