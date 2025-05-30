# encoding:utf-8
#
# Gramps - a GTK+/GNOME based genealogy program
#
# Copyright (C) 2009 Benny Malengier
# Copyright (C) 2013 Pat Lefebre
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
# Created by
# authors = ["Pat Lefebre"],
# authors_email = ["patbree49@zoho.com"],

# ------------------------------------------------------------------------
#
# H-tree view for Gramps
#
# ------------------------------------------------------------------------
register(
    VIEW,
    id="HtreePedigreeView",
    name=_("H-Tree Pedigree"),
    category=("Ancestry", _("Charts")),
    description=_(
        "The view shows a space-efficient pedigree with "
        "ancestors of the selected person"
    ),
    version = '0.0.35',
    gramps_target_version="6.0",
    status=STABLE,
    fname="HtreePedigreeView.py",
    authors=["Pat Lefebre"],
    authors_email=[""],
    viewclass="HtreePedigreeView",
    icons=[("gramps-htree", _("H-Tree Pedigree"))],
    stock_icon="gramps-htree",
    help_url="Addon:HtreePedigreeView",
)
