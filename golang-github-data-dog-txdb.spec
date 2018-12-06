# Run tests in check section
# disabled, need a mysql database
%bcond_with check

%global goipath         github.com/DATA-DOG/go-txdb
Version:                0.1.0

%global common_description %{expand:
Single transaction sql driver for golang.}

%gometa

Name:           %{goname}
Release:        2%{?dist}
Summary:        Single transaction sql driver for golang 
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}

%if %{with check}
BuildRequires:  golang(github.com/go-sql-driver/mysql)
%endif

%description
%{common_description}


%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{common_description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgeautosetup


%install
%goinstall


%if %{with check}
%check
%gochecks
%endif


%files devel -f devel.file-list
%license LICENSE
%doc README.md


%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Mar 20 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.1.0-1
- First package for Fedora

