from api_access import getSpell
import unittest


class dndApiTest(unittest.TestCase):
    """Tests for `api request`."""
    def test_could_not_find_spell(self):
        """testing wrong spell format"""
        self.assertEqual(getSpell('fireball'),"sorry I couldn't find that spell")

    def test_found_spell(self):
        spell = getSpell('Fireball')
        spell2 = getSpell('Acid Splash')
        spell3 = getSpell('Alter Self')
        spell4 = getSpell('Animal Messenger')
        spell5 = getSpell('Animal Shapes')
        spell6 = getSpell('Remove Curse')
        self.assertEqual(spell['name'],'Fireball')
        self.assertEqual(spell2['name'], 'Acid Splash')
        self.assertEqual(spell3['name'], 'Alter Self')
        self.assertEqual(spell4['name'], 'Animal Messenger')
        self.assertEqual(spell5['name'], 'Animal Shapes')
        self.assertEqual(spell6['name'], 'Remove Curse')


if __name__ == '__main__':
    unittest.main()