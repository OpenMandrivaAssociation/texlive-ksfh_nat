%global tl_name ksfh_nat
%global tl_revision 76790

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1
Release:	%{tl_revision}.1
Summary:	BibTeX style for KSFH Munich
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/biblio/bibtex/contrib/ksfh_nat
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ksfh_nat.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package supports bibliographies as standard for KSFH (Katholische
Stiftungsfachhochschule) Munich. BibTeX entries in article, book,
inbook, incollection and misc formats are supported.

