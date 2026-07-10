%global tl_name bibleref-german
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0a
Release:	%{tl_revision}.1
Summary:	German adaptation of bibleref
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/bibleref-german
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bibleref-german.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bibleref-german.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides translations and various formats for the use of
bibleref in German documents. The German naming of the bible books
complies with the 'Loccumer Richtlinien' (Locum guidelines). In
addition, the Vulgate (Latin bible) is supported.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/bibleref-german
%dir %{_datadir}/texmf-dist/tex/latex/bibleref-german
%doc %{_datadir}/texmf-dist/doc/latex/bibleref-german/CHANGES
%doc %{_datadir}/texmf-dist/doc/latex/bibleref-german/LIESMICH
%doc %{_datadir}/texmf-dist/doc/latex/bibleref-german/README
%doc %{_datadir}/texmf-dist/doc/latex/bibleref-german/bibleref-german-preamble.tex
%doc %{_datadir}/texmf-dist/doc/latex/bibleref-german/bibleref-german-print.tex
%doc %{_datadir}/texmf-dist/doc/latex/bibleref-german/bibleref-german-screen.tex
%doc %{_datadir}/texmf-dist/doc/latex/bibleref-german/de-bibleref-german.pdf
%doc %{_datadir}/texmf-dist/doc/latex/bibleref-german/de-bibleref-german.tex
%doc %{_datadir}/texmf-dist/doc/latex/bibleref-german/en-bibleref-german.pdf
%doc %{_datadir}/texmf-dist/doc/latex/bibleref-german/en-bibleref-german.tex
%{_datadir}/texmf-dist/tex/latex/bibleref-german/bibleref-german.sty
