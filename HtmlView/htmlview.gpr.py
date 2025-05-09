# encoding:utf-8
#
# Gramps - a GTK+/GNOME based genealogy program
#
# Copyright (C) 2009 Benny Malengier
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

# ------------------------------------------------------------------------
#
# HtmlView
#
# ------------------------------------------------------------------------

register(
    VIEW,
    id="htmlview",
    name=_("Html View"),
    description=_("A view showing html pages embedded in Gramps"),
    version = '1.0.16',
    gramps_target_version="6.0",
    status=STABLE,
    include_in_listing=False,
    fname="htmlview.py",
    authors=["The Gramps project"],
    authors_email=["http://gramps-project.org"],
    category=("Web", _("Web")),
    viewclass="HtmlView",
)
