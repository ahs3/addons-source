# ------------------------------------------------------------------------
#
# Register the Addon
#
# ------------------------------------------------------------------------

register(
    GENERAL,
    category="WebConnect",
    id="UK Web Connect Pack",
    name=_("UK Web Connect Pack"),
    description=_("Collection of Web sites for the UK (requires libwebconnect)"),
    status=STABLE,
    version = '1.0.43',
    gramps_target_version="6.0",
    fname="UKWebPack.py",
    load_on_reg=True,
    depends_on=["libwebconnect"],
    help_url="Addon:Web_Connect_Pack#Available_Web_connect_Packs",
)
