import thunderpuff.scripts.make as make


def test_tag_call():

    assert make.is_tags([{"Key": "Foo", "Value": "Bar"}])

    assert make.is_tags([{"Key": "Foo", "Value": "Bar"}])
