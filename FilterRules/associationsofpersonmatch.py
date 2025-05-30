#
# Gramps - a GTK+/GNOME based genealogy program
#
# Copyright (C) 2020    Matthias Kemmer
# Copyright (C) 2025    Steve Youngs
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
"""Filter rule matching associations of <person filter>."""

# -------------------------------------------------------------------------
#
# Standard python modules
#
# -------------------------------------------------------------------------
from __future__ import annotations

# -------------------------------------------------------------------------
#
# Gramps modules
#
# -------------------------------------------------------------------------
from gramps.gen.filters.rules import Rule
from gramps.gen.filters.rules.person._matchesfilter import MatchesFilter
from gramps.gen.const import GRAMPS_LOCALE as glocale

# -------------------------------------------------------------------------
#
# Typing modules
#
# -------------------------------------------------------------------------
from typing import Set
from gramps.gen.types import PersonHandle
from gramps.gen.lib import Person
from gramps.gen.db import Database

try:
    _trans = glocale.get_addon_translator(__file__)
except ValueError:
    _trans = glocale.translation
_ = _trans.gettext


# -------------------------------------------------------------------------
#
# Associations of <person filter>
#
# -------------------------------------------------------------------------
class AssociationsOfPersonMatch(Rule):
    """Filter rule matching associations of <person filter>."""

    labels = [_('Filter name:')]
    name = _('Match associations of <person filter>')
    description = _("Match associations of <person filter>")
    category = _('General filters')
    namespace = 'Person'

    def prepare(self, db: Database, user):
        """Prepare a reference list for the filter."""

        iter_persons = db.iter_person_handles()
        filter_ = MatchesFilter(self.list).find_filter()
        handle_list = filter_.apply(db, iter_persons, user=user)

        self.selected_handles: Set[PersonHandle] = set()
        for handle in handle_list:
            person = db.get_raw_person_data(handle)
            self.selected_handles.update([r.ref for r in person.person_ref_list])

    def apply_to_one(self, db: Database, person: Person) -> bool:
        """Check if the rule matches the person."""
        return person.handle in self.selected_handles
