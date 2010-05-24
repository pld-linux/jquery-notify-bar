# TODO
# - make -demo package
Summary:	jQuery Notify Bar plugin
Name:		jquery-notify-bar
Version:	1.2.2
Release:	1
License:	MIT
Group:		Applications/WWW
Source0:	http://github.com/dknight/jQuery-Notify-bar/tarball/master?/notify-bar.tgz
# Source0-md5:	e6929d46a44fcad5559970b5fe6d7e3b
URL:		http://www.dmitri.me/blog/notify-bar/
BuildRequires:	js
BuildRequires:	rpmbuild(macros) > 1.268
BuildRequires:	unzip
BuildRequires:	yuicompressor
Requires:	jquery >= 1.3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir		%{_datadir}/jquery

%description
Simple plugin (basically it's not a plugin, but widget) to show notify
bar (like on Twitter’s webpage).

%prep
%setup -qc
mv *-jQuery-Notify-bar-*/* .

%build
install -d build

# compress .js
for js in *.js; do
	yuicompressor --charset UTF-8 $js -o build/$js
	js -C -f build/$js
done

# compress .css
for css in *.css; do
	# compress with yui to get rid of comments, etc
	yuicompressor --charset UTF-8 $css -o build/$css
done

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_appdir},%{_examplesdir}/%{name}-%{version}}
cp -a build/jquery.notifyBar.* $RPM_BUILD_ROOT%{_appdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.textile
%{_appdir}/jquery.*
