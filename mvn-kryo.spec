#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-kryo
Version  : 4.0.2
Release  : 3
URL      : https://github.com/EsotericSoftware/kryo/archive/kryo-parent-4.0.2.tar.gz
Source0  : https://github.com/EsotericSoftware/kryo/archive/kryo-parent-4.0.2.tar.gz
Source1  : https://repo.maven.apache.org/maven2/com/esotericsoftware/kryo-parent/4.0.2/kryo-parent-4.0.2.pom
Source2  : https://repo1.maven.org/maven2/com/esotericsoftware/kryo-shaded/4.0.2/kryo-shaded-4.0.2.jar
Source3  : https://repo1.maven.org/maven2/com/esotericsoftware/kryo-shaded/4.0.2/kryo-shaded-4.0.2.pom
Source4  : https://repo1.maven.org/maven2/com/esotericsoftware/kryo/kryo/2.20/kryo-2.20.jar
Source5  : https://repo1.maven.org/maven2/com/esotericsoftware/kryo/kryo/2.20/kryo-2.20.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause
Requires: mvn-kryo-data = %{version}-%{release}
Requires: mvn-kryo-license = %{version}-%{release}

%description
![KryoNet](https://raw.github.com/wiki/EsotericSoftware/kryo/images/logo.jpg)
[![Build Status](https://jenkins.inoio.de/buildStatus/icon?job=kryo&foo=bar)](https://jenkins.inoio.de/job/kryo/)
[![Maven Central](https://maven-badges.herokuapp.com/maven-central/com.esotericsoftware/kryo/badge.svg)](http://search.maven.org/#search%7Cga%7C1%7Cg%3A%22com.esotericsoftware%22%20AND%20a%3Akryo)
[![Join the chat at https://gitter.im/EsotericSoftware/kryo](https://badges.gitter.im/EsotericSoftware/kryo.svg)](https://gitter.im/EsotericSoftware/kryo)

%package data
Summary: data components for the mvn-kryo package.
Group: Data

%description data
data components for the mvn-kryo package.


%package license
Summary: license components for the mvn-kryo package.
Group: Default

%description license
license components for the mvn-kryo package.


%prep
%setup -q -n kryo-kryo-parent-4.0.2

%build

%install
mkdir -p %{buildroot}/usr/share/package-licenses/mvn-kryo
cp license.txt %{buildroot}/usr/share/package-licenses/mvn-kryo/license.txt
mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/esotericsoftware/kryo-parent/4.0.2
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/com/esotericsoftware/kryo-parent/4.0.2/kryo-parent-4.0.2.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/esotericsoftware/kryo-shaded/4.0.2
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/com/esotericsoftware/kryo-shaded/4.0.2/kryo-shaded-4.0.2.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/esotericsoftware/kryo-shaded/4.0.2
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/com/esotericsoftware/kryo-shaded/4.0.2/kryo-shaded-4.0.2.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/esotericsoftware/kryo/kryo/2.20
cp %{SOURCE4} %{buildroot}/usr/share/java/.m2/repository/com/esotericsoftware/kryo/kryo/2.20/kryo-2.20.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/esotericsoftware/kryo/kryo/2.20
cp %{SOURCE5} %{buildroot}/usr/share/java/.m2/repository/com/esotericsoftware/kryo/kryo/2.20/kryo-2.20.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/com/esotericsoftware/kryo-parent/4.0.2/kryo-parent-4.0.2.pom
/usr/share/java/.m2/repository/com/esotericsoftware/kryo-shaded/4.0.2/kryo-shaded-4.0.2.jar
/usr/share/java/.m2/repository/com/esotericsoftware/kryo-shaded/4.0.2/kryo-shaded-4.0.2.pom
/usr/share/java/.m2/repository/com/esotericsoftware/kryo/kryo/2.20/kryo-2.20.jar
/usr/share/java/.m2/repository/com/esotericsoftware/kryo/kryo/2.20/kryo-2.20.pom

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mvn-kryo/license.txt
