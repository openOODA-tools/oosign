Name:           oosign
Version:        0.1.0
Release:        1%{?dist}
Summary:        Signs software packages, install scripts, and releases with detached signatures.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/oosign
Source0:        oosign-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
oosign is a sovereign, capability-bounded ARTIFACT SIGNER written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/oosign
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/oosign-uninstall

%files
/usr/bin/oosign
/usr/bin/oosign-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding
