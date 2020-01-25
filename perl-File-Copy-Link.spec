#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	File
%define	pnam	Copy-Link
Summary:	File::Copy::Link - Perl extension for replacing a link by a copy of the linked file
Summary(pl.UTF-8):	File::Copy::Link - rozszerzenie Perla do zastępowania dowiązania kopią pliku
Name:		perl-File-Copy-Link
Version:	0.113
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/File/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	5552b64bf90fd59833b9a55d71e3a907
URL:		http://search.cpan.org/dist/File-Copy-Link/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module is mostly a wrapper round "File::Spec::Link::linked" and
"File::Copy::copy", the functionality is available in a command line
script copylink.

%description -l pl.UTF-8
Ten moduł to w większości obudowanie na "File::Spec::Link::linked" i
"File::Copy::copy"; jego funkcjonalność jest dostępna z linii poleceń
poprzez skrypt copylink.

%package -n perl-File-Spec-Link
Summary:	File::Spec::Link - Perl extension for reading and resolving symbolic links
Summary(pl.UTF-8):	File::Spec::Link - rozszerzenie Perla do odczytu i rozwiązywania dowiązań symbolicznych
Group:		Development/Languages/Perl

%description -n perl-File-Spec-Link
File::Spec::Link is an extension to File::Spec, adding methods for
resolving symbolic links; it was created to implement
File::Copy::Link.

%description -n perl-File-Spec-Link -l pl.UTF-8
File::Spec::Link to rozszerzenie File::Spec dodające metody do
rozwiązywania dowiązań symbolicznych; zostało stworzone w celu
zaimplementowania File::Copy::Link.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build
# fix perl path
sed -ie 's$#!perl$#!/usr/bin/perl$' copylink

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%attr(755,root,root) %{_bindir}/copylink
%{perl_vendorlib}/File/Copy/*.pm
%{_mandir}/man3/File::Copy*
%{_mandir}/man1/copylink*

%files -n perl-File-Spec-Link
%defattr(644,root,root,755)
%{perl_vendorlib}/File/Spec/Link.pm
%{_mandir}/man3/File::Spec*
