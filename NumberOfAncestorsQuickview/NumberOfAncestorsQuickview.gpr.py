register(
    QUICKREPORT,
    id="NumberOfAncestorsQuickview",
    name=_("Number of ancestors"),
    description=_("Shows the number of ancestors of the current person"),
    version = '1.0.12',
    gramps_target_version="6.0",
    status=STABLE,
    fname="NumberOfAncestorsQuickview.py",
    authors=["Matthias Kemmer"],
    authors_email=["matt.familienforschung@gmail.com"],
    category=CATEGORY_QR_PERSON,
    runfunc="run",
    help_url="Addon:NumberOfAncestorsQuickView",
)
