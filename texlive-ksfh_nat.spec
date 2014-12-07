# revision 24825
# category Package
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-ksfh_nat
Version:	20111217
Release:	9
Summary:	TeXLive ksfh_nat package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ksfh_nat.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
TeXLive ksfh_nat package.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/bibtex/bst/ksfh_nat/ksfh_nat.bst

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20111217-2
+ Revision: 753050
- Rebuild to reduce used resources

* Sat Dec 17 2011 Paulo Andrade <pcpa@mandriva.com.br> 20111217-1
+ Revision: 743254
- texlive-ksfh_nat

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20111103-1
+ Revision: 718787
- texlive-ksfh_nat
- texlive-ksfh_nat
- texlive-ksfh_nat
- texlive-ksfh_nat

