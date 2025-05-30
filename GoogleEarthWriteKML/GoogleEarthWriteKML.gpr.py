#
# Gramps - a GTK+/GNOME based genealogy program
#
# Copyright (C) 2009       Peter Landgren
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

# $Id: GoogleEarthWriteKML.py.py 11946 2009-02-13 06:06:14Z ldnp $

# ------------------------------------------------------------------------
#
# Register map service
#
# ------------------------------------------------------------------------
register(
    MAPSERVICE,
    id="GoogleEarth",
    name=_("GoogleEarth"),
    version = '1.0.53',
    gramps_target_version="6.0",
    status=STABLE,
    fname="GoogleEarthWriteKML.py",
    description=_("Creates data file for GoogleEarth and opens it"),
    mapservice="GoogleEarthService",
    authors=["Peter Landgren"],
    authors_email=["peter.talken@telia.com"],
    help_url="Addon:MapService-GoogleEarth",
)
