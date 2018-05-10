#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : totem
Version  : 3.26.0
Release  : 8
URL      : https://download.gnome.org/sources/totem/3.26/totem-3.26.0.tar.xz
Source0  : https://download.gnome.org/sources/totem/3.26/totem-3.26.0.tar.xz
Summary  : Totem Movie Player plugin API
Group    : Development/Tools
License  : GPL-2.0
Requires: totem-bin
Requires: totem-data
Requires: totem-lib
Requires: totem-doc
Requires: totem-locales
Requires: grilo
Requires: grilo-plugins
BuildRequires : docbook-xml
BuildRequires : glibc-bin
BuildRequires : gobject-introspection-dev
BuildRequires : grilo-dev
BuildRequires : grilo-plugins
BuildRequires : gst-plugins-good
BuildRequires : intltool
BuildRequires : itstool
BuildRequires : libpeas-dev
BuildRequires : libxslt-bin
BuildRequires : meson
BuildRequires : ninja
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
BuildRequires : pylint
BuildRequires : python3
BuildRequires : totem-pl-parser-dev

%description
_|_ __|_ _ ._ _
|_(_)|_(/_| | |
Totem is movie player for the GNOME desktop based on GStreamer.
It features a playlist, a full-screen mode, seek and volume controls,
as well as complete keyboard navigation.

%package bin
Summary: bin components for the totem package.
Group: Binaries
Requires: totem-data

%description bin
bin components for the totem package.


%package data
Summary: data components for the totem package.
Group: Data

%description data
data components for the totem package.


%package dev
Summary: dev components for the totem package.
Group: Development
Requires: totem-lib
Requires: totem-bin
Requires: totem-data
Provides: totem-devel

%description dev
dev components for the totem package.


%package doc
Summary: doc components for the totem package.
Group: Documentation

%description doc
doc components for the totem package.


%package lib
Summary: lib components for the totem package.
Group: Libraries
Requires: totem-data

%description lib
lib components for the totem package.


%package locales
Summary: locales components for the totem package.
Group: Default

%description locales
locales components for the totem package.


%prep
%setup -q -n totem-3.26.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1517708087
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --prefix /usr --buildtype=plain -Denable-vala=no builddir
ninja -v -C builddir

%install
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang totem

%files
%defattr(-,root,root,-)
/usr/lib64/totem/plugins/apple-trailers/apple-trailers.plugin
/usr/lib64/totem/plugins/autoload-subtitles/autoload-subtitles.plugin
/usr/lib64/totem/plugins/brasero-disc-recorder/brasero-disc-recorder.plugin
/usr/lib64/totem/plugins/dbus/__pycache__/dbusservice.cpython-36.pyc
/usr/lib64/totem/plugins/dbus/dbusservice.plugin
/usr/lib64/totem/plugins/dbus/dbusservice.py
/usr/lib64/totem/plugins/gromit/gromit.plugin
/usr/lib64/totem/plugins/im-status/totem-im-status.plugin
/usr/lib64/totem/plugins/media-player-keys/media-player-keys.plugin
/usr/lib64/totem/plugins/ontop/ontop.plugin
/usr/lib64/totem/plugins/opensubtitles/__pycache__/hash.cpython-36.pyc
/usr/lib64/totem/plugins/opensubtitles/__pycache__/opensubtitles.cpython-36.pyc
/usr/lib64/totem/plugins/opensubtitles/hash.py
/usr/lib64/totem/plugins/opensubtitles/opensubtitles.plugin
/usr/lib64/totem/plugins/opensubtitles/opensubtitles.py
/usr/lib64/totem/plugins/opensubtitles/opensubtitles.ui
/usr/lib64/totem/plugins/properties/movie-properties.plugin
/usr/lib64/totem/plugins/pythonconsole/__pycache__/console.cpython-36.pyc
/usr/lib64/totem/plugins/pythonconsole/__pycache__/pythonconsole.cpython-36.pyc
/usr/lib64/totem/plugins/pythonconsole/console.py
/usr/lib64/totem/plugins/pythonconsole/pythonconsole.plugin
/usr/lib64/totem/plugins/pythonconsole/pythonconsole.py
/usr/lib64/totem/plugins/recent/recent.plugin
/usr/lib64/totem/plugins/save-file/save-file.plugin
/usr/lib64/totem/plugins/screensaver/screensaver.plugin
/usr/lib64/totem/plugins/screenshot/gallery.ui
/usr/lib64/totem/plugins/screenshot/screenshot.plugin
/usr/lib64/totem/plugins/skipto/skipto.plugin
/usr/lib64/totem/plugins/skipto/skipto.ui
/usr/lib64/totem/plugins/variable-rate/variable-rate.plugin
/usr/lib64/totem/plugins/vimeo/vimeo.plugin

%files bin
%defattr(-,root,root,-)
/usr/bin/totem
/usr/bin/totem-video-thumbnailer
/usr/libexec/totem-gallery-thumbnailer

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/Totem-1.0.typelib
/usr/share/GConf/gsettings/opensubtitles.convert
/usr/share/GConf/gsettings/pythonconsole.convert
/usr/share/GConf/gsettings/totem.convert
/usr/share/applications/org.gnome.Totem.desktop
/usr/share/dbus-1/services/org.gnome.Totem.service
/usr/share/gir-1.0/*.gir
/usr/share/glib-2.0/schemas/org.gnome.totem.enums.xml
/usr/share/glib-2.0/schemas/org.gnome.totem.gschema.xml
/usr/share/glib-2.0/schemas/org.gnome.totem.plugins.opensubtitles.gschema.xml
/usr/share/glib-2.0/schemas/org.gnome.totem.plugins.pythonconsole.gschema.xml
/usr/share/icons/hicolor/16x16/apps/org.gnome.Totem.png
/usr/share/icons/hicolor/22x22/apps/org.gnome.Totem.png
/usr/share/icons/hicolor/24x24/apps/org.gnome.Totem.png
/usr/share/icons/hicolor/256x256/apps/org.gnome.Totem.png
/usr/share/icons/hicolor/32x32/apps/org.gnome.Totem.png
/usr/share/icons/hicolor/48x48/apps/org.gnome.Totem.png
/usr/share/icons/hicolor/symbolic/apps/org.gnome.Totem-symbolic.svg
/usr/share/metainfo/org.gnome.Totem.appdata.xml
/usr/share/thumbnailers/totem.thumbnailer
/usr/share/totem/controls.ui
/usr/share/totem/playlist.ui
/usr/share/totem/preferences.ui
/usr/share/totem/properties.ui
/usr/share/totem/shortcuts.ui
/usr/share/totem/totem.ui
/usr/share/totem/uri.ui

%files dev
%defattr(-,root,root,-)
/usr/include/totem/1.0/totem-dirs.h
/usr/include/totem/1.0/totem-interface.h
/usr/include/totem/1.0/totem-plugin.h
/usr/include/totem/1.0/totem.h
/usr/lib64/libtotem.so
/usr/lib64/pkgconfig/totem.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*
/usr/share/help/C/totem/figures/totem_next_button.png
/usr/share/help/C/totem/figures/totem_pause_button.png
/usr/share/help/C/totem/figures/totem_play_button.png
/usr/share/help/C/totem/figures/totem_previous_button.png
/usr/share/help/C/totem/figures/totem_show_playlist_button.png
/usr/share/help/C/totem/figures/totem_start_window.png
/usr/share/help/C/totem/figures/totem_volume_maximum_button.png
/usr/share/help/C/totem/figures/totem_volume_mute_button.png
/usr/share/help/C/totem/index.docbook
/usr/share/help/C/totem/legal.xml
/usr/share/help/bg/totem/figures/totem_next_button.png
/usr/share/help/bg/totem/figures/totem_pause_button.png
/usr/share/help/bg/totem/figures/totem_play_button.png
/usr/share/help/bg/totem/figures/totem_previous_button.png
/usr/share/help/bg/totem/figures/totem_show_playlist_button.png
/usr/share/help/bg/totem/figures/totem_start_window.png
/usr/share/help/bg/totem/figures/totem_volume_maximum_button.png
/usr/share/help/bg/totem/figures/totem_volume_mute_button.png
/usr/share/help/bg/totem/index.docbook
/usr/share/help/bg/totem/legal.xml
/usr/share/help/ca/totem/figures/totem_next_button.png
/usr/share/help/ca/totem/figures/totem_pause_button.png
/usr/share/help/ca/totem/figures/totem_play_button.png
/usr/share/help/ca/totem/figures/totem_previous_button.png
/usr/share/help/ca/totem/figures/totem_show_playlist_button.png
/usr/share/help/ca/totem/figures/totem_start_window.png
/usr/share/help/ca/totem/figures/totem_volume_maximum_button.png
/usr/share/help/ca/totem/figures/totem_volume_mute_button.png
/usr/share/help/ca/totem/index.docbook
/usr/share/help/ca/totem/legal.xml
/usr/share/help/cs/totem/figures/totem_next_button.png
/usr/share/help/cs/totem/figures/totem_pause_button.png
/usr/share/help/cs/totem/figures/totem_play_button.png
/usr/share/help/cs/totem/figures/totem_previous_button.png
/usr/share/help/cs/totem/figures/totem_show_playlist_button.png
/usr/share/help/cs/totem/figures/totem_start_window.png
/usr/share/help/cs/totem/figures/totem_volume_maximum_button.png
/usr/share/help/cs/totem/figures/totem_volume_mute_button.png
/usr/share/help/cs/totem/index.docbook
/usr/share/help/cs/totem/legal.xml
/usr/share/help/da/totem/figures/totem_next_button.png
/usr/share/help/da/totem/figures/totem_pause_button.png
/usr/share/help/da/totem/figures/totem_play_button.png
/usr/share/help/da/totem/figures/totem_previous_button.png
/usr/share/help/da/totem/figures/totem_show_playlist_button.png
/usr/share/help/da/totem/figures/totem_start_window.png
/usr/share/help/da/totem/figures/totem_volume_maximum_button.png
/usr/share/help/da/totem/figures/totem_volume_mute_button.png
/usr/share/help/da/totem/index.docbook
/usr/share/help/da/totem/legal.xml
/usr/share/help/de/totem/figures/totem_next_button.png
/usr/share/help/de/totem/figures/totem_pause_button.png
/usr/share/help/de/totem/figures/totem_play_button.png
/usr/share/help/de/totem/figures/totem_previous_button.png
/usr/share/help/de/totem/figures/totem_show_playlist_button.png
/usr/share/help/de/totem/figures/totem_start_window.png
/usr/share/help/de/totem/figures/totem_volume_maximum_button.png
/usr/share/help/de/totem/figures/totem_volume_mute_button.png
/usr/share/help/de/totem/index.docbook
/usr/share/help/de/totem/legal.xml
/usr/share/help/el/totem/figures/totem_next_button.png
/usr/share/help/el/totem/figures/totem_pause_button.png
/usr/share/help/el/totem/figures/totem_play_button.png
/usr/share/help/el/totem/figures/totem_previous_button.png
/usr/share/help/el/totem/figures/totem_show_playlist_button.png
/usr/share/help/el/totem/figures/totem_start_window.png
/usr/share/help/el/totem/figures/totem_volume_maximum_button.png
/usr/share/help/el/totem/figures/totem_volume_mute_button.png
/usr/share/help/el/totem/index.docbook
/usr/share/help/el/totem/legal.xml
/usr/share/help/en_GB/totem/figures/totem_next_button.png
/usr/share/help/en_GB/totem/figures/totem_pause_button.png
/usr/share/help/en_GB/totem/figures/totem_play_button.png
/usr/share/help/en_GB/totem/figures/totem_previous_button.png
/usr/share/help/en_GB/totem/figures/totem_show_playlist_button.png
/usr/share/help/en_GB/totem/figures/totem_start_window.png
/usr/share/help/en_GB/totem/figures/totem_volume_maximum_button.png
/usr/share/help/en_GB/totem/figures/totem_volume_mute_button.png
/usr/share/help/en_GB/totem/index.docbook
/usr/share/help/en_GB/totem/legal.xml
/usr/share/help/es/totem/figures/totem_next_button.png
/usr/share/help/es/totem/figures/totem_pause_button.png
/usr/share/help/es/totem/figures/totem_play_button.png
/usr/share/help/es/totem/figures/totem_previous_button.png
/usr/share/help/es/totem/figures/totem_show_playlist_button.png
/usr/share/help/es/totem/figures/totem_start_window.png
/usr/share/help/es/totem/figures/totem_volume_maximum_button.png
/usr/share/help/es/totem/figures/totem_volume_mute_button.png
/usr/share/help/es/totem/index.docbook
/usr/share/help/es/totem/legal.xml
/usr/share/help/eu/totem/figures/totem_next_button.png
/usr/share/help/eu/totem/figures/totem_pause_button.png
/usr/share/help/eu/totem/figures/totem_play_button.png
/usr/share/help/eu/totem/figures/totem_previous_button.png
/usr/share/help/eu/totem/figures/totem_show_playlist_button.png
/usr/share/help/eu/totem/figures/totem_start_window.png
/usr/share/help/eu/totem/figures/totem_volume_maximum_button.png
/usr/share/help/eu/totem/figures/totem_volume_mute_button.png
/usr/share/help/eu/totem/index.docbook
/usr/share/help/eu/totem/legal.xml
/usr/share/help/fi/totem/figures/totem_next_button.png
/usr/share/help/fi/totem/figures/totem_pause_button.png
/usr/share/help/fi/totem/figures/totem_play_button.png
/usr/share/help/fi/totem/figures/totem_previous_button.png
/usr/share/help/fi/totem/figures/totem_show_playlist_button.png
/usr/share/help/fi/totem/figures/totem_start_window.png
/usr/share/help/fi/totem/figures/totem_volume_maximum_button.png
/usr/share/help/fi/totem/figures/totem_volume_mute_button.png
/usr/share/help/fi/totem/index.docbook
/usr/share/help/fi/totem/legal.xml
/usr/share/help/fr/totem/figures/totem_next_button.png
/usr/share/help/fr/totem/figures/totem_pause_button.png
/usr/share/help/fr/totem/figures/totem_play_button.png
/usr/share/help/fr/totem/figures/totem_previous_button.png
/usr/share/help/fr/totem/figures/totem_show_playlist_button.png
/usr/share/help/fr/totem/figures/totem_start_window.png
/usr/share/help/fr/totem/figures/totem_volume_maximum_button.png
/usr/share/help/fr/totem/figures/totem_volume_mute_button.png
/usr/share/help/fr/totem/index.docbook
/usr/share/help/fr/totem/legal.xml
/usr/share/help/gl/totem/figures/totem_next_button.png
/usr/share/help/gl/totem/figures/totem_pause_button.png
/usr/share/help/gl/totem/figures/totem_play_button.png
/usr/share/help/gl/totem/figures/totem_previous_button.png
/usr/share/help/gl/totem/figures/totem_show_playlist_button.png
/usr/share/help/gl/totem/figures/totem_start_window.png
/usr/share/help/gl/totem/figures/totem_volume_maximum_button.png
/usr/share/help/gl/totem/figures/totem_volume_mute_button.png
/usr/share/help/gl/totem/index.docbook
/usr/share/help/gl/totem/legal.xml
/usr/share/help/id/totem/figures/totem_next_button.png
/usr/share/help/id/totem/figures/totem_pause_button.png
/usr/share/help/id/totem/figures/totem_play_button.png
/usr/share/help/id/totem/figures/totem_previous_button.png
/usr/share/help/id/totem/figures/totem_show_playlist_button.png
/usr/share/help/id/totem/figures/totem_start_window.png
/usr/share/help/id/totem/figures/totem_volume_maximum_button.png
/usr/share/help/id/totem/figures/totem_volume_mute_button.png
/usr/share/help/id/totem/index.docbook
/usr/share/help/id/totem/legal.xml
/usr/share/help/it/totem/figures/totem_next_button.png
/usr/share/help/it/totem/figures/totem_pause_button.png
/usr/share/help/it/totem/figures/totem_play_button.png
/usr/share/help/it/totem/figures/totem_previous_button.png
/usr/share/help/it/totem/figures/totem_show_playlist_button.png
/usr/share/help/it/totem/figures/totem_start_window.png
/usr/share/help/it/totem/figures/totem_volume_maximum_button.png
/usr/share/help/it/totem/figures/totem_volume_mute_button.png
/usr/share/help/it/totem/index.docbook
/usr/share/help/it/totem/legal.xml
/usr/share/help/ja/totem/figures/totem_next_button.png
/usr/share/help/ja/totem/figures/totem_pause_button.png
/usr/share/help/ja/totem/figures/totem_play_button.png
/usr/share/help/ja/totem/figures/totem_previous_button.png
/usr/share/help/ja/totem/figures/totem_show_playlist_button.png
/usr/share/help/ja/totem/figures/totem_start_window.png
/usr/share/help/ja/totem/figures/totem_volume_maximum_button.png
/usr/share/help/ja/totem/figures/totem_volume_mute_button.png
/usr/share/help/ja/totem/index.docbook
/usr/share/help/ja/totem/legal.xml
/usr/share/help/oc/totem/figures/totem_next_button.png
/usr/share/help/oc/totem/figures/totem_pause_button.png
/usr/share/help/oc/totem/figures/totem_play_button.png
/usr/share/help/oc/totem/figures/totem_previous_button.png
/usr/share/help/oc/totem/figures/totem_show_playlist_button.png
/usr/share/help/oc/totem/figures/totem_start_window.png
/usr/share/help/oc/totem/figures/totem_volume_maximum_button.png
/usr/share/help/oc/totem/figures/totem_volume_mute_button.png
/usr/share/help/oc/totem/index.docbook
/usr/share/help/oc/totem/legal.xml
/usr/share/help/pa/totem/figures/totem_next_button.png
/usr/share/help/pa/totem/figures/totem_pause_button.png
/usr/share/help/pa/totem/figures/totem_play_button.png
/usr/share/help/pa/totem/figures/totem_previous_button.png
/usr/share/help/pa/totem/figures/totem_show_playlist_button.png
/usr/share/help/pa/totem/figures/totem_start_window.png
/usr/share/help/pa/totem/figures/totem_volume_maximum_button.png
/usr/share/help/pa/totem/figures/totem_volume_mute_button.png
/usr/share/help/pa/totem/index.docbook
/usr/share/help/pa/totem/legal.xml
/usr/share/help/pl/totem/figures/totem_next_button.png
/usr/share/help/pl/totem/figures/totem_pause_button.png
/usr/share/help/pl/totem/figures/totem_play_button.png
/usr/share/help/pl/totem/figures/totem_previous_button.png
/usr/share/help/pl/totem/figures/totem_show_playlist_button.png
/usr/share/help/pl/totem/figures/totem_start_window.png
/usr/share/help/pl/totem/figures/totem_volume_maximum_button.png
/usr/share/help/pl/totem/figures/totem_volume_mute_button.png
/usr/share/help/pl/totem/index.docbook
/usr/share/help/pl/totem/legal.xml
/usr/share/help/pt_BR/totem/figures/totem_next_button.png
/usr/share/help/pt_BR/totem/figures/totem_pause_button.png
/usr/share/help/pt_BR/totem/figures/totem_play_button.png
/usr/share/help/pt_BR/totem/figures/totem_previous_button.png
/usr/share/help/pt_BR/totem/figures/totem_show_playlist_button.png
/usr/share/help/pt_BR/totem/figures/totem_start_window.png
/usr/share/help/pt_BR/totem/figures/totem_volume_maximum_button.png
/usr/share/help/pt_BR/totem/figures/totem_volume_mute_button.png
/usr/share/help/pt_BR/totem/index.docbook
/usr/share/help/pt_BR/totem/legal.xml
/usr/share/help/ro/totem/figures/totem_next_button.png
/usr/share/help/ro/totem/figures/totem_pause_button.png
/usr/share/help/ro/totem/figures/totem_play_button.png
/usr/share/help/ro/totem/figures/totem_previous_button.png
/usr/share/help/ro/totem/figures/totem_show_playlist_button.png
/usr/share/help/ro/totem/figures/totem_start_window.png
/usr/share/help/ro/totem/figures/totem_volume_maximum_button.png
/usr/share/help/ro/totem/figures/totem_volume_mute_button.png
/usr/share/help/ro/totem/index.docbook
/usr/share/help/ro/totem/legal.xml
/usr/share/help/ru/totem/figures/totem_next_button.png
/usr/share/help/ru/totem/figures/totem_pause_button.png
/usr/share/help/ru/totem/figures/totem_play_button.png
/usr/share/help/ru/totem/figures/totem_previous_button.png
/usr/share/help/ru/totem/figures/totem_show_playlist_button.png
/usr/share/help/ru/totem/figures/totem_start_window.png
/usr/share/help/ru/totem/figures/totem_volume_maximum_button.png
/usr/share/help/ru/totem/figures/totem_volume_mute_button.png
/usr/share/help/ru/totem/index.docbook
/usr/share/help/ru/totem/legal.xml
/usr/share/help/sl/totem/figures/totem_next_button.png
/usr/share/help/sl/totem/figures/totem_pause_button.png
/usr/share/help/sl/totem/figures/totem_play_button.png
/usr/share/help/sl/totem/figures/totem_previous_button.png
/usr/share/help/sl/totem/figures/totem_show_playlist_button.png
/usr/share/help/sl/totem/figures/totem_start_window.png
/usr/share/help/sl/totem/figures/totem_volume_maximum_button.png
/usr/share/help/sl/totem/figures/totem_volume_mute_button.png
/usr/share/help/sl/totem/index.docbook
/usr/share/help/sl/totem/legal.xml
/usr/share/help/sv/totem/figures/totem_next_button.png
/usr/share/help/sv/totem/figures/totem_pause_button.png
/usr/share/help/sv/totem/figures/totem_play_button.png
/usr/share/help/sv/totem/figures/totem_previous_button.png
/usr/share/help/sv/totem/figures/totem_show_playlist_button.png
/usr/share/help/sv/totem/figures/totem_start_window.png
/usr/share/help/sv/totem/figures/totem_volume_maximum_button.png
/usr/share/help/sv/totem/figures/totem_volume_mute_button.png
/usr/share/help/sv/totem/index.docbook
/usr/share/help/sv/totem/legal.xml
/usr/share/help/te/totem/figures/totem_next_button.png
/usr/share/help/te/totem/figures/totem_pause_button.png
/usr/share/help/te/totem/figures/totem_play_button.png
/usr/share/help/te/totem/figures/totem_previous_button.png
/usr/share/help/te/totem/figures/totem_show_playlist_button.png
/usr/share/help/te/totem/figures/totem_start_window.png
/usr/share/help/te/totem/figures/totem_volume_maximum_button.png
/usr/share/help/te/totem/figures/totem_volume_mute_button.png
/usr/share/help/te/totem/index.docbook
/usr/share/help/te/totem/legal.xml
/usr/share/help/uk/totem/figures/totem_next_button.png
/usr/share/help/uk/totem/figures/totem_pause_button.png
/usr/share/help/uk/totem/figures/totem_play_button.png
/usr/share/help/uk/totem/figures/totem_previous_button.png
/usr/share/help/uk/totem/figures/totem_show_playlist_button.png
/usr/share/help/uk/totem/figures/totem_start_window.png
/usr/share/help/uk/totem/figures/totem_volume_maximum_button.png
/usr/share/help/uk/totem/figures/totem_volume_mute_button.png
/usr/share/help/uk/totem/index.docbook
/usr/share/help/uk/totem/legal.xml
/usr/share/help/zh_CN/totem/figures/totem_next_button.png
/usr/share/help/zh_CN/totem/figures/totem_pause_button.png
/usr/share/help/zh_CN/totem/figures/totem_play_button.png
/usr/share/help/zh_CN/totem/figures/totem_previous_button.png
/usr/share/help/zh_CN/totem/figures/totem_show_playlist_button.png
/usr/share/help/zh_CN/totem/figures/totem_start_window.png
/usr/share/help/zh_CN/totem/figures/totem_volume_maximum_button.png
/usr/share/help/zh_CN/totem/figures/totem_volume_mute_button.png
/usr/share/help/zh_CN/totem/index.docbook
/usr/share/help/zh_CN/totem/legal.xml
/usr/share/help/zh_HK/totem/figures/totem_next_button.png
/usr/share/help/zh_HK/totem/figures/totem_pause_button.png
/usr/share/help/zh_HK/totem/figures/totem_play_button.png
/usr/share/help/zh_HK/totem/figures/totem_previous_button.png
/usr/share/help/zh_HK/totem/figures/totem_show_playlist_button.png
/usr/share/help/zh_HK/totem/figures/totem_start_window.png
/usr/share/help/zh_HK/totem/figures/totem_volume_maximum_button.png
/usr/share/help/zh_HK/totem/figures/totem_volume_mute_button.png
/usr/share/help/zh_HK/totem/index.docbook
/usr/share/help/zh_HK/totem/legal.xml
/usr/share/help/zh_TW/totem/figures/totem_next_button.png
/usr/share/help/zh_TW/totem/figures/totem_pause_button.png
/usr/share/help/zh_TW/totem/figures/totem_play_button.png
/usr/share/help/zh_TW/totem/figures/totem_previous_button.png
/usr/share/help/zh_TW/totem/figures/totem_show_playlist_button.png
/usr/share/help/zh_TW/totem/figures/totem_start_window.png
/usr/share/help/zh_TW/totem/figures/totem_volume_maximum_button.png
/usr/share/help/zh_TW/totem/figures/totem_volume_mute_button.png
/usr/share/help/zh_TW/totem/index.docbook
/usr/share/help/zh_TW/totem/legal.xml

%files lib
%defattr(-,root,root,-)
/usr/lib64/libtotem.so.0
/usr/lib64/libtotem.so.0.0.0
/usr/lib64/nautilus/extensions-3.0/libtotem-properties-page.so
/usr/lib64/totem/plugins/apple-trailers/libapple-trailers.so
/usr/lib64/totem/plugins/autoload-subtitles/libautoload-subtitles.so
/usr/lib64/totem/plugins/brasero-disc-recorder/libbrasero-disc-recorder.so
/usr/lib64/totem/plugins/gromit/libgromit.so
/usr/lib64/totem/plugins/im-status/libtotem-im-status.so
/usr/lib64/totem/plugins/media-player-keys/libmedia_player_keys.so
/usr/lib64/totem/plugins/ontop/libontop.so
/usr/lib64/totem/plugins/properties/libmovie-properties.so
/usr/lib64/totem/plugins/recent/librecent.so
/usr/lib64/totem/plugins/save-file/libsave-file.so
/usr/lib64/totem/plugins/screensaver/libscreensaver.so
/usr/lib64/totem/plugins/screenshot/libscreenshot.so
/usr/lib64/totem/plugins/skipto/libskipto.so
/usr/lib64/totem/plugins/variable-rate/libvariable-rate.so
/usr/lib64/totem/plugins/vimeo/libvimeo.so

%files locales -f totem.lang
%defattr(-,root,root,-)

