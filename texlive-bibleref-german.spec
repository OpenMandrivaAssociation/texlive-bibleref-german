Name:		texlive-bibleref-german
Version:	1.0a
Release:	1
Summary:	German adaptation of bibleref
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/bibleref-german
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bibleref-german.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bibleref-german.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package provides translations and various formats for the
use of bibleref in German documents. The German naming of the
bible books complies with the 'Loccumer Richtlinien' (Locum
guidelines). In addition, the Vulgate (Latin bible) is
supported.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
