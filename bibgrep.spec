# TODO:
# - fix against home_etc
# - simply... finish it..
Summary:	Indexes and searches BibTeX files using Google-like queries
Summary(pl):	Indeksowanie i przeszukiwanie plików BibTeXa przy u¿yciu zapytañ w stylu Googli
Name:		bibgrep
Version:	0.51
Release:	0.1
License:	??
Group:		Applications
Source0:	http://dl.sourceforge.net/bibgrep/%{name}-src-%{version}.tgz
# Source0-md5:	e13320753a513a7c8ce91836375c3249
URL:		http://www.sourceforge.net/projects/bibgrep/
#BuildRequires:	btparse
BuildRequires:	ocaml
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Bibgrep indexes and efficiently searches BibTeX files. Its usage is
similar to the command grep and the queries use a Google-like syntax.
Bibgrep will create an index for each BibTeX file it touches, and keep
the result within "~/.bibgrep.idx" (by defaults). It watches the
modification date and the size of the original BibTeX file, and will
update (and delete) its index as needed.

%description -l pl
Bibgrep indeksuje i wydajnie przeszukuje pliki BibTeXa. U¿ycie go jest
podobne do polecenia grep, a polecenia wykorzystuj± sk³adniê w stylu
Googli. Bibgrep tworzy indeks dla ka¿dego przetwarzanego pliku BibTeXa
i utrzymuje wynik w ~/.bibgrep.idx (domy¶lnie). Kontroluje datê
modyfikacji i rozmiar oryginalnego pliku BibTeXa i uaktualnia (lub
kasuje) jego indeks w razie potrzeby.

%prep
%setup -q -T -c -a0

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man8}

install bibgrep $RPM_BUILD_ROOT%{_bindir}
install bibgrep.8 $RPM_BUILD_ROOT%{_mandir}/man8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man?/*
