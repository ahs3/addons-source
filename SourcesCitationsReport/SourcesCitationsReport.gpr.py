#
# Gramps - a GTK+/GNOME based genealogy program
#
# Copyright (C) 2010 Adam Sampson <ats-familytree@offog.org>
# Copyright (C) 2010 Jerome Rapinat <romjerome@yahoo.fr>
# Copyright (C) 2010, 2012 lcc <lcc.mailaddress@gmail.com>
# Copyright (C) 2015 Don Piercy
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
# SourcesCitations Report
#
# ------------------------------------------------------------------------

register(
    REPORT,
    id="SourcesCitationsReport",
    name=_("Sources and Citations Report"),
    description=_("Provides a source and Citations Report with notes"),
    version = '3.6.15',
    gramps_target_version="6.0",
    status=STABLE,
    fname="SourcesCitationsReport.py",
    authors=["Uli22"],
    authors_email=["hansulrich.frink@gmail.com"],
    category=CATEGORY_TEXT,
    reportclass="SourcesCitationsReport",
    optionclass="SourcesCitationsOptions",
    report_modes=[REPORT_MODE_GUI, REPORT_MODE_BKI, REPORT_MODE_CLI],
    require_active=False,
    help_url="Addon:SourcesCitationsReport",
)
