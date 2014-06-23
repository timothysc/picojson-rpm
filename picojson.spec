%global commit da5c7988253f9a09851fc97f36f0fe4e7db07b9a
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           picojson
Summary:        A header-file-only, JSON parser serializer in C++
Version:        1.0.0
Release:        1.%{shortcommit}%{?dist}

Group:          Development/Libraries
License:        BSD
# http://opensource.org/licenses/BSD-2-Clause
URL:            https://github.com/kazuho/picojson

Source0:        https://github.com/kazuho/picojson/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz
BuildArch:      noarch

BuildRequires:  automake
Requires:       gcc-libstdc++-devel

%description
PicoJSON is a tiny JSON parser / serializer for C++ with following properties:

- Header-file only
- No external dependencies (only uses standard C++ libraries)
- STL-frendly (arrays are represented by using std::vector, objects are std::map)
provides both pull interface and streaming (event-based) interface

%prep
%setup -qn %{name}-%{commit}

%build
echo "Nothing to do"

%check
make test

%install
mkdir -p %{buildroot}%{_includedir}
install -m 0644 picojson.h %{buildroot}%{_includedir}/picojson.h

%files
%{_includedir}/picojson.h
%doc LICENSE README.mkdn examples

%changelog
* Mon Jun 23 2014 Timothy St. Clair <tstclair@redhat.com> 1.0.0-1
- initial rpm

