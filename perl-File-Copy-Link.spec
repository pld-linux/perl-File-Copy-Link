#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	File
%define	pnam	Copy-Link
Summary:	File::Copy::Link - Perl extension for replacing a link by a copy of the linked file
#Summary(pl):	
Name:		perl-File-Copy-Link
Version:	0.110
Release:	0.1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	b434d5069cf108950ed785565916c2b0
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module is mostly a wrapper round "File::Spec::Link::linked" and
"File::Copy::copy", the functionality is available in a command line
script copylink.

# %description -l pl
# TODO

%package -n perl-File-Spec-Link
Summary:	File::Spec::Link - Perl extension for reading and resolving symbolic links
Group:		Development/Languages/Perl

%description -n perl-File-Spec-Link
File::Spec::Link is an extension to File::Spec, adding methods for
resolving symbolic links; it was created to implement File::Copy::Link.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{_bindir}/copylink
%{perl_vendorlib}/File/Copy/*.pm
%{_mandir}/man3/File::Copy*
%{_mandir}/man1/copylink*

%files -n perl-File-Spec-Link
%{perl_vendorlib}/File/Spec/Link.pm
%{_mandir}/man3/File::Spec*
