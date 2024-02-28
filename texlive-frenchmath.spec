Name:		texlive-frenchmath
Version:	70163
Release:	1
Summary:	Typesetting mathematics according to French rules
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/frenchmath
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/frenchmath.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/frenchmath.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/frenchmath.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides: capital letters in roman (upright shape)
in mathematical mode according to French rule (can be
optionnally disabled), optionally lowercase Greek letters in
upright shape, correct spacing after commas and before a
semicolon in math mode, some useful macros and aliases for
symbols used in France: \infeg, \supeg, \paral, ... several
macros for writing french operator names like pgcd, ppcm, Card,
rg, Vect, ...

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/frenchmath
%{_texmfdistdir}/tex/latex/frenchmath
%doc %{_texmfdistdir}/doc/latex/frenchmath

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
