import unittest

import regex


class TestRegex(unittest.TestCase):
    def test_parse_reg_ex(self):
        #  tests for Stage 3
        self.assertEqual(regex.parse_reg_ex("a.bc"), ['a', '.', "bc"])
        #  tests for Stage 4
        self.assertEqual(regex.parse_reg_ex("^abc^"), ['^', "abc^"])
        self.assertEqual(regex.parse_reg_ex("$abc$"), ["$abc", '$'])
        self.assertEqual(regex.parse_reg_ex("^abc$"), ['^', "abc", '$'])
        self.assertEqual(regex.parse_reg_ex("^abc"), ['^', "abc"])
        self.assertEqual(regex.parse_reg_ex("abc$"), ["abc", '$'])
        #  tests for Stage 5
        self.assertEqual(regex.parse_reg_ex("a?bc"), ["a?", "bc"])
        self.assertEqual(regex.parse_reg_ex("ab?c"), ['a', "b?", 'c'])
        self.assertEqual(regex.parse_reg_ex("abc?"), ["ab", "c?"])
        self.assertEqual(regex.parse_reg_ex("a.?"), ['a', ".?"])
        self.assertEqual(regex.parse_reg_ex("a.?c"), ['a', ".?", 'c'])
        self.assertEqual(regex.parse_reg_ex("ab.?"), ["ab", ".?"])
        self.assertEqual(regex.parse_reg_ex(".?a"), [".?", 'a'])
        self.assertEqual(regex.parse_reg_ex("..?a"), ['.', ".?", 'a'])
        self.assertEqual(regex.parse_reg_ex("^?abc"), ['^', "?abc"])
        self.assertEqual(regex.parse_reg_ex("a*bc"), ["a*", "bc"])
        self.assertEqual(regex.parse_reg_ex("ab*c"), ['a', "b*", 'c'])
        self.assertEqual(regex.parse_reg_ex("abc*"), ["ab", "c*"])
        self.assertEqual(regex.parse_reg_ex("a.*"), ['a', ".*"])
        self.assertEqual(regex.parse_reg_ex("a.*c"), ['a', ".*", 'c'])
        self.assertEqual(regex.parse_reg_ex("ab.*"), ["ab", ".*"])
        self.assertEqual(regex.parse_reg_ex("^*abc"), ['^', "*abc"])
        self.assertEqual(regex.parse_reg_ex(".*a"), [".*", 'a'])
        self.assertEqual(regex.parse_reg_ex("..*a"), ['.', ".*", 'a'])
        self.assertEqual(regex.parse_reg_ex("a+bc"), ["a+", "bc"])
        self.assertEqual(regex.parse_reg_ex("ab+c"), ['a', "b+", 'c'])
        self.assertEqual(regex.parse_reg_ex("abc+"), ["ab", "c+"])
        self.assertEqual(regex.parse_reg_ex("a.+"), ['a', ".+"])
        self.assertEqual(regex.parse_reg_ex("a.+c"), ['a', ".+", 'c'])
        self.assertEqual(regex.parse_reg_ex("ab.+"), ["ab", ".+"])
        self.assertEqual(regex.parse_reg_ex("^+abc"), ['^', "+abc"])
        self.assertEqual(regex.parse_reg_ex(".+a"), [".+", 'a'])
        self.assertEqual(regex.parse_reg_ex("..+a"), ['.', ".+", 'a'])

    def test_process_string(self):
        #  tests for Stages 1-3
        self.assertTrue(regex.process_string("abc", ['']))
        self.assertFalse(regex.process_string('', ['a']))
        self.assertTrue(regex.process_string("abc", ['.', "bc"]))
        self.assertTrue(regex.process_string("abc", ['a', '.', 'c']))
        self.assertTrue(regex.process_string("abc", ["ab", '.']))
        self.assertTrue(regex.process_string("a bc", ["bc"]))
        self.assertTrue(regex.process_string(" abc", ["bc"]))
        self.assertTrue(regex.process_string("abc ", ["bc"]))
        self.assertTrue(regex.process_string("abc de", ["abc d"]))
        self.assertTrue(regex.process_string(" abc de", ["abc d"]))
        self.assertTrue(regex.process_string("abc de ", ["abc d"]))
        self.assertTrue(regex.process_string(" abc de", [" abc"]))
        self.assertTrue(regex.process_string("abc de ", ["de "]))
        self.assertFalse(regex.process_string("a\nc", ['a', '.', 'c']))
        #  tests for a Stage 4
        self.assertTrue(regex.process_string("abc", ['^', "ab"]))
        self.assertTrue(regex.process_string("become", ['^', "be"]))
        self.assertFalse(regex.process_string("to be", ['^', "be"]))
        self.assertTrue(regex.process_string("abc", ["bc", '$']))
        self.assertTrue(regex.process_string("abc", ['^', "abc", '$']))
        self.assertTrue(regex.process_string("section", ["tion", '$']))
        self.assertFalse(regex.process_string("sections", ["tion", '$']))
        self.assertTrue(regex.process_string("apple", ['.', '$']))
        self.assertTrue(regex.process_string("apple", ['l', '.', '$']))
        #  tests for a Stage 5
        self.assertTrue(regex.process_string("aaaaaaaaaabc", ['a*', 'bc']))
        self.assertTrue(regex.process_string("bc", ['a*', 'bc']))
        self.assertTrue(regex.process_string("abcccccccccc", ["ab", 'c*']))
        self.assertTrue(regex.process_string("ab", ["ab", 'c*']))
        self.assertTrue(regex.process_string("aaaaaaaaaabc", ['a+', 'bc']))
        self.assertTrue(regex.process_string("abcccccccccc", ["ab", 'c+']))
        self.assertTrue(regex.process_string("color", ["colo", 'u?', 'r']))
        self.assertTrue(regex.process_string("colour", ["colo", 'u?', 'r']))
        self.assertFalse(regex.process_string("colouur", ["colo", 'u?', 'r']))
        self.assertTrue(regex.process_string("color", ["colo", 'u*', 'r']))
        self.assertTrue(regex.process_string("colour", ["colo", 'u*', 'r']))
        self.assertTrue(regex.process_string("colouur", ["colo", 'u*', 'r']))
        self.assertTrue(regex.process_string("color", ["col", '.*', 'r']))
        self.assertTrue(regex.process_string("colour", ["col", '.*', 'r']))
        self.assertTrue(regex.process_string("colr", ["col", '.*', 'r']))
        #  tests for a Stage 6
