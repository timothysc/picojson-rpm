%global commit
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           picojson
Summary:        A header-file-only, JSON parser serializer in C++
Version:        0.0.1
Release:        1.%{shortcommit}%{?dist}

Group:          Development/Libraries
License:        BSD
# http://opensource.org/licenses/BSD-2-Clause
URL:            https://github.com/kazuho/picojson

Source0:        https://github.com/kazuho/picojson/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz
BuildArch:      noarch

%description
PicoJSON is a tiny JSON parser / serializer for C++ with following properties:

- Header-file only
- No external dependencies (only uses standard C++ libraries)
- STL-frendly (arrays are represented by using std::vector, objects are std::map)
provides both pull interface and streaming (event-based) interface

%prep
%setup -qn %{name}-%{commit}

%build
echo

%check
echo "Nothing to do"

%install



%files
%{_includedir}/picojson.h
%doc README.mkdn
# install examples?

%changelog
* Tue Jun 3 2014 Timothy St. Clair <tstclair@redhat.com> 0.0.1-1.
-

