#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : totem
Version  : 43.0
Release  : 32
URL      : https://download.gnome.org/sources/totem/43/totem-43.0.tar.xz
Source0  : https://download.gnome.org/sources/totem/43/totem-43.0.tar.xz
Summary  : Totem Movie Player plugin API
Group    : Development/Tools
License  : GPL-2.0
Requires: grilo
Requires: grilo-plugins
BuildRequires : appstream-glib
BuildRequires : buildreq-gnome
BuildRequires : buildreq-meson
BuildRequires : docbook-xml
BuildRequires : glibc-bin
BuildRequires : gobject-introspection-dev
BuildRequires : grilo-dev
BuildRequires : grilo-plugins
BuildRequires : gsettings-desktop-schemas
BuildRequires : gst-plugins-good
BuildRequires : intltool
BuildRequires : itstool
BuildRequires : libpeas-dev
BuildRequires : libxslt-bin
BuildRequires : pkgconfig(clutter-1.0)
BuildRequires : pkgconfig(clutter-gst-3.0)
BuildRequires : pkgconfig(clutter-gtk-1.0)
BuildRequires : pkgconfig(gdk-3.0)
BuildRequires : pkgconfig(gdk-pixbuf-2.0)
BuildRequires : pkgconfig(gio-2.0)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gnome-desktop-3.0)
BuildRequires : pkgconfig(gsettings-desktop-schemas)
BuildRequires : pkgconfig(gstreamer-1.0)
BuildRequires : pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires : pkgconfig(gstreamer-tag-1.0)
BuildRequires : pkgconfig(gthread-2.0)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(libnautilus-extension)
BuildRequires : pkgconfig(libxml-2.0)
BuildRequires : pkgconfig(pygobject-3.0)
BuildRequires : totem-pl-parser-dev

%description
_|_ __|_ _ ._ _
|_(_)|_(/_| | |
Totem is movie player for the GNOME desktop based on GStreamer.
It features a playlist, a full-screen mode, seek and volume controls,
as well as complete keyboard navigation.

%prep
%setup -q -n totem-43.0
cd %{_builddir}/totem-43.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1663965948
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
# Tests require some glib schemas to be initialized
target=$HOME/.local/share/glib-2.0/schemas
mkdir -p $target
glib-compile-schemas --targetdir=$target /usr/share/glib-2.0/schemas
export XDG_DATA_DIRS="$HOME/.local/share${XDG_DATA_DIRS:+:$XDG_DATA_DIRS}"
meson test -C builddir || :

%install
mkdir -p %{buildroot}/usr/share/package-licenses/totem
cp %{_builddir}/totem-%{version}/license_change %{buildroot}/usr/share/package-licenses/totem/5fda7ef0ea822add58f4d3769f593d1c8b6d2df7 || :
DESTDIR=%{buildroot} ninja -C builddir install

%files
%defattr(-,root,root,-)
