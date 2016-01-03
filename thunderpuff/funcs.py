
def join(*args, **kwargs):
    """
    Return an intrinsic joining each argument together with an empty seperator.

    join("foo", bar) is shorthand for:

    {"Fn::Join": ["", list(("foo", bar))]}
    """
    sep = kwargs.pop("sep", "")
    assert not kwargs, "unknown params specified: {}".format(kwargs.keys())
    return {"Fn::Join": [sep, list(args)]}
