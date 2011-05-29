%define upstream_name	 DBIx-Class-Loader
%define upstream_version 0.21

#define _provides_exceptions perl(DB::Main

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:	Dynamic definition of DBIx::Class sub classes
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/DBIx/%{upstream_name}-%{upstream_version}.tar.gz

%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires:	perl(DBD::SQLite2)
BuildRequires:	perl(Lingua::EN::Inflect)
BuildRequires:	perl(Test::Pod)
BuildRequires:	perl(Test::Pod::Coverage)
BuildRequires:	perl-UNIVERSAL-require
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
DBIx::Class::Loader automate the definition of DBIx::Class sub-classes by
scanning table schemas and setting up columns and primary keys.  Class names
are defined by table names and the namespace option. The only required
arguments are namespace and dsn.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
%{perl_vendorlib}/DBIx
%{_mandir}/man*/*
