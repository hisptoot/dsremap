#!/usr/bin/env python3

from pyqtcmd import Command

from dsrlib.domain.mixins import ConfigurationMixin


class ChangeConfigurationNameCommand(ConfigurationMixin, Command):
    def __init__(self, *, configuration, name):
        super().__init__(configuration=configuration)
        self._oldName = configuration.name()
        self._newName = name

    def do(self):
        self.configuration().setName(self._newName)

    def undo(self):
        self.configuration().setName(self._oldName)


class ChangeConfigurationThumbnailCommand(ConfigurationMixin, Command):
    def __init__(self, *, configuration, filename):
        super().__init__(configuration=configuration)
        self._oldFilename = configuration.thumbnail()
        self._newFilename = filename

    def do(self):
        self.configuration().setThumbnail(self._newFilename)

    def undo(self):
        self.configuration().setThumbnail(self._oldFilename)


class AddActionCommand(ConfigurationMixin, Command):
    def __init__(self, *, action, configuration):
        super().__init__(configuration=configuration)
        self._action = action

    def do(self):
        self.configuration().addAction(self._action)

    def undo(self):
        self.configuration().removeAction(self._action)


class DeleteActionsCommand(ConfigurationMixin, Command):
    def __init__(self, *, actions, configuration):
        super().__init__(configuration=configuration)
        self._actions = sorted([(self.actions().indexOf(action), action) for action in actions])

    def do(self):
        for _, action in self._actions:
            self.configuration().removeAction(action)

    def undo(self):
        for index, action in self._actions:
            self.configuration().addAction(action, index=index)


class SetConfigurationEnabledCommand(ConfigurationMixin, Command):
    def __init__(self, *, enabled, configuration):
        super().__init__(configuration=configuration)
        self._newEnabled = enabled
        self._oldEnabled = configuration.enabled()

    def do(self):
        self.configuration().setEnabled(self._newEnabled)

    def undo(self):
        self.configuration().setEnabled(self._oldEnabled)
