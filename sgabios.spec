Name:           sgabios
# no official version of upstream sgabios tagged in the upstream repo
Version:        0
Release:        0.3.20110621svn%{?dist}
Summary:        Serial Graphics Adapter BIOS

Group:          Applications/Emulators
License:        ASL 2.0
URL:            http://code.google.com/p/sgabios/
# Tarball created from SVN archive using the following commands:
# svn export -r8 http://sgabios.googlecode.com/svn/trunk/ sgabios-svn-r8
# tar -cvzf sgabios-0.1-svnr8.tar.gz sgabios-svn-r8
Source0:        sgabios-svn-r8.tar.gz

BuildRoot:      %{_tmppath}/%{name}-%{release}-root-%(%{__id_u} -n)

ExclusiveArch: %{ix86} x86_64

Requires: %{name}-bin = %{version}-%{release}

# Sgabios is noarch, but required on architectures which cannot build it.
# Disable debuginfo because it is of no use to us.
%global debug_package %{nil}

%description
SGABIOS is designed to be inserted into a BIOS as an option rom to provide
over a serial port the display and input capabilities normally handled by
a VGA adapter and a keyboard, and additionally provide hooks for logging
displayed characters for later collection after an operating system boots.

%ifarch %{ix86} x86_64 
%package bin
Summary: Sgabios for x86
Buildarch: noarch

%description bin
SGABIOS is designed to be inserted into a BIOS as an option rom to provide
over a serial port the display and input capabilities normally handled by
a VGA adapter and a keyboard, and additionally provide hooks for logging
displayed characters for later collection after an operating system boots.
%endif

%prep
%setup -n sgabios-svn-r8

%build
%ifarch %{ix86} x86_64 
export CFLAGS="$RPM_OPT_FLAGS"
make
%endif


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/sgabios
%ifarch %{ix86} x86_64 
install -m 0644 sgabios.bin $RPM_BUILD_ROOT%{_datadir}/sgabios
%endif


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc COPYING design.txt

%ifarch %{ix86} x86_64 
%files bin
%defattr(-,root,root,-)
%dir %{_datadir}/sgabios/
%{_datadir}/sgabios/sgabios.bin
%endif


%changelog
* Tue Jul 26 2011 Eduardo Habkost <ehabkost@redhat.com> - sgabios-0-0.3.20110621svn.el6
- Change package summary to not mention trademarks unnecessarily
- Update info about tarball-generation command
- Related: bz#712993

* Tue Jul 26 2011 Eduardo Habkost <ehabkost@redhat.com> - sgabios-0-0.2.20110621svn.el6
- Regenerating tarball from svn
- Related: bz#712993

* Fri Jul 08 2011 Eduardo Habkost <ehabkost@redhat.com> - sgabios-0-0.1.20110621svn.el6
- Importing package into RHEL-6

* Tue Jun 21 2011 Justin M. Forbes <jforbes@redhat.com> 0.1-0.20110621SVN
- Created initial package
