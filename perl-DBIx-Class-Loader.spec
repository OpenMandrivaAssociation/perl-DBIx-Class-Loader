%define module	DBIx-Class-Loader
%define name	perl-%{module}
%define	modprefix DBIx

%define version 0.21

%define	rel	1
%define release %mkrel %{rel}

#define _provides_exceptions perl(DB::Main

Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL or Artistic
Group:		Development/Perl
Summary:	Dynamic definition of DBIx::Class sub classes
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{modprefix}/%{module}-%{version}.tar.gz
Url:		http://search.cpan.org/dist/%{module}
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires:	perl-UNIVERSAL-require
BuildRequires:	perl(Lingua::EN::Inflect)
BuildRequires:	perl(Test::Pod)
BuildRequires:	perl(DBD::SQLite2)
BuildRequires:	perl(Test::Pod::Coverage)
BuildArch:	noarch

%description
DBIx::Class::Loader automate the definition of DBIx::Class sub-classes by
scanning table schemas and setting up columns and primary keys.  Class names
are defined by table names and the namespace option. The only required
arguments are namespace and dsn.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL installdirs=vendor destdir=%{buildroot}
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
rm -rf %{buildroot}
make install

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes
%{perl_vendorlib}/%{modprefix}
%{_mandir}/man*/*
