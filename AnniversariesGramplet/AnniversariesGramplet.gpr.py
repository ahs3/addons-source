#
# Gramps - a GTK+/GNOME based genealogy program
#
# Copyright (C) 2023  Nick Hall
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
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#

register(
    GRAMPLET,
    id="Anniversaries",
    name=_("Anniversaries"),
    description=_("A gramplet that displays the anniversaries of events"),
    status=STABLE,
    version="1.0.3",
    fname="AnniversariesGramplet.py",
    height=200,
    gramplet="AnniversariesGramplet",
    gramps_target_version="6.0",
    gramplet_title=_("Anniversaries"),
    help_url="AnniversariesGramplet",
)
