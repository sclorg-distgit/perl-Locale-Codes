%{?scl:%scl_package perl-Locale-Codes}

Name:           %{?scl_prefix}perl-Locale-Codes
Version:        3.39
Release:        2%{?dist}
Summary:        Distribution of modules to handle locale codes
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Locale-Codes/
Source0:        http://www.cpan.org/authors/id/S/SB/SBECK/Locale-Codes-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  %{?scl_prefix}perl
BuildRequires:  %{?scl_prefix}perl-generators
BuildRequires:  %{?scl_prefix}perl(ExtUtils::MakeMaker) >= 6.30
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
Requires:       %{?scl_prefix}perl(:MODULE_COMPAT_%(%{?scl:scl enable %{scl} '}eval "$(perl -V:version)";echo $version%{?scl:'}))

%if 0%{?rhel} < 7
# RPM 4.8 style
%{?filter_setup:
# Filter under-specified privdes
%filter_from_provides /^%{?scl_prefix}perl(Locale::Codes)$/d
# Filter dependencies on private modules. Generator:
# for F in $(find lib -type f); do perl -e '$/ = undef; $_ = <>; if (/^package #\R([\w:]*);/m) { print qq{|^%{?scl_prefix}perl\\\\($1\\\\)} }' "$F"; done
%filter_from_requires /^%{?scl_prefix}perl(Locale::Codes::Country_Retired)/d
%filter_from_requires /^%{?scl_prefix}perl(Locale::Codes::LangFam_Retired)/d
%filter_from_requires /^%{?scl_prefix}perl(Locale::Codes::Script_Retired)/d
%filter_from_requires /^%{?scl_prefix}perl(Locale::Codes::LangExt_Codes)/d
%filter_from_requires /^%{?scl_prefix}perl(Locale::Codes::LangFam_Codes)/d
%filter_from_requires /^%{?scl_prefix}perl(Locale::Codes::Script_Codes)/d
%filter_from_requires /^%{?scl_prefix}perl(Locale::Codes::Language_Codes)/d
%filter_from_requires /^%{?scl_prefix}perl(Locale::Codes::LangExt_Retired)/d
%filter_from_requires /^%{?scl_prefix}perl(Locale::Codes::Currency_Codes)/d
%filter_from_requires /^%{?scl_prefix}perl(Locale::Codes::LangVar_Retired)/d
%filter_from_requires /^%{?scl_prefix}perl(Locale::Codes::Language_Retired)/d
%filter_from_requires /^%{?scl_prefix}perl(Locale::Codes::Country_Codes)/d
%filter_from_requires /^%{?scl_prefix}perl(Locale::Codes::LangVar_Codes)/d
%filter_from_requires /^%{?scl_prefix}perl(Locale::Codes::Currency_Retired)/d
%?perl_default_filter
}
%else
# RPM 4.9 style
# Filter under-specified provides
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^%{?scl_prefix}perl\\(Locale::Codes\\)$
# Filter dependencies on private modules. Generator:
# for F in $(find lib -type f); do perl -e '$/ = undef; $_ = <>; if (/^package #\R([\w:]*);/m) { print qq{|^%{?scl_prefix}perl\\\\($1\\\\)} }' "$F"; done
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^%{?scl_prefix}perl\\(Locale::Codes::Country_Retired\\)|^%{?scl_prefix}perl\\(Locale::Codes::LangFam_Retired\\)|^%{?scl_prefix}perl\\(Locale::Codes::Script_Retired\\)|^%{?scl_prefix}perl\\(Locale::Codes::LangExt_Codes\\)|^%{?scl_prefix}perl\\(Locale::Codes::LangFam_Codes\\)|^%{?scl_prefix}perl\\(Locale::Codes::Script_Codes\\)|^%{?scl_prefix}perl\\(Locale::Codes::Language_Codes\\)|^%{?scl_prefix}perl\\(Locale::Codes::LangExt_Retired\\)|^%{?scl_prefix}perl\\(Locale::Codes::Currency_Codes\\)|^%{?scl_prefix}perl\\(Locale::Codes::LangVar_Retired\\)|^%{?scl_prefix}perl\\(Locale::Codes::Language_Retired\\)|^%{?scl_prefix}perl\\(Locale::Codes::Country_Codes\\)|^%{?scl_prefix}perl\\(Locale::Codes::LangVar_Codes\\)|^%{?scl_prefix}perl\\(Locale::Codes::Currency_Retired\\)
%endif

%description
Locale-Codes is a distribution containing a set of modules. The modules
each deal with different types of codes which identify parts of the locale
including languages, countries, currency, etc.

%prep
%setup -q -n Locale-Codes-%{version}
chmod -x examples/*

%build
%{?scl:scl enable %{scl} '}perl Makefile.PL INSTALLDIRS=vendor && make %{?_smp_mflags}%{?scl:'}

%install
%{?scl:scl enable %{scl} '}make pure_install DESTDIR=%{buildroot}%{?scl:'}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} %{buildroot}/*

%check
%{?scl:scl enable %{scl} '}make test%{?scl:'}

%files
%doc LICENSE
%doc Changes examples README README.first
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Mon Jul 11 2016 Petr Pisar <ppisar@redhat.com> - 3.39-2
- SCL

* Wed Jun 01 2016 Petr Pisar <ppisar@redhat.com> - 3.39-1
- 3.39 bump

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 3.38-2
- Perl 5.24 rebuild

* Thu Mar 03 2016 Petr Pisar <ppisar@redhat.com> - 3.38-1
- 3.38 bump

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.37-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Dec 02 2015 Petr Pisar <ppisar@redhat.com> - 3.37-1
- 3.37 bump

* Wed Sep 02 2015 Petr Pisar <ppisar@redhat.com> - 3.36-1
- 3.36 bump (Locale::Codes::_delete_code_alias() removed)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.35-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 3.35-2
- Perl 5.22 rebuild

* Tue Jun 02 2015 Petr Pisar <ppisar@redhat.com> - 3.35-1
- 3.35 bump

* Tue Mar 03 2015 Petr Pisar <ppisar@redhat.com> - 3.34-1
- 3.34 bump

* Fri Dec 05 2014 Petr Pisar <ppisar@redhat.com> - 3.33-1
- 3.33 bump

* Wed Sep 10 2014 Petr Pisar <ppisar@redhat.com> - 3.32-1
- 3.32 bump

* Tue Aug 26 2014 Jitka Plesnikova <jplesnik@redhat.com> - 3.31-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.31-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Jun 02 2014 Petr Pisar <ppisar@redhat.com> - 3.31-1
- 3.31 bump

* Wed Mar 05 2014 Petr Pisar <ppisar@redhat.com> - 3.30-1
- 3.30 bump

* Thu Jan 30 2014 Petr Pisar <ppisar@redhat.com> - 3.29-1
- 3.29 bump

* Wed Dec 04 2013 Petr Pisar <ppisar@redhat.com> - 3.28-2
- Filter private module Locale::Codes::LangFam_Retired from dependencies

* Tue Dec 03 2013 Petr Pisar <ppisar@redhat.com> - 3.28-1
- 3.28 bump

* Thu Sep 12 2013 Petr Pisar <ppisar@redhat.com> - 3.27-2
- Filter dependencies on private modules

* Tue Sep 10 2013 Petr Pisar <ppisar@redhat.com> - 3.27-1
- 3.27 bump

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.26-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jul 12 2013 Petr Pisar <ppisar@redhat.com> - 3.26-2
- Perl 5.18 rebuild

* Fri Jun 07 2013 Petr Pisar <ppisar@redhat.com> - 3.26-1
- 3.26 bump

* Fri Mar 01 2013 Petr Pisar <ppisar@redhat.com> - 3.25-1
- 3.25 bump

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Dec 05 2012 Petr Pisar <ppisar@redhat.com> - 3.24-1
- 3.24 bump

* Tue Nov 20 2012 Petr Šabata <contyk@redhat.com> - 3.23-2
- Add missing deps
- Drop command macros
- Modernize spec

* Tue Sep 04 2012 Petr Pisar <ppisar@redhat.com> - 3.23-1
- 3.23 bump

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.22-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 06 2012 Petr Pisar <ppisar@redhat.com> - 3.22-2
- Perl 5.16 rebuild

* Mon Jun 04 2012 Petr Pisar <ppisar@redhat.com> - 3.22-1
- 3.22 bump

* Mon Jun 04 2012 Petr Pisar <ppisar@redhat.com> - 3.21-2
- The POD tests do not run by default anymore
- Switch build script from Module::Build to EU::MM

* Fri Mar 02 2012 Petr Pisar <ppisar@redhat.com> - 3.21-1
- 3.21 bump

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Dec 02 2011 Petr Pisar <ppisar@redhat.com> - 3.20-1
- 3.20 bump

* Thu Sep 01 2011 Petr Pisar <ppisar@redhat.com> - 3.18-1
- 3.18 bump

* Thu Jun 30 2011 Petr Pisar <ppisar@redhat.com> 3.17-1
- Specfile autogenerated by cpanspec 1.78.
- Remove BuildRoot and defattr
