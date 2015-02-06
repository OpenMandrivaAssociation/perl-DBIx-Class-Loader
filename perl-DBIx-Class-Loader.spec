%define upstream_name	 DBIx-Class-Loader
%define upstream_version 0.21

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Dynamic definition of DBIx::Class sub classes
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/DBIx/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(DBD::SQLite2)
BuildRequires:	perl(Lingua::EN::Inflect)
BuildRequires:	perl(Test::Pod)
BuildRequires:	perl(Test::Pod::Coverage)
BuildRequires:	perl(UNIVERSAL::require)
BuildArch:	noarch

%description
DBIx::Class::Loader automate the definition of DBIx::Class sub-classes by
scanning table schemas and setting up columns and primary keys.  Class names
are defined by table names and the namespace option. The only required
arguments are namespace and dsn.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL installdirs=vendor destdir=%{buildroot}
make

%check
##export PG_NAME="dbi:Pg:dbname=test;host=localhost"
##export PG_USER=pgtest
##export PG_PASS='pgtest'
##export MYSQL_NAME="dbi:mysql:database=test;host=localhost"
##export MYSQL_USER=mysqltest
##export MYSQL_PASS='mysqltest'
#make test

%install
%makeinstall_std

%files
%doc Changes
%{perl_vendorlib}/DBIx
%{_mandir}/man*/*


%changelog
* Sun May 29 2011 Funda Wang <fwang@mandriva.org> 0.210.0-2mdv2011.0
+ Revision: 681358
- mass rebuild

* Tue Aug 04 2009 Jérôme Quelin <jquelin@mandriva.org> 0.210.0-1mdv2011.0
+ Revision: 408952
- rebuild using %%perl_convert_version

* Mon Sep 29 2008 Oden Eriksson <oeriksson@mandriva.com> 0.21-2mdv2009.0
+ Revision: 289470
- rebuild

* Thu Dec 20 2007 Olivier Blin <oblin@mandriva.com> 0.21-1mdv2008.1
+ Revision: 135833
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon May 07 2007 Buchan Milne <bgmilne@mandriva.org> 0.21-1mdv2008.0
+ Revision: 24906
- Import perl-DBIx-Class-Loader

