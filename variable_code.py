import unittest


class TurretFactory:
    pass


class TurretTest(unittest.TestCase):

    def setUp(self):
        self.turret_factory = TurretFactory()
        self.turret = self.turret_factory.CreateTurret()

    def test_turret_is_on_by_default(self):
        self.assertEquals(True, self.turret.is_on())

    def test_turret_turns_can_be_turned_off(self):
        self.turret.turn_off()
        self.assertEquals(False, self.turret.is_on())
