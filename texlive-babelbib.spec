%global tl_name babelbib
%global tl_revision 76790

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.34
Release:	%{tl_revision}.1
Summary:	Multilingual bibliographies
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/biblio/bibtex/contrib/babelbib
License:	lppl1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/babelbib.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/babelbib.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package enables the user to generate multilingual bibliographies in
cooperation with babel. Two approaches are possible: Each citation may
be written in another language, or the whole bibliography can be typeset
in a language chosen by the user. In addition, the package supports
commands to change the typography of the bibliographies.

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
%dir %{_datadir}/texmf-dist/bibtex
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/bibtex/bst
%dir %{_datadir}/texmf-dist/doc/bibtex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/bibtex/bst/babelbib
%dir %{_datadir}/texmf-dist/doc/bibtex/babelbib
%dir %{_datadir}/texmf-dist/tex/latex/babelbib
%{_datadir}/texmf-dist/bibtex/bst/babelbib/bababbr3-fl.bst
%{_datadir}/texmf-dist/bibtex/bst/babelbib/bababbr3-lf.bst
%{_datadir}/texmf-dist/bibtex/bst/babelbib/bababbr3.bst
%{_datadir}/texmf-dist/bibtex/bst/babelbib/bababbrv-fl.bst
%{_datadir}/texmf-dist/bibtex/bst/babelbib/bababbrv-lf.bst
%{_datadir}/texmf-dist/bibtex/bst/babelbib/bababbrv.bst
%{_datadir}/texmf-dist/bibtex/bst/babelbib/babalpha-fl.bst
%{_datadir}/texmf-dist/bibtex/bst/babelbib/babalpha-lf.bst
%{_datadir}/texmf-dist/bibtex/bst/babelbib/babalpha.bst
%{_datadir}/texmf-dist/bibtex/bst/babelbib/babamspl.bst
%{_datadir}/texmf-dist/bibtex/bst/babelbib/babplai3-fl.bst
%{_datadir}/texmf-dist/bibtex/bst/babelbib/babplai3-lf.bst
%{_datadir}/texmf-dist/bibtex/bst/babelbib/babplai3.bst
%{_datadir}/texmf-dist/bibtex/bst/babelbib/babplain-fl.bst
%{_datadir}/texmf-dist/bibtex/bst/babelbib/babplain-lf.bst
%{_datadir}/texmf-dist/bibtex/bst/babelbib/babplain.bst
%{_datadir}/texmf-dist/bibtex/bst/babelbib/babunsrt-fl.bst
%{_datadir}/texmf-dist/bibtex/bst/babelbib/babunsrt-lf.bst
%{_datadir}/texmf-dist/bibtex/bst/babelbib/babunsrt.bst
%doc %{_datadir}/texmf-dist/doc/bibtex/babelbib/ChangeLog
%doc %{_datadir}/texmf-dist/doc/bibtex/babelbib/Makefile
%doc %{_datadir}/texmf-dist/doc/bibtex/babelbib/README
%doc %{_datadir}/texmf-dist/doc/bibtex/babelbib/babelbib.dtx
%doc %{_datadir}/texmf-dist/doc/bibtex/babelbib/babelbib.ins
%doc %{_datadir}/texmf-dist/doc/bibtex/babelbib/babelbib.pdf
%doc %{_datadir}/texmf-dist/doc/bibtex/babelbib/babelbibtest.bib
%doc %{_datadir}/texmf-dist/doc/bibtex/babelbib/babelbibtest.tex
%doc %{_datadir}/texmf-dist/doc/bibtex/babelbib/getversion.tex
%doc %{_datadir}/texmf-dist/doc/bibtex/babelbib/tugboat-babelbib.pdf
%{_datadir}/texmf-dist/tex/latex/babelbib/afrikaans.bdf
%{_datadir}/texmf-dist/tex/latex/babelbib/babelbib.sty
%{_datadir}/texmf-dist/tex/latex/babelbib/bahasa.bdf
%{_datadir}/texmf-dist/tex/latex/babelbib/catalan.bdf
%{_datadir}/texmf-dist/tex/latex/babelbib/croatian.bdf
%{_datadir}/texmf-dist/tex/latex/babelbib/czech.bdf
%{_datadir}/texmf-dist/tex/latex/babelbib/danish.bdf
%{_datadir}/texmf-dist/tex/latex/babelbib/dutch.bdf
%{_datadir}/texmf-dist/tex/latex/babelbib/english.bdf
%{_datadir}/texmf-dist/tex/latex/babelbib/esperanto.bdf
%{_datadir}/texmf-dist/tex/latex/babelbib/finnish.bdf
%{_datadir}/texmf-dist/tex/latex/babelbib/french.bdf
%{_datadir}/texmf-dist/tex/latex/babelbib/galician.bdf
%{_datadir}/texmf-dist/tex/latex/babelbib/german.bdf
%{_datadir}/texmf-dist/tex/latex/babelbib/greek.bdf
%{_datadir}/texmf-dist/tex/latex/babelbib/italian.bdf
%{_datadir}/texmf-dist/tex/latex/babelbib/norsk.bdf
%{_datadir}/texmf-dist/tex/latex/babelbib/portuguese.bdf
%{_datadir}/texmf-dist/tex/latex/babelbib/romanian.bdf
%{_datadir}/texmf-dist/tex/latex/babelbib/russian.bdf
%{_datadir}/texmf-dist/tex/latex/babelbib/serbian.bdf
%{_datadir}/texmf-dist/tex/latex/babelbib/spanish.bdf
%{_datadir}/texmf-dist/tex/latex/babelbib/swedish.bdf
%{_datadir}/texmf-dist/tex/latex/babelbib/turkish.bdf
