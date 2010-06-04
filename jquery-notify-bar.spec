# TODO
# - make -demo package
%define		plugin	notify-bar
Summary:	jQuery Notify Bar plugin
Name:		jquery-%{plugin}
Version:	1.2.2
Release:	2
License:	MIT
Group:		Applications/WWW
Source0:	http://github.com/dknight/jQuery-Notify-bar/tarball/master?/%{plugin}.tgz
# Source0-md5:	e6929d46a44fcad5559970b5fe6d7e3b
URL:		http://www.dmitri.me/blog/notify-bar/
BuildRequires:	js
BuildRequires:	rpmbuild(macros) >= 1.268
BuildRequires:	unzip
BuildRequires:	yuicompressor
Requires:	jquery >= 1.3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir	%{_datadir}/jquery/%{plugin}

%description
Simple plugin (basically it's not a plugin, but widget) to show notify
bar (like on Twitter’s webpage).

%prep
%setup -qc
mv *-jQuery-Notify-bar-*/* .

%build
install -d build

# compress .js
yuicompressor --charset UTF-8 jquery.notifyBar.js -o build/notifyBar.js
js -C -f build/notifyBar.js

# compress .css
yuicompressor --charset UTF-8 jquery.notifyBar.css -o build/notifyBar.css

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_appdir},%{_examplesdir}/%{name}-%{version}}
cp -a build/* $RPM_BUILD_ROOT%{_appdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.textile
%{_appdir}
