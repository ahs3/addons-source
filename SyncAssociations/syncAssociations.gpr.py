register(
    TOOL,
    id="syncAssociations",
    name=_("Sync Associations"),
    description=_(
        "Traverses the Person list for all Associations that are bi-directional and adds any which are missing to the Associated Person."
    ),
    version = '0.0.14',
    gramps_target_version="6.0",
    status=STABLE,
    fname="syncAssociations.py",
    authors=["Gary Griffin"],
    authors_email=["genealogy@garygriffin.net"],
    category=TOOL_DBPROC,
    toolclass="syncAssociations",
    optionclass="syncAssociationsOptions",
    tool_modes=[TOOL_MODE_GUI, TOOL_MODE_CLI],
    help_url="Addon:SyncAssociation",
)

__author__ = "gary griffin"
