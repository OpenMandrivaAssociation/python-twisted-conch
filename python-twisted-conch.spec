%define mainver %(echo %{version} | sed -e 's/\\([0-9]*\\.[0-9]*\\)\\.[0-9]*/\\1/')

%define progname TwistedConch

# There is no debug here, but can't build as noarch,
# since some 'twisted' modules are arch-dependent and all these modules
# should be located in the same place
%define debug_package %{nil}

Summary:	An SSH and SFTP protocol implementation together with clients and servers
Name:		python-twisted-conch
Version:	13.0.0
Release:	2
License:	MIT
Group:		Development/Python
Url:		http://twistedmatrix.com/projects/conch
Source0:	http://twistedmatrix.com/Releases/Conch/%{mainver}/TwistedConch-%{version}.tar.bz2
BuildRequires:	python-twisted-core
BuildRequires:	pkgconfig(python)
Requires:	python-twisted-core
Requires:	pyasn1

%description
Conch is an SSHv2 implementation written in Python.
SSH is a protocol designed to allow remote access
to shells and commands, but it is generic enough to allow
everything from TCP forwarding to generic filesystem access.
Since Conch is written in Python, it interfaces well with
other Python projects such as Imagination.
Conch also includes a implementations of the telnet and vt102
protocols, as well as support for rudamentary line editing behaviors.
A new implementation of Twisted's Manhole application is also included,
featuring server-side input history and interactive syntax coloring.

%prep
%setup -qn %{progname}-%{version}

%build
%__python setup.py build

%install
%__python setup.py install --root=%{buildroot} --install-purelib=%{py_platsitedir}

%__install -d %{buildroot}%{_mandir}/man1
%__install -m 644 doc/man/*.1 %{buildroot}%{_mandir}/man1

%files
%defattr(0755,root,root,0755)
%{_bindir}/*
%defattr(0644,root,root,0755)
%doc LICENSE README doc/*
%dir %{py_platsitedir}/twisted/conch
%{py_platsitedir}/twisted/conch/*
%{py_platsitedir}/twisted/plugins/*
%{py_platsitedir}/*.egg-info
%{_mandir}/man1/*

