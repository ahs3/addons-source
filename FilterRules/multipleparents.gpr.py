#
# Gramps - a GTK+/GNOME based genealogy program
#
# Copyright (C) 2021       Davis E Scheipers
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

"""
People with multiple parent records
"""
register(
    RULE,
    id="multipleparents",
    name=_("Multiple Parents Filter"),
    description=_("Multiple Parents Filter"),
    version = '0.0.14',
    authors=["Dave Scheipers"],
    authors_email=["dave.scheipers@gmail.com"],
    gramps_target_version="6.0",
    status=STABLE,
    fname="multipleparents.py",
    ruleclass="MultipleParents",  # must be rule class name
    namespace="Person",  # one of the primary object classes
    help_url="Addon:Rule_expansions#People_with_multiple_parent_records",
)
