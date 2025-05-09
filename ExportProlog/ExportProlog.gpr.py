register(
    EXPORT,
    id="Prolog Export",
    name=_("Prolog Export"),
    description=_(
        "Exports data into a Prolog fact format.  " "Data is in Unicode (utf-8)"
    ),
    version = '1.0.21',
    gramps_target_version="6.0",
    status=STABLE,
    fname="ExportProlog.py",
    export_function="exportData",
    extension="pl",
    help_url="Output_formats#Prolog",
)
