%define upstream_name    Data-Dumper-Concise
%define upstream_version 2.020

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Less indentation and newlines plus sub deparsing
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Data/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Devel::ArgNames)
BuildRequires:	perl(ExtUtils::MakeMaker)

BuildArch:	noarch

%description
This module always exports a single function, Dumper, which can be called
with a single reference value to dump that value or with no arguments to
return the Data::Dumper object it's created.

It exists, fundamentally, as a convenient way to reproduce a set of Dumper
options that we've found ourselves using across large numbers of
applications, primarily for debugging output.

The principle guiding theme is "all the concision you can get while still
having a useful dump and not doing anything cleverer than setting
Data::Dumper options" - it's been pointed out to us that
Data::Dump::Streamer can produce shorter output with less lines of code. We
know. This is simpler and we've never seen it segfault. But for
complex/weird structures, it generally rocks. You should use it as well,
when Concise is underkill. We do.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 2.20.0-2mdv2011.0
+ Revision: 656902
- rebuild for updated spec-helper

* Sun Jan 30 2011 Guillaume Rousse <guillomovitch@mandriva.org> 2.20.0-1
+ Revision: 634222
- update to new version 2.020

* Thu Sep 02 2010 Jérôme Quelin <jquelin@mandriva.org> 2.12.0-1mdv2011.0
+ Revision: 575394
- update to 2.012

* Tue Aug 17 2010 Jérôme Quelin <jquelin@mandriva.org> 2.10.0-1mdv2011.0
+ Revision: 570740
- update to 2.010

* Tue Jul 27 2010 Jérôme Quelin <jquelin@mandriva.org> 2.1.0-1mdv2011.0
+ Revision: 561850
- adding missing buildrequires:
- update to 2.001

* Sun Feb 14 2010 Jérôme Quelin <jquelin@mandriva.org> 1.200.0-1mdv2011.0
+ Revision: 505677
- update to 1.200

* Sat Dec 12 2009 Jérôme Quelin <jquelin@mandriva.org> 1.100.0-1mdv2010.1
+ Revision: 477619
- update to 1.100

* Tue Nov 24 2009 Jérôme Quelin <jquelin@mandriva.org> 1.2.0-1mdv2010.1
+ Revision: 469431
- update to 1.002

* Sat Nov 14 2009 Jérôme Quelin <jquelin@mandriva.org> 1.1.0-1mdv2010.1
+ Revision: 466005
- import perl-Data-Dumper-Concise


* Sat Nov 14 2009 cpan2dist 1.001-1mdv
- initial mdv release, generated with cpan2dist
