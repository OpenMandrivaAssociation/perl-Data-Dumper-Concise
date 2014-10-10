%define upstream_name    Data-Dumper-Concise
%define upstream_version 2.022

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

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


