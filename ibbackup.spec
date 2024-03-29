Summary:	InnoDB Hot Backup
Summary(pl.UTF-8):	Gorący backup InnoDB
Name:		ibbackup
Version:	3.0.0
Release:	4
License:	restricted (http://www.innodb.com/hotbackuplicense.php)
Group:		Applications/Databases
# Source0Download:	http://www.innodb.com/order.php
Source0:	%{name}
# NoSource0-md5:	e0d46c6fb2627ce13d540d4efa935551
NoSource:	0
Source1:	%{name}.conf
URL:		http://www.innodb.com/
Conflicts:	innobackup < 1.4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
InnoDB Hot Backup is the ideal solution for online backups of InnoDB
tables in MySQL - and for setting up replication. It allows you to
back up a running InnoDB database under MySQL without setting any
locks or disturbing normal database processing. You get a consistent
copy of your database, as if the copy were taken at a precise point in
time. InnoDB Hot Backup is also the ideal method of setting up new
slaves if you use the MySQL replication on InnoDB tables.

The program documentation is available at
<http://www.innodb.com/manual.php>.

%description -l pl.UTF-8
InnoDB Hot Backup to idealne rozwiązanie dla tworzenia w czasie
rzeczywistym kopii zapasowych tabel w MySQL oraz zestawiania
replikacji. Umożliwia tworzenie kopii zapasowych działającej bazy
danych InnoDB pod MySQL-em bez ustawiania żadnych blokad czy
przeszkadzania w normalnym przetwarzaniu baz danych. Otrzymuje się
spójną kopię bazy danych, tak, jakby była wykonana w dokładnym punkcie
w czasie. InnoDB Hot Backup to także idealna metoda zestawiania nowych
serwerów podrzędnych w przypadku używania replikacji MySQL-a na
tabelach InnoDB.

Dokumentacja programu dostępna jest pod
<http://www.innodb.com/manual.php>.

%prep
%setup -q -c -T
cp %{SOURCE0} %{name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_sysconfdir}}
install %{name} $RPM_BUILD_ROOT%{_bindir}/ibbackup
install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.conf

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ibbackup
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/ibbackup.conf
