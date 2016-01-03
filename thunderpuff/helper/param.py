
def String(description, **kwargs):
    """
    Shorthand for {"Type": "String", "Description": description} + **kwargs
    """
    d = {
        "Type": "String",
        "Description": description,
    }
    d.update(kwargs)
    return d
