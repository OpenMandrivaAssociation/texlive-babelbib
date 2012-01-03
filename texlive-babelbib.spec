# revision 15878
# category Package
# catalog-ctan /biblio/bibtex/contrib/babelbib
# catalog-date 2009-10-11 21:12:19 +0200
# catalog-license lppl1
# catalog-version 1.29
Name:		texlive-babelbib
Version:	1.29
Release:	2
Summary:	Multilingual bibliographies
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/biblio/bibtex/contrib/babelbib
License:	LPPL1
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babelbib.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babelbib.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babelbib.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package enables to generate multilingual bibliographies in
cooperation with babel. Two approaches are possible: Each
citation may be written in another language, or the whole
bibliography can be typeset in a language chosen by the user.
In addition, the package supports commands to change the
typography of the bibliographies.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/bibtex/bst/babelbib/bababbr3-fl.bst
%{_texmfdistdir}/bibtex/bst/babelbib/bababbr3-lf.bst
%{_texmfdistdir}/bibtex/bst/babelbib/bababbr3.bst
%{_texmfdistdir}/bibtex/bst/babelbib/bababbrv-fl.bst
%{_texmfdistdir}/bibtex/bst/babelbib/bababbrv-lf.bst
%{_texmfdistdir}/bibtex/bst/babelbib/bababbrv.bst
%{_texmfdistdir}/bibtex/bst/babelbib/babalpha-fl.bst
%{_texmfdistdir}/bibtex/bst/babelbib/babalpha-lf.bst
%{_texmfdistdir}/bibtex/bst/babelbib/babalpha.bst
%{_texmfdistdir}/bibtex/bst/babelbib/babalpha2.bst
%{_texmfdistdir}/bibtex/bst/babelbib/babamspl.bst
%{_texmfdistdir}/bibtex/bst/babelbib/babplai3-fl.bst
%{_texmfdistdir}/bibtex/bst/babelbib/babplai3-lf.bst
%{_texmfdistdir}/bibtex/bst/babelbib/babplai3.bst
%{_texmfdistdir}/bibtex/bst/babelbib/babplain-fl.bst
%{_texmfdistdir}/bibtex/bst/babelbib/babplain-lf.bst
%{_texmfdistdir}/bibtex/bst/babelbib/babplain-neu.bst
%{_texmfdistdir}/bibtex/bst/babelbib/babplain-orig.bst
%{_texmfdistdir}/bibtex/bst/babelbib/babplain-spielen.bst
%{_texmfdistdir}/bibtex/bst/babelbib/babplain.bst
%{_texmfdistdir}/bibtex/bst/babelbib/babunsrt-fl.bst
%{_texmfdistdir}/bibtex/bst/babelbib/babunsrt-lf.bst
%{_texmfdistdir}/bibtex/bst/babelbib/babunsrt.bst
%{_texmfdistdir}/tex/latex/babelbib/afrikaans.bdf
%{_texmfdistdir}/tex/latex/babelbib/babelbib.sty
%{_texmfdistdir}/tex/latex/babelbib/bahasa.bdf
%{_texmfdistdir}/tex/latex/babelbib/catalan.bdf
%{_texmfdistdir}/tex/latex/babelbib/danish.bdf
%{_texmfdistdir}/tex/latex/babelbib/dutch.bdf
%{_texmfdistdir}/tex/latex/babelbib/english.bdf
%{_texmfdistdir}/tex/latex/babelbib/esperanto.bdf
%{_texmfdistdir}/tex/latex/babelbib/finnish.bdf
%{_texmfdistdir}/tex/latex/babelbib/french.bdf
%{_texmfdistdir}/tex/latex/babelbib/french2.bdf
%{_texmfdistdir}/tex/latex/babelbib/galician.bdf
%{_texmfdistdir}/tex/latex/babelbib/german.bdf
%{_texmfdistdir}/tex/latex/babelbib/greek.bdf
%{_texmfdistdir}/tex/latex/babelbib/italian.bdf
%{_texmfdistdir}/tex/latex/babelbib/norsk.bdf
%{_texmfdistdir}/tex/latex/babelbib/portuguese.bdf
%{_texmfdistdir}/tex/latex/babelbib/russian.bdf
%{_texmfdistdir}/tex/latex/babelbib/spanish.bdf
%{_texmfdistdir}/tex/latex/babelbib/swedish.bdf
%doc %{_texmfdistdir}/doc/latex/babelbib/ChangeLog
%doc %{_texmfdistdir}/doc/latex/babelbib/README
%doc %{_texmfdistdir}/doc/latex/babelbib/babelbib.pdf
%doc %{_texmfdistdir}/doc/latex/babelbib/babelbibtest.bib
%doc %{_texmfdistdir}/doc/latex/babelbib/babelbibtest.tex
%doc %{_texmfdistdir}/doc/latex/babelbib/tugboat-babelbib.pdf
#- source
%doc %{_texmfdistdir}/source/latex/babelbib/Makefile
%doc %{_texmfdistdir}/source/latex/babelbib/babelbib.dtx
%doc %{_texmfdistdir}/source/latex/babelbib/babelbib.ins
%doc %{_texmfdistdir}/source/latex/babelbib/babelbib.xml
%doc %{_texmfdistdir}/source/latex/babelbib/getversion.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex doc source %{buildroot}%{_texmfdistdir}
