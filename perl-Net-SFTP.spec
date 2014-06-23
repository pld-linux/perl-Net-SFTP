#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Net
%define		pnam	SFTP
Summary:	Net::SFTP - Secure File Transfer Protocol client
Summary(pl.UTF-8):	Net::SFTP - klient protokołu SFTP (Secure File Transfer Protocol)
Name:		perl-Net-SFTP
Version:	0.10
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	8383eb0839178cab8cbfe619b232b8c0
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Net-SSH-Perl >= 1.24
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net::SFTP is a pure-Perl implementation of the Secure File Transfer
Protocol (SFTP) - file transfer built on top of the SSH protocol.
Net::SFTP uses Net::SSH::Perl to build a secure, encrypted tunnel
through which files can be transferred and managed. It provides a
subset of the commands listed in the SSH File Transfer Protocol IETF
draft, which can be found at
http://www.openssh.com/txt/draft-ietf-secsh-filexfer-00.txt .

%description -l pl.UTF-8
Net::SFTP to czysto perlowa implementacja protokołu SFTP (Secure File
Transfer Protocol) - przesyłania plików w oparciu o protokół SSH.
Net::SFTP używa Net::SSH::Perl do utworzenia bezpiecznego,
szyfrowanego tunelu, przez który można przesyłać pliki i zarządzać
nimi. Udostępnia podzbiór poleceń podanych w szkicu IETF "SSH File
Transfer Protocol", dostępnym pod adresem
http://www.openssh.com/txt/draft-ietf-secsh-filexfer-00.txt .

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a eg/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README ToDo
%{perl_vendorlib}/%{pdir}/*.pm
%{perl_vendorlib}/%{pdir}/%{pnam}
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
