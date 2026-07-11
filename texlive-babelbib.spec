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
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package enables the user to generate multilingual bibliographies in
cooperation with babel. Two approaches are possible: Each citation may
be written in another language, or the whole bibliography can be typeset
in a language chosen by the user. In addition, the package supports
commands to change the typography of the bibliographies.

