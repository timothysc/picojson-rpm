%global commit 59e34764c56690c8e864045a642aae736c8f4769
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           picojson
Summary:        A header-file-only, JSON parser serializer in C++
Version:        1.1.0
Release:        1.%{shortcommit}%{?dist}

Group:          Development/Libraries
License:        BSD
# http://opensource.org/licenses/BSD-2-Clause
URL:            https://github.com/kazuho/picojson

Source0:        https://github.com/kazuho/picojson/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz

BuildRequires:  automake
Requires:       gcc-libstdc++-devel

%description
PicoJSON is a tiny JSON parser / serializer for C++ with following properties:

- Header-file only
- No external dependencies (only uses standard C++ libraries)
- STL-frendly (arrays are represented by using std::vector, objects are std::map)
provides both pull interface and streaming (event-based) interface

%package devel
Summary:        Header files for picojson development
Group:          Development/Libraries
Provides:       %{name}-static = %{version}-%{release}

%description devel
Provide header file for %{name}.

%prep
%setup -qn %{name}-%{commit}

%build
echo "Nothing to do"

%check
make test

%install
mkdir -p %{buildroot}%{_includedir}
install -p -m 0644 picojson.h %{buildroot}%{_includedir}/picojson.h

%files devel
%{_includedir}/picojson.h
%doc LICENSE README.mkdn examples

%changelog
* Tue Jun 24 2014 Timothy St. Clair <tstclair@redhat.com> 1.1.0-1
- update per review

* Mon Jun 23 2014 Timothy St. Clair <tstclair@redhat.com> 1.0.0-1
- initial rpm

