# -*- coding: UTF-8 -*-


"""
Unittests for emojiar.unicode_codes
"""


import emojiar


def test_emoji_names():

    for use_aliases, group in (
            (False, emojiar.unicode_codes.EMOJI_UNICODE),
            (True, emojiar.unicode_codes.EMOJI_ALIAS_UNICODE)):
        for name, ucode in group.items():
            assert name.startswith(':') and name.endswith(':') and len(name) >= 3
            emj = emojiar.emojize(name, use_aliases=use_aliases)
            assert emj == ucode, "%s != %s" % (emojiar.emojize(name), ucode)


def test_compare_normal_and_aliases():
    # There should always be more aliases than normal codes since the aliases contain
    # the normal codes
    assert len(emojiar.EMOJI_UNICODE) < len(emojiar.EMOJI_ALIAS_UNICODE)