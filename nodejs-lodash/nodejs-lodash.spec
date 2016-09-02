%global npm_name lodash

Name: nodejs-%{npm_name}
Version: 4.15.0
Release: 1%{?dist}
Summary: Lodash modular utilities
License: MIT
Group: Development/Libraries
URL: https://lodash.com
Source0: http://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
BuildRequires: nodejs-devel
BuildRequires: nodejs-packaging
BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch
Provides: npm(%{npm_name}) = %{version}

%description
A utility library delivering consistency, customization, performance, &
extras.

%package doc
Summary: Documentation for nodejs-%{npm_name}
Group: Documentation
Requires: nodejs-%{npm_name} = %{version}-%{release}
BuildArch: noarch

%description doc
This package contains documentation for nodejs-%{npm_name}

%prep
%setup -q -n package
rm -rf node_modules

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr *.json LICENSE fp *.md *.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
%nodejs_symlink_deps

%files
%{nodejs_sitelib}/%{npm_name}
%doc LICENSE

%files doc
%doc README.md

%changelog
* Thu Aug 11 2016 Dominic Cleal <dominic@cleal.org> 2.4.2-1
- new package built with tito

