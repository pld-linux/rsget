# TODO:
# - /home/users/blues/.rsget-mod/common.sh: line 65: /usr/bin/rsget: Brak dost�pu
#   .rsget-mod/common.sh is downloaded on first run.
#
Summary:	A console-based RapidShare files downloader
Summary(pl.UTF-8):	Konsolowy skrypt do pobierania plików z RapidShare
Name:		rsget
Version:	0.6
Release:	1
Epoch:		1
License:	WTFPL
Group:		Applications
Source0:	http://rs.nerdblog.pl/stable/latest/%{name}-mod.sh
# Source0-md5:	d768c0e3adeb13db020a201b44a01c93
Source1:	http://sam.zoy.org/wtfpl/COPYING
# Source1-md5:	65a4a3db35cb4ac63386bdc70687d1e5
URL:		http://rs.nerdblog.pl/
Requires:	bash
Requires:	grep
Requires:	sed
Requires:	wget
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
rsget is a console-based RapidShare files downloader.

%description -l pl.UTF-8
rsget jest konsolowym skryptem automatyzującym pobieranie plików z
RapidShare.

%prep
%setup -q -c -T
cp %{SOURCE0} .
cp %{SOURCE1} .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install %{name}-mod.sh $RPM_BUILD_ROOT%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING
%attr(755,root,root) %{_bindir}/%{name}
