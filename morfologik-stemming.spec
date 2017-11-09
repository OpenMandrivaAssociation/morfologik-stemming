%{?_javapackages_macros:%_javapackages_macros}

Name:          morfologik-stemming
Version:       2.0.1
Release:       6.1
Summary:       Morfologik stemming library
Group:         Development/Java
License:       BSD
URL:           http://morfologik.blogspot.com/
Source0:       https://github.com/morfologik/morfologik-stemming/archive/%{version}.tar.gz

BuildRequires: maven-local
BuildRequires: mvn(com.beust:jcommander)
BuildRequires: mvn(com.carrotsearch:hppc)
BuildRequires: mvn(com.google.guava:guava)
BuildRequires: mvn(commons-cli:commons-cli)
BuildRequires: mvn(commons-lang:commons-lang)
BuildRequires: mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires: mvn(org.sonatype.oss:oss-parent:pom:)

%if 0
# test deps
BuildRequires: mvn(com.carrotsearch:junit-benchmarks)
BuildRequires: mvn(org.hamcrest:hamcrest-core)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.easytesting:fest-assert-core:2.0M10)
%endif

BuildArch:     noarch

%description
Morfologik provides high quality lemmatisation for the Polish language,
along with tools for building and using byte-based finite state automata.

%package javadoc
Summary:       Javadoc for %{name}

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q
find . -name "*.class" -print -delete
find . -name "*.jar" -print -delete

chmod 644 README.txt
# Convert from dos to unix line ending
for file in CHANGES.txt CONTRIBUTING.txt README.txt LICENSE.txt; do
 sed -i.orig 's|\r||g' $file
 touch -r $file.orig $file
 rm $file.orig
done

%pom_add_dep org.hamcrest:hamcrest-core::test morfologik-tools
%pom_remove_plugin com.carrotsearch.randomizedtesting:junit4-maven-plugin
%pom_remove_plugin de.thetaphi:forbiddenapis
%pom_remove_plugin :maven-javadoc-plugin

# Remove classpath from manifest file
%pom_xpath_set pom:addClasspath false morfologik-tools
# Unwanted task
%pom_remove_plugin :maven-assembly-plugin morfologik-tools

%pom_change_dep :morfologik-polish ::'${project.version}' morfologik-speller

%build
# Test skipped for unavailable test deps
%mvn_build -f -- -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

%files -f .mfiles
%doc CHANGES.txt CONTRIBUTING.txt README.txt
%doc LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%changelog
* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jun 29 2016 gil cattaneo <puntogil@libero.it> 2.0.1-4
- add missing build requires

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 21 2016 gil cattaneo <puntogil@libero.it> 2.0.1-2
- use pom macros
- disable classapth in the morfologik-tools manifest file
- remove duplicate files
- fix BRs list

* Thu Jan 21 2016 Alexander Kurtakov <akurtako@redhat.com> 2.0.1-1
- Update to 2.0.1

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Feb 10 2015 gil cattaneo <puntogil@libero.it> 1.8.3-3
- introduce license macro

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Jan 11 2014 gil cattaneo <puntogil@libero.it> 1.8.3-1
- update to 1.8.3

* Sun Dec 29 2013 gil cattaneo <puntogil@libero.it> 1.8.2-1
- update to 1.8.2

* Thu Dec 05 2013 gil cattaneo <puntogil@libero.it> 1.8.1-1
- update to 1.8.1

* Mon Oct 21 2013 gil cattaneo <puntogil@libero.it> 1.7.2-1
- update to 1.7.2

* Sun Aug 25 2013 gil cattaneo <puntogil@libero.it> 1.5.5-1
- initial rpm

