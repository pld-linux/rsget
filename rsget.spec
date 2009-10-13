#
Summary:	A console-based RapidShare files downloader
Summary(pl.UTF-8):	Konsolowy skrypt do pobierania plików z RapidShare
Name:		rsget
Version:	20091013
Release:	1
License:	WTFPL
Group:		Applications
Source0:	http://jachacy.mm5.pl/pub/%{name}.sh
# Source0-md5:	f783eee9d3fba101289d4213ed383217
Source1:	http://sam.zoy.org/wtfpl/COPYING
# Source1-md5:	65a4a3db35cb4ac63386bdc70687d1e5
Patch0:		%{name}.patch
URL:		http://jachacy.jogger.pl/2008/07/03/rsget-sh-skrypt-automatyzujacy-pobieranie-z-rapidshare-com/
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
%patch0

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install rsget.sh $RPM_BUILD_ROOT%{_bindir}/rsget

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/rsget
%doc COPYING
