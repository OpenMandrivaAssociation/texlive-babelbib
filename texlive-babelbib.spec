Name:		texlive-babelbib
Version:	76790
Release:	1
Summary:	Multilingual bibliographies
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/biblio/bibtex/contrib/babelbib
License:	LPPL1
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babelbib.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babelbib.doc.r%{version}.tar.xz
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
%{_texmfdistdir}/bibtex/bst/babelbib
%{_texmfdistdir}/tex/latex/babelbib
%doc %{_texmfdistdir}/doc/bibtex/babelbib

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex doc %{buildroot}%{_texmfdistdir}
