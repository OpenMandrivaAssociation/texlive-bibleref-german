Name:		texlive-bibleref-german
Version:	21923
Release:	1
Summary:	German adaptation of bibleref
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/bibleref-german
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bibleref-german.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bibleref-german.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides translations and various formats for the
use of bibleref in German documents. The German naming of the
bible books complies with the 'Loccumer Richtlinien' (Locum
guidelines). In addition, the Vulgate (Latin bible) is
supported.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/bibleref-german/bibleref-german.sty
%doc %{_texmfdistdir}/doc/latex/bibleref-german/CHANGES
%doc %{_texmfdistdir}/doc/latex/bibleref-german/LIESMICH
%doc %{_texmfdistdir}/doc/latex/bibleref-german/README
%doc %{_texmfdistdir}/doc/latex/bibleref-german/bibleref-german-preamble.tex
%doc %{_texmfdistdir}/doc/latex/bibleref-german/bibleref-german-print.tex
%doc %{_texmfdistdir}/doc/latex/bibleref-german/bibleref-german-screen.tex
%doc %{_texmfdistdir}/doc/latex/bibleref-german/de-bibleref-german.pdf
%doc %{_texmfdistdir}/doc/latex/bibleref-german/de-bibleref-german.tex
%doc %{_texmfdistdir}/doc/latex/bibleref-german/en-bibleref-german.pdf
%doc %{_texmfdistdir}/doc/latex/bibleref-german/en-bibleref-german.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
