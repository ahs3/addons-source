register(
    GRAMPLET,
    id="Face Detection",
    name=_("Face Detection"),
    description=_("Gramplet for detecting and assigning faces"),
    version = '1.0.33',
    gramps_target_version="6.0",
    include_in_listing=False,
    status=UNSTABLE,  # not yet tested with python 3
    fname="FaceDetection.py",
    height=200,
    gramplet="FaceDetection",
    gramplet_title=_("Faces"),
    navtypes=["Media"],
)
