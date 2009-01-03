%define name python-twisted-conch
%define version 8.2.0
%define release %mkrel 1

%define progname TwistedConch

Summary:        An SSH and SFTP protocol implementation together with clients and servers
Name:           %name
Version:        %version
Release:        %release
Source0:        http://tmrc.mit.edu/mirror/twisted/Conch/8.1/%{progname}-%{version}.tar.bz2
License:        MIT
Group:          Development/Python
URL:            http://twistedmatrix.com/projects/conch
BuildRoot:      %{_tmppath}/%{name}-buildroot
BuildRequires:	python-devel python-twisted-core
Requires:       python-twisted-core

%description
Conch is an SSHv2 implementation written in Python. SSH is a protocol designed
to allow remote access to shells and commands, but it is generic enough to
allow everything from TCP forwarding to generic filesystem access. Since
conch is written in Python, it interfaces well with other Python projects,
such as Imagination.
Conch also includes a implementations of the telnet and vt102 protocols, as
well as support for rudamentary line editing behaviors.

A new implementation of Twisted's Manhole application is also included,
featuring server-side input history and interactive syntax coloring.

%prep
%setup -q -n %{progname}-%version

%build
%__python setup.py build

%install
%__rm -rf %buildroot
%__python setup.py install --root  %buildroot --install-purelib=%py_platsitedir

%__install -d                      %buildroot%_mandir/man1
%__install -m 644 doc/man/*.1      %buildroot%_mandir/man1

%clean
%__rm -rf %buildroot

%files
%defattr(0755,root,root,0755)
%_bindir/*
%defattr(0644,root,root,0755)
%doc LICENSE README doc/*
%py_platsitedir/twisted/conch
%py_platsitedir/twisted/plugins/*
%py_platsitedir/*.egg-info
%_mandir/man1/*


