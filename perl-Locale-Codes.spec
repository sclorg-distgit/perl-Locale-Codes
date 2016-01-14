%{?scl:%scl_package perl-Locale-Codes}
%{!?scl:%global pkg_name %{name}}

Name:           %{?scl_prefix}perl-Locale-Codes
Version:        3.27
Release:        2.sc1%{?dist}
Summary:        Distribution of modules to handle locale codes
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Locale-Codes/
Source0:        http://www.cpan.org/authors/id/S/SB/SBECK/Locale-Codes-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  %{?scl_prefix}perl
BuildRequires:  %{?scl_prefix}perl(ExtUtils::MakeMaker)
BuildRequires:  %{?scl_prefix}perl(strict)
BuildRequires:  %{?scl_prefix}perl(warnings)
# Run-time
BuildRequires:  %{?scl_prefix}perl(Carp)
BuildRequires:  %{?scl_prefix}perl(constant)
BuildRequires:  %{?scl_prefix}perl(Exporter)
BuildRequires:  %{?scl_prefix}perl(utf8)
# Tests
BuildRequires:  %{?scl_prefix}perl(Storable)
BuildRequires:  %{?scl_prefix}perl(Test::More)
%{?scl:%global perl_version %(scl enable %{scl} 'eval "`perl -V:version`"; echo $version')}
%{!?scl:%global perl_version %(eval "`perl -V:version`"; echo $version)}
Requires:       %{?scl_prefix}perl(:MODULE_COMPAT_%{perl_version})

# Inject not detected module version
Provides:       %{?scl_prefix}perl(Locale::Codes) = %{version}


# Filter under-specified provides
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}perl\\(Locale::Codes\\)$

# Filter dependencies on private modules. Generator:
# for F in $(find lib -type f); do perl -e '$/ = undef; $_ = <>; if (/^package #\R([\w:]*);/m) { print qq{|^perl\\\\($1\\\\)} }' "$F"; done
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^%{?scl_prefix}perl\\(Locale::Codes::Country_Retired\\)|^%{?scl_prefix}perl\\(Locale::Codes::Script_Retired\\)|^%{?scl_prefix}perl\\(Locale::Codes::LangExt_Codes\\)|^%{?scl_prefix}perl\\(Locale::Codes::LangFam_Codes\\)|^%{?scl_prefix}perl\\(Locale::Codes::Script_Codes\\)|^%{?scl_prefix}perl\\(Locale::Codes::Language_Codes\\)|^%{?scl_prefix}perl\\(Locale::Codes::LangExt_Retired\\)|^%{?scl_prefix}perl\\(Locale::Codes::Currency_Codes\\)|^%{?scl_prefix}perl\\(Locale::Codes::LangVar_Retired\\)|^%{?scl_prefix}perl\\(Locale::Codes::Language_Retired\\)|^%{?scl_prefix}perl\\(Locale::Codes::Country_Codes\\)|^%{?scl_prefix}perl\\(Locale::Codes::LangVar_Codes\\)|^%{?scl_prefix}perl\\(Locale::Codes::Currency_Retired\\)

%if ( 0%{?rhel} && 0%{?rhel} < 7 )
%{?filter_setup:
%filter_from_provides /perl(Locale::Codes)$/d
%filter_from_requires /^%{?scl_prefix}perl(Locale::Codes::\(Country_Retired\|Script_Retired\|LangExt_Codes\|LangFam_Codes\|Script_Codes\|Language_Codes\|LangExt_Retired\|Currency_Codes\|LangVar_Retired\|Language_Retired\|Country_Codes\|LangVar_Codes\|Currency_Retired\))/d
%filter_setup
}
%endif

%description
Locale-Codes is a distribution containing a set of modules. The modules
each deal with different types of codes which identify parts of the locale
including languages, countries, currency, etc.

%prep
%setup -q -n Locale-Codes-%{version}
chmod -x examples/*

%build
%{?scl:scl enable %{scl} "}
perl Makefile.PL INSTALLDIRS=vendor
%{?scl:"}
%{?scl:scl enable %{scl} "}
make %{?_smp_mflags}
%{?scl:"}

%install
%{?scl:scl enable %{scl} "}
make pure_install DESTDIR=%{buildroot}
%{?scl:"}
find %{buildroot} -type f -name .packlist -exec rm -f {} \;
%{_fixperms} %{buildroot}/*

%check
%{?scl:scl enable %{scl} "}
make test
%{?scl:"}

%files
%doc examples ChangeLog LICENSE README README.first
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Thu Feb 13 2014 Jitka Plesnikova <jplesnik@redhat.com> - 3.27-2
- Updated conditions to work properly for non-RHEL systems
- Resolves: rhbz#1064855

* Tue Nov 19 2013 Jitka Plesnikova <jplesnik@redhat.com> - 3.27-1
- 3.27 bump

* Mon May 20 2013 Jitka Plesnikova <jplesnik@redhat.com> - 3.25-1
- 3.25 bump

* Wed Feb 13 2013 Jitka Plesnikova <jplesnik@redhat.com> - 3.24-1
- SCL package - initial import
