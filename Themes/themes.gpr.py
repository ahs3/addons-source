#
# Gramps - a GTK+/GNOME based genealogy program
#
# Copyright (C) 2019      Paul Culley
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#

# ------------------------------------------------------------------------
#
# Themes
#
# ------------------------------------------------------------------------
register(
    GENERAL,
    id="ThemesPrefs",
    name=_("Theme preferences"),
    description=_(
        "An addition to Preferences for simple Theme and Font"
        " adjustment.  Especially useful for Windows users."
    ),
    version = '0.0.16',
    gramps_target_version="6.0",
    fname="themes_load.py",
    authors=["Paul Culley"],
    authors_email=["paulr2787@gmail.com"],
    category=TOOL_UTILS,
    load_on_reg=True,
    status=STABLE,
    help_url="Addon:ThemePreferences",
)
